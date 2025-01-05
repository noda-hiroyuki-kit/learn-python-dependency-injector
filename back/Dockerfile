FROM python:slim-bullseye

# Debian日本語化, MISEインストール
RUN apt-get update && apt-get install -y \
    locales \
    curl \
    && curl https://mise.run | MISE_INSTALL_PATH=/usr/local/bin/mise sh \
    && echo 'eval "$(mise activate bash)"' >> ~/.bashrc \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean -y \
    && sed -i -e 's/# \(ja_JP.UTF-8\)/\1/' /etc/locale.gen \
    && locale-gen \
    && update-locale LANG=ja_JP.UTF-8