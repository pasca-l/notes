FROM debian:trixie

RUN apt update \
  # procps for `ps` command
  # libcap2-bin for `getpcaps` command
  && apt install -y sudo procps libcap2-bin \
  && rm -rf /var/lib/apt/lists/*

# create non-root user, and add to sudo group
RUN useradd -m nonroot \
  && usermod -aG sudo nonroot \
  && echo "nonroot ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/nonroot \
  && chmod 0440 /etc/sudoers.d/nonroot

USER nonroot

WORKDIR /home/nonroot
