# python v3.6 をベースにDockerイメージを作成
FROM python:3.6

# 作業ディレクトリを指定
WORKDIR /app

# カレントディレクトリのファイルをDockerコンテナの｢/app｣ ディレクトリにコピー
ADD . /app

# インストール
RUN pip install -r requirements.txt

# 外部に公開するポートを指定
EXPOSE 5002

# コンテナの実行コマンドを指定
CMD ["python", "app.py"]
