FROM node:20.11.0-bookworm-slim

ENV HOME /home/local/app/
WORKDIR /home/local/app/

# install necessary packages
RUN apt-get update && apt-get upgrade -y

# installing Watchman via Homebrew does not work (requires curl, git-all)
# RUN /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)" \
#     # add Homebrew to PATH
#     && (echo; echo 'eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"') >> /root/.bashrc \
#     && eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"
# RUN . /root/.bashrc && brew update && brew install gcc

# use of yarn, for "faster and more reliable dependency management"
RUN yarn add expo
# `yarn create expo-app APP_NAME`, to create new app
RUN yarn install
