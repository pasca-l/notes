# Nim Cheat Sheet <!-- omit in toc -->

## Table of Contents <!-- omit in toc -->
- [References](#references)
- [Running code](#running-code)

## References
- [Official document reference](https://nim-lang.org/documentation.html)

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
