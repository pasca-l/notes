# GitHub Actions Cheat Sheet [^document] <!-- omit in toc -->
[^document]: [Official document references](https://docs.github.com/en/actions)

## Table of Contents <!-- omit in toc -->
- [Creating workflow](#creating-workflow)
- [Using variables and context](#using-variables-and-context)
- [Triggering workflow manually](#triggering-workflow-manually)
- [Deploying built application onto GitHub Pages](#deploying-built-application-onto-github-pages)

## Creating workflow
> A workflow is a configurable automated process that will run one or more jobs.

Create a YAML file under `.github/workflows` directory under a repository.

```yaml
name: github actions workflow name

# trigger of workflow
on:
  push:
    branches:
      - main
      - develop

jobs:
  # job definition
  example:
    runs-on: ubuntu-latest
    steps:
      - name: checkout repository to runner
        uses: actions/checkout@v3

      - name: setup python
        uses: actions/setup-python@v3
        with:
          python-version: "3.10"

      - name: run main.py
        run: |
          echo "running main script"
          python main.py
```

## Using [variables](https://docs.github.com/en/actions/learn-github-actions/variables) and [context](https://docs.github.com/en/actions/learn-github-actions/contexts)
- Variables can only be accessed in the runner under the shell environment, expressed as `$VARIABLE`.
- Context can be refered as a context object's property, expressed as `${{ <context>.<property> }}`.

```yaml
jobs:
  example:
    runs-on: ubuntu-latest
    - if: ${{ runner.os }} == 'Linux'
      run: echo "Running $RUNNER_OS!"
```

## Triggering workflow manually
Use [`workflow_dispatch` trigger](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#workflow_dispatch), with custom inputs. Input values can be referenced from the `inputs.<name>` or `github.event.inputs.<name>` context property.
```yaml
on:
  workflow_dispatch:
    # optional custom inputs
    inputs:
      <name>:
        description: 'manual input for workflow'
        required: false
        type: [choice, boolean, environment, ...]
        # type 'choice' takes in options
        # options:
        #   - option1
        #   - option2
```

## Deploying built application onto GitHub Pages
1. Upload [artifacts](https://docs.github.com/en/actions/using-workflows/storing-workflow-data-as-artifacts) that can be deployed to GitHub Pages, using [official action](https://github.com/actions/upload-pages-artifact).
2. Deploy artifacts to GitHub Pages, using [official action](https://github.com/actions/deploy-pages).

```yaml
jobs:
  upload:
    runs-on: ubuntu-latest
    steps:
      - name: upload artifact (built application)
        uses: actions/upload-pages-artifact@v2
        with:
          path: "."

  deploy:
    # dependency to the 'upload' job, to use artifact
    needs: upload

    # permissions needed for GitHub Pages deployment
    permissions:
      pages: write
      id-token: write

    # deploy to an environment (eg. dev, prod)
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}

    runs-on: ubuntu-latest
    steps:
      - name: deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v2
        with:
          token: ${{ secrets.GITHUB_TOKEN }}
```
