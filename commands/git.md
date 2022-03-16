# Git command Cheat Sheet

## Change message after commit
Changing commit message after a given commit.
```
$ git commit --amend -m "COMMENT"
```


## Applying `.gitignore` afterwards
Get certain file or directory out of repository.
```
$ git rm --cached (-r) FILE/(DIRECTORY)
```

Then, commit new file or directory, with the new `.gitignore` applied.
```
$ git add .
$ git commit -m "COMMENT"
```


## Force local repository update (on `main` branch)
Fetch latest version of remote repository.
```
$ git fetch origin main
```

Then, reset local `main` to latest remote `main`. Note that with `--hard`, commit history in worktree and index will be deleted on local.
```
$ git reset --hard origin/main
```
