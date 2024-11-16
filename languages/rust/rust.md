# Rust Cheat Sheet [^document] <!-- omit in toc -->
[^document]: [Official document reference](https://doc.rust-lang.org/reference/index.html)

## Table of Contents <!-- omit in toc -->
- [Initializing project](#initializing-project)
- [Running code](#running-code)
- [Formatting code](#formatting-code)

## Initializing project
Creating a new Cargo package.
```bash
$ cargo new PROJECT_NAME
```

## Running code
Compiling and then running executable file.
```bash
# using Cargo (directly run after compile)
$ cargo run

# using `rustc` compiler
$ rustc SCRIPT.rs
$ ./EXEC_FILE
```

## Formatting code
Rust has a tool that formats source code, according to the [official style guide](https://doc.rust-lang.org/nightly/style-guide/).
1. Install formatting tool.
```bash
$ rustup component add rustfmt
```

2. Run on cargo project.
```bash
$ cargo fmt
```
