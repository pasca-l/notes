# Linux Setting Cheat Sheet <!-- omit in toc -->

## Table of content <!-- omit in toc -->
- [Permission settings](#permission-settings)
  - [Manage group member](#manage-group-member)
- [SSH server setup](#ssh-server-setup)
- [Alias settings](#alias-settings)
  - [On zsh](#on-zsh)
  - [On bash](#on-bash)


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

1. Check firewall.
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
### On zsh
Aliases put in `~/.zshrc`.
```sh
alias "ALIAS"="COMMAND"
```

To apply change:
- Restart zsh.
- Reflect settings by command.
```
$ source ~/.zshrc
```

### On bash
Aliases put in `~/.bashrc`.
```sh
alias "ALIAS"="COMMAND"
```

To apply change:
- Restart bash, under condition of changes loaded by `~/.bash_profile`.
- Reflect settings by command.
```
$ source ~/.bashrc
```
