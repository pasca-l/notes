# Linux Setting Cheat Sheet <!-- omit in toc -->

## Table of content <!-- omit in toc -->
- [Alias settings](#alias-settings)
  - [On zsh](#on-zsh)
  - [On bash](#on-bash)


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
