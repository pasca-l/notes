FROM ubuntu:20.04

ENV HOME /home/local/
WORKDIR /home/local/

# Flutter SDK
RUN apt update && apt upgrade -y \
    && apt install -y curl file git unzip xz-utils zip \
    && git clone https://github.com/flutter/flutter.git /usr/local/bin/flutter
ENV PATH /usr/local/bin/flutter/bin:$PATH

# ignores dialog
ENV DEBIAN_FRONTEND noninteractive

# Chrome (not necessary)
RUN apt install -y wget gnupg \
    # add package info (repository)
    && echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list \
    # download and register key
    && wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && apt update \
    && apt install -y google-chrome-stable

# Android toolchain (not necessary)
ENV ANDROID_HOME /usr/local/bin/android-sdk
ENV PATH /usr/local/bin/android-sdk/cmdline-tools/bin:$PATH
RUN mkdir -p $ANDROID_HOME && cd $ANDROID_HOME \
    # from https://developer.android.com/studio#command-tools
    && wget -O android-sdk-tools.zip https://dl.google.com/android/repository/commandlinetools-linux-9477386_latest.zip \
    && unzip android-sdk-tools.zip && rm android-sdk-tools.zip \
    && apt install -y default-jdk
RUN yes | sdkmanager --sdk_root=$ANDROID_HOME --licenses
RUN sdkmanager --sdk_root=$ANDROID_HOME "build-tools;33.0.0" "platform-tools" "platforms;android-33" "cmdline-tools;9.0"

# Linux toolchain
RUN apt install -y clang cmake ninja-build pkg-config libgtk-3-dev

# set back as default
ENV DEBIAN_FRONTEND newt
