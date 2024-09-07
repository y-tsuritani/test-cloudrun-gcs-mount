from flask import Flask
import os

app = Flask(__name__)

# Cloud Storageのボリュームマウントポイント
MOUNT_PATH = "/gcs"
FILE_NAME = "test-file.txt"
FILE_PATH = os.path.join(MOUNT_PATH, FILE_NAME)

@app.route('/')
def index():
    # ファイルに書き込むテキスト
    content_to_write = "Hello from Cloud Run and Cloud Storage!"

    # ファイルに書き込み
    with open(FILE_PATH, 'w') as file:
        file.write(content_to_write)

    # ファイルを読み込み
    with open(FILE_PATH, 'r') as file:
        content = file.read()

    return f"File content: {content}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))