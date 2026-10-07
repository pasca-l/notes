# Haskell Cheat Sheet <!-- omit in toc -->

## Table of Contents <!-- omit in toc -->
- [References](#references)
- [Using GHCi](#using-ghci)

## References
- [Official document reference](https://www.haskell.org/documentation/)

## Using GHCi
- Call GHCi, to use an interpreter (prompt should change to `Prelude`).
```
$ ghci
Prelude>
```

- Load files either from the interpreter, or from the command line. When using `ghci` from command line, the file does not need to include `main` as for GHC.
```
Prelude> :l FILE
```

- Exiting GHCi.
```
Prelude> :q
```
