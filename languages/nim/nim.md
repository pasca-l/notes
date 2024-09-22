# Nim Cheat Sheet [^document] <!-- omit in toc -->
[^document]: [Official document reference](https://nim-lang.org/documentation.html)

## Table of Contents <!-- omit in toc -->
- [Installing Nim](#installing-nim)
- [Running code](#running-code)

## Installing Nim
1. Install Nim (using Homebrew) [^installation].
```
$ brew install nim
```
[^installation]: [Installing Nim](https://nim-lang.org/install_unix.html)

## Running code
Compiling and then running executable file.
- `--run` flag executes the file automatically after compilation.
```bash
$ nim compile --run SCRIPT.nim
```

Otherwise, use the abbreviated version, for commonly used commands.
```bash
$ nim c -r SCRIPT.nim
```

> To compile a release version use `-d:release`.
> ```bash
> $ nim c -d:release SCRIPT.nim
> ```
