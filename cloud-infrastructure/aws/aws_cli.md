# AWS CLI Cheat Sheet [^userguide] [^document] <!-- omit in toc -->
[^userguide]: [Official user guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html)
[^document]: [Official document references](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html)

## Table of Contents <!-- omit in toc -->
- [Downloading and installing AWS CLI](#downloading-and-installing-aws-cli)
- [Configure AWS](#configure-aws)
- [Uploading files to Amazon S3](#uploading-files-to-amazon-s3)
- [Uploading AWS Lambda code](#uploading-aws-lambda-code)
- [Uploading AWS Lambda layer and attaching to AWS Lambda function](#uploading-aws-lambda-layer-and-attaching-to-aws-lambda-function)
- [Uploading Docker image to Amazon ECR](#uploading-docker-image-to-amazon-ecr)
- [Using on GitHub Actions](#using-on-github-actions)
  - [Login to Amazon ECR](#login-to-amazon-ecr)
  - [Deploy AWS CloudFormation stacks](#deploy-aws-cloudformation-stacks)

## Downloading and installing AWS CLI
- On Ubuntu
```bash
$ curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
$ unzip awscliv2.zip
$ sudo ./aws/install
```

- On macOS
```bash
$ curl "https://awscli.amazonaws.com/AWSCLIV2.pkg" -o "AWSCLIV2.pkg"
$ sudo installer -pkg AWSCLIV2.pkg -target /
```

## Configure AWS
- generate settings file using `aws configure`.

`~/.aws/config` and `/.aws/credentials` will be created.
```bash
$ aws configure
AWS Access Key ID [None]: IAM_ACCESS_KEY
AWS Secret Access Key [None]: IAM_SECRET_ACCESS_KEY
Default region name [None]: AWS_REGION
Default output format [None]: [json, yaml, text, ...]
```

## Uploading files to Amazon S3
1. Configure IAM role's policy. The given IAM role should be authorized to perform `CreateMultipartUpload` operation, with `s3:putObject` on target Amazon S3 bucket.

2. Upload file to target Amazon S3 bucket.
- To copy objects to a location, use `aws s3 cp`.
```bash
$ aws s3 cp FILES AMAZON_S3_URI
```
- To sync directories with a location, allowing removal of objects, use `aws s3 sync`.
```bash
$ aws s3 sync DIRECTORY AMAZON_S3_URI
```

## Uploading AWS Lambda code
1. Configure IAM role's policy. The given IAM role should be authorized to perform `lambda:UpdateFunctionCode` on target AWS Lambda function.

2. Upload code to target AWS Lambda function.

- For zip file, the artifact size, must be less than 250MB when expanded.
```bash
$ zip -r PACKAGE.zip TARGET_CODE_DIRECTORY
$ aws lambda update-function-code --function-name AWS_LAMBDA_FUNCTION --zip-file fileb://PACKAGE.zip --publish
```

- For docker image, refering Amazon ECR, AWS Lambda's function type must be set to `Image`.
```bash
$ aws lambda update-function-code --function-name AWS_LAMBDA_FUNCTION --image-uri AWS_ECR_URI
```

## Uploading AWS Lambda layer and attaching to AWS Lambda function
1. Upload zipped code file (library source files) from S3 bucket to target AWS Lambda function layer.

For every upload of layer, version number will be incremented. As of 2023/6/3, there is no support for `latest` tag for the newest version.
```bash
$ aws lambda publish-layer-version --layer-name LAYER_NAME --content S3Bucket=<S3_BUCKET_NAME>,S3Key=<S3_OBJECT_KEY>
```

2. Attach layer to AWS Lambda function.
```bash
$ aws lambda update-function-configuration --function-name AWS_LAMBDA_FUNCTION --layers <LAYER_ARN>:<LAYER_VERSION>
```

- Layer version can be obtained from `aws lambda list-layer-versions --layer-name LAYER_NAME --query 'LayerVersions[0].LayerVersionArn'`

## Uploading Docker image to Amazon ECR
1. Authenticate Docker client to Amazon ECR registry
```bash
$ aws ecr get-login-password --region AWS_REGION | docker login --username AWS --password-stdin <AWS_ACCOUNT_ID>.dkr.ecr.<AWS_REGION>.amazonaws.com
```

2. Push tag configured Docker image.
```bash
$ docker build -t ECR_REPOSITORY .
$ docker tag ECR_REPOSITORY:latest <AWS_ACCOUNT_ID>.dkr.ecr.<AWS_REGION>.amazonaws.com/<ECR_REPOSITORY>:latest
$ docker push <AWS_ACCOUNT_ID>.dkr.ecr.<AWS_REGION>.amazonaws.com/<ECR_REPOSITORY>:latest
```

## Using on [GitHub Actions](https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/configuring-openid-connect-in-amazon-web-services)
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

3. Add permission to token and use [official action](https://github.com/aws-actions/configure-aws-credentials).
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

### Login to Amazon ECR
0. Workflow must include steps on [Connecting with AWS](#connecting-with-aws).

1. Use [official action](https://github.com/aws-actions/amazon-ecr-login) to login to Amazon ECR.
```yaml
      - name: login to Amazon ECR
        uses: aws-actions/amazon-ecr-login@v1
        id: login-ecr   # id to refer information in later steps
```
> The role for carrying out this action should have the following policies:
> - `ecr:GetAuthorizationToken`

2. Push Docker image to Amazon ECR.
> The role for carrying out this action should have the following policies:
> - `ecr:BatchCheckLayerAvailability`
> - `ecr:CompleteLayerUpload`
> - `ecr:InitiateLayerUpload`
> - `ecr:PutImage`
> - `ecr:UploadLayerPart`

### Deploy AWS CloudFormation stacks
0. Workflow must include steps on [Connecting with AWS](#connecting-with-aws).

1. Use [official action](https://github.com/aws-actions/aws-cloudformation-github-deploy) to deploy AWS CloudFormation stack.
```yaml
      - name: deploy stack to AWS CloudFormation
        uses: aws-actions/aws-cloudformation-github-deploy@v1
        with:
          name: NAME
          template: FILE_PATH
          no-fail-on-empty-changeset: "1" # throw no error for no changes
```
