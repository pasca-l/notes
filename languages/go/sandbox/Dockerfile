FROM golang:1.22

ENV HOME /home/local/
WORKDIR /home/local/app/src/

RUN apt-get update && apt-get upgrade -y

# project should be initialized with `go mod init`
# to create `go.mod` file, for installing dependencies, and etc.
COPY */go.mod */go.sum ./
RUN go mod tidy

# install air
RUN go install github.com/cosmtrek/air@latest
