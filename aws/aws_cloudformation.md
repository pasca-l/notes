# AWS CloudFormation Cheat Sheet [^userguide] [^document] <!-- omit in toc -->
[^userguide]: [Official user guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html)
[^document]: [Official document references](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html)

## Table of Content <!-- omit in toc -->
- [Recommended extensions for VSCode](#recommended-extensions-for-vscode)
- [Create template](#create-template)


## Recommended extensions for VSCode
- [`CloudFormation Linter`](https://github.com/aws-cloudformation/cfn-lint)
  - `cfn-lint` or `cfn-python-lint` from pip, required
  - `pydot` from pip, not required
- [`CloudFormation`](https://github.com/aws-scripting-guy/cform-VSCode)


## Create template
To create a stack for AWS CloudFormation, the template should be given as a JSON or YAML text file. The template must have the [`Resources`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html) top-level section.

```yaml
# Identify capabilities of the template
AWSTemplateFormatVersion: "2010-09-09"

# Comment about the template
Description: "Detail about the template."

Metadata:
  # eg. for using the CloudFormation console
  AWS::CloudFormation::Interface:
    # grouping parameters with heading
    ParameterGroups:
      - Label:
          default: "Parameter group name to show as header"
        Parameters:
          - <PARAM1>
    # parameter description
    ParameterLabels:
      - <PARAM1>: "Description for PARAM1 to show"

# Enable custom input values
# Use `Ref` intrinsic function to reference a parameter
Parameters:
  <PARAM1>:
    Description: "Description for PARAM1"
    Type: String
    Default: "default"

# Matches a key to a corresponding set of named values
# Use `FindInMap` intrinsic function, giving the list of names, eg. [map, key1, key2], to refer a specific value
Mappings:
  <MAP1>:
    <KEY1>:
      <NAME>: "value1"
    <KEY2>:
      <NAME>: "value2"

# Statements that define the circumstances by configuration
Conditions:
  # returns `true` when PARAM1 equals "default", with name LOGIC1
  <LOGIC1>: !Equals
    - !Ref <PARAM1>
    - "default"

# AWS resources to include in the stack
Resources:
  <RESOURCE1>:
    Type: "AWS::EC2::Instance"
    Properties:
      Tags:
        - Key: Name
          Value: "EC2-instance-name"
      ImageId: ---
      ...

# Output values for:
#   - importing into other stacks
#   - returning responses
#   - view on AWS CloudFormation console
Outputs:
  <OUTPUT1>:
    Value: "value to return, required"
    Description: "Description for OUTPUT1"
    Export:
      Name: !Sub "${AWS::StackName}-OUTPUT1"
```
