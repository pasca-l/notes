# AWS CloudFormation Cheat Sheet [^userguide] <!-- omit in toc -->
[^userguide]: [Official user guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html)

## Table of Content <!-- omit in toc -->
- [Recommended extensions for VSCode](#recommended-extensions-for-vscode)
- [Create template](#create-template)
- [Nesting Stacks](#nesting-stacks)
- [Referencing values](#referencing-values)


## Recommended extensions for VSCode
- [CloudFormation Linter](https://github.com/aws-cloudformation/cfn-lint)
  - `cfn-lint` or `cfn-python-lint` from pip, required
  - `pydot` from pip, not required
- [CloudFormation](https://github.com/aws-scripting-guy/cform-VSCode)


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


## Nesting Stacks
To create stacks with split file structure, [`AWS::CloudFormation::Stack`](https://docs.aws.amazon.com/ja_jp/AWSCloudFormation/latest/UserGuide/aws-properties-stack.html) can be used to nest a stack as a resource.
```yaml
AWSTemplateFormatVersion: "2010-09-09"
Description: "Nesting stacks with AWS::CloudFormation::Stack resource."

Resources:
  <RESOURCE1>:
    Type: AWS::CloudFormation::Stack
    # URL to stack YAML file in Amazon S3 bucket is required
    TemplateURL: https://<S3_BUCKET_NAME>.s3.<REGION_CODE>.amazonaws.com/TEMPLATE.yml
    # Parameters that are required by the target template
    Parameters:
      <PARAM1>: "default"

  <RESOURCE2>:
    Type: ...
    # Unnecessary if this resource contains !GetAtt for <RESOURCE1>
    # DependsOn: <RESOURCE1>
    Properties:
      Tags:
        - Key: Name
          # Referencing output values from an imported template
          Value: !GetAtt <RESOURCE1>.Outputs.<OUTPUT1>
```

- Because `Parameters` can only be a type of `List<String>`, template accepting parameters as lists needs to be string manipulated.
```yaml
# template defining nested stacks
Resources:
  <RESOURCE1>:
    Type: AWS::CloudFormation::Stack
    TemplateURL: ...
    Parameters:
      "PARAM1": !Join
        - ','
        - - <VALUE1>
```
```yaml
# stack that is imported
Parameters:
  <PARAM1>:
    Description: "Joined string for PARAM1"
    Type: String

Resources:
  <RESOURCE1>:
    Type: ...
    Properties:
      Tags: !Split [',', !Ref "<PARAM1>"]
```


## Referencing values
- If using short form `!Sub`, short form `!ImportValue` cannot be used in YAML.
```yaml
# no short form
Value: Fn::ImportValue
  'Fn::Sub': "${<PARAM>}-text"

# with short form
Value: Fn::ImportValue:
  !Sub "${<PARAM>}-text"
# or in one line
Value: {Fn::ImportValue: !Sub "${<PARAM>}-text"}
```

- If using short form `!Ref`, short form `!Join` cannot be used with `comma-delimited list of values` in YAML.
```yaml
# if joining values does not contain !Ref
Value: !Join [<DELIMITER>, [<VALUE1>, <VALUE2>, ...]]

# if joining values does contain !Ref
Value: !Join
  - <DELIMITER>
  - - <VALUE1>
    - !Ref <PARAM1>
    - !Ref <PARAM2>
    - ...
```
