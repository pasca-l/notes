FROM ubuntu:20.04

WORKDIR /home/local/

# Flutter SDK
RUN apt update && apt upgrade -y \
    && apt install -y curl file git unzip xz-utils zip \
    && git clone https://github.com/flutter/flutter.git /usr/bin/flutter
ENV PATH /usr/bin/flutter/bin:$PATH

# ignores dialog
ENV DEBIAN_FRONTEND noninteractive

# Android toolchain (not necessary)

# Chrome (not necessary)
RUN apt install -y wget gnupg \
    # add package info (repository)
    && echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list \
    # download and register key
    && wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && apt update \
    && apt install -y google-chrome-stable

# Linux toolchain
RUN apt install -y clang cmake ninja-build pkg-config libgtk-3-dev

ENV DEBIAN_FRONTEND newt

CMD [ "flutter", "run", "-d", "web-server", "--web-port=8888", "--web-hostname=0.0.0.0" ]
