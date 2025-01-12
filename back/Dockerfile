FROM python:slim-bullseye

# miseの環境変数の設定
ENV MISE_DATA_DIR="/mise" \
    MISE_CONFIG_DIR="/mise" \
    MISE_CACHE_DIR="/mise/cache" \
    MISE_INSTALL_PATH="/usr/local/bin/mise" \
    UV_LINK_MODE=copy \
    UV_COMPILE_BYTCODE=1 \ 
    PATH="/mise/shims:$PATH"

WORKDIR /app
COPY mise.toml pyproject.toml uv.lock ./

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

# Debian日本語化, MISEインストール, MISEパッケージインストール
RUN apt-get update && apt-get install -y --no-install-recommends \
    locales \
    curl \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean -y \
    && sed -i -e 's/# \(ja_JP.UTF-8\)/\1/' /etc/locale.gen \
    && locale-gen \
    && update-locale LANG=ja_JP.UTF-8 \
    && curl https://mise.run | sh \
    && mise trust mise.toml \
    && mise install \
    && uv sync --no-install-project