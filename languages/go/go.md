# Go Cheat Sheet [^document] <!-- omit in toc -->
[^document]: [Official document reference](https://go.dev/doc/)

## Table of Contents <!-- omit in toc -->
- [Initializing project](#initializing-project)
- [Formatting code](#formatting-code)
- [Running code](#running-code)
- [Testing code](#testing-code)
- [Reference documentation](#reference-documentation)
- [Handling dependencies](#handling-dependencies)

## Initializing project
1. Choose a module path and create a `go.mod` file that declares it.
```bash
$ go mod init github.com/GITHUB_USERNAME/PROJECT_NAME
```

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

## Handling dependencies
1. Initialize `go mod`, which creates `go.mod` and `go.sum` files.
```bash
$ go mod init
```

2. Tidy up dependencies, adding missing files and deleting unnecessary files, according to the imports of the source files.
```bash
$ go mod tidy
```
> There are 2 modes, `GOPATH mode` or `module-aware mode`, in which the go command runs (as of Go 1.11, controlled with the `GO111MODULE` environment variable).
> 1. `GOPATH mode`, which the command looks into `vendor` directories and in `GOPATH` to find dependencies.
> 2. `module-aware mode`, which the command uses the `go.mod` file to find versioned dependencies (set to default, as of Go 1.16).
> 
> Use cases of similar go commands are as below:
> - `go get`, to edit `go.mod` file (as of Go 1.18, installation of executables is deprecated).
> - `go install`, to install executable.
>   - `go install module`, to read version requirements from `go.mod`.
>   - `go install module@version`, to install without altering `go.mod`.
> - `go mod tidy`, auto delete and addition of dependency.
