FROM golang:1.22

ENV HOME /home/local/
WORKDIR /home/local/src/

RUN apt-get update && apt-get upgrade -y

# project should be initialized with `go mod init`
# to create `go.mod` file, for installing dependencies, and etc.

# install air
ENV GOPATH /usr/local/go
RUN go install github.com/cosmtrek/air@latest
COPY *go.mod *go.sum ./
