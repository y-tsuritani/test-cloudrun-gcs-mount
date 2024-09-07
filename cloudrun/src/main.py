import os

import pandas as pd
from flask import Flask
from google.cloud import bigquery

app = Flask(__name__)

# Cloud Storageのボリュームマウントポイント
MOUNT_PATH = os.environ.get("MOUNT_PATH", "/mnt/gcs")
PROJECT_ID = os.environ.get("PROJECT_ID", "any-development")
TABLE_NAME = os.environ.get("TABLE_NAME", "users")
SOURCE_DATASET = os.environ.get("SOURCE_DATASET", "TEST_DATA")
FILE_NAME = "users.gzip"
DESTINATION_URI = f"{MOUNT_PATH}/{FILE_NAME}"

@app.route('/')
def main():
    # BigQueryクライアントの初期化
    client = bigquery.Client()

    # MOUNT_PATH ディレクトリ内のファイルを再起的に削除
    os.system(f"rm -rf {MOUNT_PATH}/*")
    print(f"Deleted all files in {MOUNT_PATH}")

    query = f"SELECT * FROM {SOURCE_DATASET}.{TABLE_NAME}"
    query_job = client.query(query)
    print(f"Executing query: {query}")
    print(f"Result: {query_job.result()}")
    df = query_job.to_dataframe()

    # BigQueryからテーブルデータをロード
    df.to_csv(DESTINATION_URI, compression="gzip", index=False)

    return f"Exported {SOURCE_DATASET}.{TABLE_NAME} to {DESTINATION_URI}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
