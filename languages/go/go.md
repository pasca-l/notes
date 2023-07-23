# Go Cheat Sheet [^document] <!-- omit in toc -->
[^document]: [Official document reference](https://go.dev/doc/)

## Table of Content <!-- omit in toc -->
- [Formatting code](#formatting-code)
- [Running code](#running-code)
- [Testing code](#testing-code)
- [Reference documentation](#reference-documentation)


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


## Testing code
1. Create a test file with a name ending with "_test.go". These files will be excluded from regular package builds.

2. Import `testing` package, a standard library, and write test functions.
```go
// if testing in the same package, unexported identifiers can be refered
package main
// for a separate testing package ("black box" testing), with a "_test" suffix, the package being tested must be imported explicitly
// eg. package main_test
//     import "path_to_pkg/main"

import "testing"

// testing functions should have the same form, where "Xxx" starts with uppercase
func TestXxx(t *testing.T) {
    if debug {
        t.Skip("skip test")
    }

    if condition {
        t.Errorf("error message")
    }
}
```

3. Run testing command.
```bash
$ go test
```

- To run all tests under the current directory, with verbose output.
```bash
$ go test -v ./...
```


## Reference documentation
Show documentation of packages, identifiers, or methods.
```bash
$ go doc PACKAGE.IDENTIFIER.METHOD
```
