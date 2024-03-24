# Poetry Cheat Sheet [^document] <!-- omit in toc -->
[^document]: [Official document references](https://python-poetry.org/docs/)

## Table of Content <!-- omit in toc -->
- [Installing Poetry](#installing-poetry)
- [Installing dependencies](#installing-dependencies)
- [Configuring Poetry](#configuring-poetry)
- [List available packages](#list-available-packages)
- [Creating `pyproject.toml` file](#creating-pyprojecttoml-file)

## Installing Poetry
- With official installer
1. Download and install with python3.7 and above.
```bash
$ curl -sSL https://install.python-poetry.org | python3 -
```

2. Add Poetry to PATH, the wrapper is created at `$HOME/.local/bin` on Unix, or the binary file is at `~/.local/share/pypoetry/venv/bin/poetry` on Linux/Unix.
```bash
$ export PATH=$PATH:$HOME/.local/bin
```

3. Poetry is able to update itself when installed by the official installer.
```bash
$ poetry self update
```

- With [pipx](https://github.com/pypa/pipx)
0. Install pipx, on Linux.
```bash
$ python3 -m pip install --user pipx
$ python3 -m pipx ensurepath

# upgrade pipx
$ python3 -m pip install --user --upgrade pipx
```

1. Install using pipx.
```bash
$ pipx install poetry
```

2. Update Poetry.
```bash
$ pipx upgrade poetry
```

## Installing dependencies
- Resolves and installs dependencies from `pyproject.toml` from the project. If `poetry.lock` file present, exact dependency resolution will be used.
```bash
# with dependencies from group dev
$ poetry install --with dev
```

- Add package and installs it.
```bash
$ poetry add --group dev black
```

## Configuring Poetry
Configuration file `config.toml` will be automatically created after running `poetry config` command, under `~/.config/pypoetry` on Unix.

```bash
$ poetry config --list
```
```
cache-dir = "/path/to/cache/directory"
virtualenvs.create = true
virtualenvs.in-project = null
virtualenvs.options.always-copy = true
virtualenvs.options.no-pip = false
virtualenvs.options.no-setuptools = false
virtualenvs.options.system-site-packages = false
virtualenvs.path = "{cache-dir}/virtualenvs"
virtualenvs.prefer-active-python = false
virtualenvs.prompt = "{project_name}-py{python_version}"
```

- If `virtualenvs.create` is `false`, and detects no enabled or existing virtual environment in `{cache-dir}/virtualenvs` or `{project-dir}/.venv`, Poetry will install dependencies into the python environment of the system.
  - For Docker containers that require dependencies on the python environment of the image, virtual environment should not be created.

## List available packages
List all available packages, or pass the package name to show detail of a certain package.
```bash
$ poetry show --tree
```

## Creating `pyproject.toml` file
`pyproject.toml` should be prepared or created for the project.

```
[tool.poetry]
# required
name = "my-package"                  # valid PEP 508 name
version = "0.1.0"                    # valid PEP 440 string
description = "short description"
authors = [
    "Sébastien Eustace <sebastien@eustace.io>",
]

# optional
readme = "README.md"
license = "MIT"                      # identifiers at https://spdx.org/licenses/
homepage = "https://python-poetry.org/"
repository = "https://github.com/python-poetry/poetry"
documentation = "https://python-poetry.org/docs/"


[tool.poetry.dependencies]
python = "^3.7"                      # declaring python version is mandatory
requests = "^2.13.0"


# organizing dependencies in groups
[tool.poetry.group.dev.dependencies]
black = "*"
isort = "*"
pyproject-flake8 = "*"
mypy = "*"

[tool.poetry.group.test.dependencies]
pytest = "*"

[tool.poetry.group.docs.dependencies]
mkdocs = "*"


# scripts or executables
[tool.poetry.scripts]
my_package_cli = 'my_package.console:run'


# define alternative build systems according to PEP 517
# Poetry provides a lightweight core library
[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"
```
