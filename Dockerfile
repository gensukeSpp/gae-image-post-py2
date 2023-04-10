# ビルド・ランタイム共通のPythonバージョン
ARG PYTHON_VERSION="3.10"

# ビルド用
FROM python:${PYTHON_VERSION} as build-env

# Pythonスクリプトをローカルからコピー
COPY . /app
WORKDIR /app

# venvのセットアップ・ライブラリインストール
RUN python -m venv ./venv
RUN . venv/bin/activate && pip install -U pip && pip install -r requirements.txt -t lib/

# ランタイム
FROM python:${PYTHON_VERSION}-slim

ENV PYTHONBUFFERED=1
# venvのpythonを使用するようにする
ENV PATH /venv/bin:$PATH

# venv含めてPythonスクリプトをビルド用環境からコピー
COPY --from=build-env /app /

# ランタイムで必要なライブラリインストール
RUN apt-get update && apt-get install -y
# 必要なライブラリ
RUN apt-get clean
RUN rm -rf /var/lib/apt/lists/*

ENTRYPOINT ["source", "bin/activate"]
