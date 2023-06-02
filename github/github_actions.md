# GitHub Actions Cheat Sheet [^document] <!-- omit in toc -->
[^document]: [Official document references](https://docs.github.com/en/actions)

## Table of Content <!-- omit in toc -->
- [Creating workflow](#creating-workflow)
- [Connecting with AWS](#connecting-with-aws)


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


## [Connecting with AWS](https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/configuring-openid-connect-in-amazon-web-services)
1. Add GitHub OIDC identity provider to IAM.
- Use `https://token.actions.githubusercontent.com` for provider URL.
- Use `sts.amazonaws.com` for audience.

2. Configure IAM role's trust policy.

Edit the trust policy for IAM role to be used.
```yaml
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Federated": "arn:aws:iam::<AWS_ACCOUND_ID>:oidc-provider/token.actions.githubusercontent.com"
            },
            "Action": "sts:AssumeRoleWithWebIdentity",
            "Condition": {
                "StringLike": {
                    "token.actions.githubusercontent.com:sub": "repo:<GITHUB_ORGANIZATION>/<GITHUB_REPOSITORY>:*"
                },
                "StringEquals": {
                    "token.actions.githubusercontent.com:aud": "sts.amazonaws.com"
                }
            }
        }
    ]
}
```

3. Add permission to token and use official action.
```yaml
jobs:
  aws:
    runs-on: ubuntu-latest

    # token permissions (can be written outside of jobs, if other jobs uses AWS as well)
    permissions:
      id-token: write
      contents: read

    steps:
      - name: setup python
        uses: actions/setup-python@v3
        with:
          python-version: "3.10"

      - name: configure AWS credentials
        uses: aws-actions/configure-aws-credentials@v2
        with:
          role-to-assume: arn:aws:iam::<AWS_ACCOUNT_ID>:role/<AWS_ROLE>
          aws-region: <AWS_REGION>

      - name: using AWS CLI commands
        run: |
          pip install awscli
          aws COMMAND
```
