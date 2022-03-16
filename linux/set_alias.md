# How to set alias

## Zsh
Aliases put in `~/.zshrc`.
```sh
alias "ALIAS"="COMMAND"
```

To apply change:
1. Restart zsh.
2. Reflect settings by command.
```
$ source ~/.zshrc
```

## Bash
Aliases put in `~/.bashrc`.
```sh
alias "ALIAS"="COMMAND"
```

To apply change:
1. Restart bash, under condition of changes loaded by `~/.bash_profile`.
```sh
source ~/.bashrc
```
2. Reflect settings by command.
```
$ source ~/.bashrc
```
