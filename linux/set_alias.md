# How to set alias

## Zsh
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

## Bash
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
