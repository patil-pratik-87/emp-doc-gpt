---
type: page
title: Create Cloud Provider
listed: true
slug: cloud-provider
description: 
index_title: Create Cloud Provider
hidden: 
keywords: 
tags: 
---published

Before creating an instance of EMP, you must create a cloud provider by specifying your AWS account credentials. 

## Privileges Required

Here is a **summary** of the required privileges. 

1. ELB Management: Permissions to manage AWS Elastic Load Balancer (ELB).
2. Route 53 DNS Configuration: Access to configure DNS settings in Route 53.
3. Access to 2 or More Availability Zones: The credentials should have permission to interact with resources in at least two Availability Zones within the specified region.
4. EC2 Instance Management: Permission to manage EC2 instances, including creating, terminating, and modifying instances.
5. EBS Volume Management: Access to manage Elastic Block Storage (EBS) volumes for storage configurations associated with EMP.
6. VPC Management: Permission to configure and manage Virtual Private Clouds (VPCs).

## Create Cloud Provider Using 

Below are steps to download a Cloud Formation Template. This template creates a new user in your AWS environment with all the required IAM policies preconfigured.

The following steps describe the process to download and deploy the template to create a new IAM user with the required privileges. 

## Step 1: Download CloudFormation Template

Download the [EMP IAM CloudFormation Template](https://github.com/platform9/support-locker/blob/master/emp/emp_iam_cftemplate.yml) from Platform9's official GitHub repository:

$plugin[{
    "type": "code-block",
    "data": {
        "languageBlocks": [
            {
                "code": "export TEMPOUT=$(mktemp)\ncurl -fsSL https:\/\/raw.githubusercontent.com\/platform9\/support-locker\/master\/emp\/emp_iam_cftemplate.yml > $TEMPOUT",
                "language": "none"
            }
        ]
    }
}]$

## Step 2: Deploy CloudFormation Stack

Deploy the EMP IAM CloudFormation stack to create the new IAM user with the necessary policies:

$plugin[{
    "type": "code-block",
    "data": {
        "languageBlocks": [
            {
                "code": "aws cloudformation deploy --stack-name \"EMP-<org-id>\" --template-file \"${TEMPOUT}\" --capabilities CAPABILITY_NAMED_IAM",
                "language": "none"
            }
        ]
    }
}]$

You can change the name of the IAM user by providing `--parameter-overrides IAMUserName=<new-name>` to the deploy command. 

Note however that if you choose to override the IAM user name, the new name that you specify **must contain** either '_pf9"_ or '_platform9"_ as a substring. eg: _pf9-emp-john._

## Step 3: Retrieve AWS Credentials

### Newly Created User

If you created a new user using steps above, follow the steps below to retrieve the credentials. 

Retrieve your AWS secret and access keys for this newly created IAM user, using the following command. 

You can get the secret and access key from the output of this command. 

$plugin[{
    "type": "code-block",
    "data": {
        "languageBlocks": [
            {
                "code": "aws cloudformation describe-stacks --stack-name \"EMP-<org-id>\"",
                "language": "none"
            }
        ]
    }
}]$

### Existing User

For an existing AWS user, follow the [instructions on this page](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html#Using_CreateAccessKey)

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).
2. In the navigation pane, choose Users.
3. Choose the name of the intended user, and then choose the Security credentials tab. In the Access keys section, you will see the user's access keys and the status of each key displayed. Get the AWS Access Key ID, Secret Access Key from here. 

## Step 4: Create Cloud Provider

Use the obtained AWS Access Key ID, Secret Access Key to create a cloud provider using the EMP UI.

## Updating Existing CloudFormation Deployment

The EMP CloudFormation template may periodically be updated with a new set of permissions or other relevant changes. We recommend that you check the Platform9 github repository periodically and update your deployment to ensure that it reflects the latest changes.

To update an existing deployment, utilize the "aws cloudformation deploy" command with the following syntax:

$plugin[{
    "type": "code-block",
    "data": {
        "languageBlocks": [
            {
                "code": "aws cloudformation deploy --stack-name <stack-name> --template-file <template-file> --capabilities CAPABILITY_IAM",
                "language": "none"
            }
        ]
    }
}]$

Replace `<stack-name>` with the name of the stack you previously deployed and `<template-file>` with the path to the updated CloudFormation template file you have downloaded. If necessary, specify the IAM user using the `--parameter-overrides IAMUserName=<new-name>` option. This process ensures that the new configuration is applied to the specified stack and IAM user seamlessly.

