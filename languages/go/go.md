# Go Cheat Sheet [^document] <!-- omit in toc -->
[^document]: [Official document reference](https://go.dev/doc/)

## Table of Content <!-- omit in toc -->
- [Formatting code](#formatting-code)
- [Running code](#running-code)


## Formatting code
Go contains a tool that automatically formats source code, according to the [official style guide](https://go.dev/doc/effective_go#formatting).
```bash
$ go fmt SCRIPT
```

- To format all source code under the project.
```bash
$ go fmt ./...
```

- To see the formatted result at the standard output. This is equivalent to `gofmt -l -w`.
```bash
$ gofmt SCRIPT
```


## Running code
Compiling and then running executable file.
```bash
$ go run SCRIPT

# if separating the two actions
$ go build EXEC_FILE SCRIPT
$ ./EXEC_FILE
```
