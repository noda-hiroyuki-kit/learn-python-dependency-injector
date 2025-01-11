FROM python:slim-bullseye

# Debian日本語化
RUN apt-get update && apt-get install -y --no-install-recommends \
    locales \
    curl \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean -y \
    && sed -i -e 's/# \(ja_JP.UTF-8\)/\1/' /etc/locale.gen \
    && locale-gen \
    && update-locale LANG=ja_JP.UTF-8

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

# miseの環境変数の設定
ENV MISE_DATA_DIR="/mise"
ENV MISE_CONFIG_DIR="/mise"
ENV MISE_CACHE_DIR="/mise/cache"
ENV MISE_INSTALL_PATH="/usr/local/bin/mise"
ENV PATH="/mise/shims:$PATH"

WORKDIR /app
COPY mise.toml .

# MISEインストール, MISEパッケージインストール
RUN curl https://mise.run | sh \
    && mise trust mise.toml \
    && mise install