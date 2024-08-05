# Git command Cheat Sheet [^document] <!-- omit in toc -->
[^document]: [Official document references](https://git-scm.com/docs)

## Table of Contents <!-- omit in toc -->
- [Installing git command](#installing-git-command)
- [Change message after commit](#change-message-after-commit)
- [Applying `.gitignore` afterwards](#applying-gitignore-afterwards)
- [Change base branch](#change-base-branch)
- [Force local repository update](#force-local-repository-update)

## Installing git command
- On Ubuntu
```
$ apt-get install git
```

- Using Homebrew
```
$ brew install git
```

## Change message after commit
1. Changing commit message after a given commit.
```
$ git commit --amend -m "COMMENT"
```

## Applying `.gitignore` afterwards
1. Get certain file or directory out of repository.
```
$ git rm --cached (-r) FILE/(DIRECTORY)
```

2. Commit new file or directory, with the new `.gitignore` applied.
```
$ git add .
$ git commit -m "COMMENT"
```

## Change base branch
1. Having `BRANCH` with base branch `UPSTREAM`, changing `BRANCH` to work from `NEWBASE`.
```
$ git rebase --onto NEWBASE UPSTREAM BRANCH
```

## Force local repository update
1. Fetch latest version of remote repository.
```
$ git fetch origin BRANCH
```

2. Reset local `BRANCH` to latest remote `BRANCH`. Note that with `--hard`, commit history in worktree and index will be deleted on local.
```
$ git reset --hard origin/BRANCH
```
