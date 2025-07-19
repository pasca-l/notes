# Docker Cheat Sheet <!-- omit in toc -->

## Table of Contents <!-- omit in toc -->
- [Installing Docker on Ubuntu](#installing-docker-on-ubuntu)
- [Using dind (docker-in-docker)](#using-dind-docker-in-docker)
- [Using dood (docker-outside-of-docker)](#using-dood-docker-outside-of-docker)

## Installing Docker on Ubuntu
There are several ways of installing Docker ([official installation methods of Docker](https://docs.docker.com/engine/install/ubuntu/#installation-methods)).

## Using dind (docker-in-docker)
Dind (docker-in-docker) is a method where the Docker Daemon is ran inside a container, allowing management of containers from the parent container.

1. Create a container with all the Docker packages.
```bash
# build an image with Docker installed
$ docker build -t custom-dind .

# run the container as priviledged
$ docker run --priviledged -it custom-dind
```

2. Start the Docker Daemon inside the container.
```bash
(container) $ dockerd &
```

3. Start any Docker container.
```bash
# eg. running test command
(container) $ docker run hello-world
```

## Using dood (docker-outside-of-docker)
Dood (docker-outside-of-docker) is a method where a container accesses the Docker Daemon on the host machine, allowing management of containers created on host level.

1. Create a container with the Docker CLI (not all Docker packages).
```bash
# build an image with Docker CLI (docker-ce-cli)
$ docker build -t custom-dood .
```

2. Run the container, bind mounting host's `/var/run/docker.sock`.
- the `docker` command will work for root users, otherwise the container user needs to be added to the `docker` group of the host machine.
```bash
$ docker run -v /var/run/docker.sock:/var/run/docker.sock -it custom-dood
```

3. Start any Docker container.
```bash
# eg. running test command
(container) $ docker run hello-world
```
