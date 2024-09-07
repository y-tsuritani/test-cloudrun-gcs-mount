# ベースイメージ
FROM python:3.12.4-slim-bookworm

# 作業ディレクトリの設定
WORKDIR /app

# 必要なPythonパッケージをインストール
COPY requirements.txt .
RUN pip install -r requirements.txt

# アプリケーションのコードをコピー
COPY . .

ENV PORT 8080

# Flaskアプリケーションを起動
CMD ["python", "main.py"]