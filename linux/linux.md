# Linux Cheat Sheet <!-- omit in toc -->

## Table of Contents <!-- omit in toc -->
- [Creating a bootable USB stick](#creating-a-bootable-usb-stick)
- [Installing Ubuntu](#installing-ubuntu)
- [Permission settings](#permission-settings)
  - [Manage group member](#manage-group-member)
- [SSH server setup](#ssh-server-setup)
- [Alias settings](#alias-settings)

## Creating a bootable USB stick
- For any OS, download and use [balenaEtcher](https://www.balena.io/etcher).
- On Ubuntu, use "Startup Disk Creator", which is installed as default in Ubuntu.

## Installing Ubuntu
1. Download Ubuntu ISO file image from the [official website](https://ubuntu.com/download).
2. [Create bootable USB stick](#creating-a-bootable-usb-stick).
3. Insert USB stick into the desired PC and boot.

## Permission settings
### Manage group member
- Check groups, which the user is in.
```
$ whoami  # to find out username
$ cat /etc/group | grep USERNAME
```
- Adding or removing user from group
```
$ sudo gpasswd -a USERNAME GROUP  # to add
$ sudo gpasswd -d USERNAME GROUP  # to remove
```

## SSH server setup
1. Install OpenSSH.
```
$ sudo apt install openssh-server
```

2. Check service status.
- SSH service should be running active.
```
$ sudo systemctl status ssh
```
- Check for automatic start up. If `enabled`, the service starts with the server.
  - `sudo systemctl enable ssh` for enabling.
  - `sudo systemctl disable ssh` for disabling.
```
$ sudo systemctl is-enabled ssh
```

3. Check firewall.
- If `active`, firewall is enabled.
  - `sudo ufw enable` for enabling.
  - `sudo ufw disable` for disabling.
```
$ sudo ufw status
```
- Allow certain ports.
```
$ sudo ufw allow [portnum]
```

## Alias settings
1. Add the following setting for aliases, in any settings file such as `~/.zshrc`, `~/.bashrc`.
```sh
alias "ALIAS"="COMMAND"
```

2. Apply the change made.
```
$ source SETTINGS_FILE
```
