# Zig Cheat Sheet <!-- omit in toc -->

## Table of Contents <!-- omit in toc -->
- [References](#references)
- [Formatting code](#formatting-code)
- [Running code](#running-code)
- [Testing code](#testing-code)
- [Generating document](#generating-document)

## References
- [Official document reference](https://ziglang.org/)

## Formatting code
Zig contains a tool that automatically formats source code, including re-encoding the file to UTF-8 as the Zig comipler does not support other encodings.
```bash
$ zig fmt SCRIPT.zig
```

## Running code
Compiling and then running executable file.
```bash
$ zig run SCRIPT.zig
```

## Testing code
Testing designating a test file.
```bash
$ zig test SCRIPT.zig
```

## Generating document
Zig compiler comes with automatic [document generation](https://zig.guide/build-system/generating-documentation), and can be invoked by adding `-femit-docs` option to the building (and running) commands.
```bash
$ zig run -femit-docs SCRIPT.zig
```
