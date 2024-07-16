# Haskell Cheat Sheet <!-- omit in toc -->

## Table of Contents <!-- omit in toc -->
- [Installing Haskell](#installing-haskell)
- [Using GHCi](#using-ghci)
- [Making a new project](#making-a-new-project)

## Installing Haskell
1. Install Stack (using Homebrew) [^installation].
```
$ brew install haskell-stack
```
[^installation]: [Installing Stack](https://docs.haskellstack.org/en/stable/install_and_upgrade/#using-homebrew)

## Using GHCi
- Call GHCi, to use an interpreter. Prompt should change to `Prelude`
```
$ stack ghci
Prelude>
```

- Load files either from the command line, or from the interpreter. When using `ghci` from command line, the file does not need to include `main` as for GHC.
```
$ stack ghci FILE
```
```
Prelude> :l(oad) FILE
```

- Exiting GHCi.
```
Prelude> :q
$
```

## Making a new project
1. Create new template project.
```
$ stack new PROJECT_NAME
```

2. Build project, within the project directory.
```
$ stack build
```

3. Execute project.
```
$ stack exec PROJECT_NAME-exe
```