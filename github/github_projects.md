# GitHub Projects Cheat Sheet [^document] <!-- omit in toc -->

## Table of Contents <!-- omit in toc -->
- [Automating Projects](#automating-projects)
  - [Automatically add issues on Projects](#automatically-add-issues-on-projects)

## Automating Projects
### Automatically add issues on Projects
```yaml
name: add issues to project
on:
  issues:
    types:
      - opened
      - reopened

jobs:
  add_item:
    runs-on: ubuntu-latest
    steps:

      - name: set environment variables
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          ORGANIZATION: 
```
