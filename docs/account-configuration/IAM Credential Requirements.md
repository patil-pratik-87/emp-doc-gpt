---
type: page
title: IAM Credential Requirements
listed: true
slug: iam-prereqs
description: 
index_title: IAM Credential Requirements
hidden: 
keywords: 
tags: 
---published

This document provides the steps to configure required IAM credentials for the user role that you will use to create the EMP cloud provider. 

## Create New IAM User For EMP

We highly recommend that you create **a new IAM user** that you will then use for creating an EMP cloud provider. Follow the steps below to create the user:

### Step 1: Check Your IAM Policy Quotas

Running the EMP IAM User Cloud Formation Template will attempt to create a few additional 'Customer managed policies' for the newly created IAM user. Ensure that any **policy quota** **limit** set on your AWS account will allow this. [Read more here](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-quotas.html#reference_iam-quotas-entities) about **default and maximum quotas** for the customer managed policies per account.

### Step 2: Run EMP IAM CloudFormation Template

Run the EMP [IAM User Configuration CloudFormation Template](https://github.com/platform9/support-locker/blob/master/emp/emp_iam_cftemplate.yml)  in your AWS environment. This will create a new IAM user. The output of the template will specify the AWS Access key and Secret access key that you can then use to create the EMP cloud provider. 

## Use An Existing IAM User

### Pre-requisites

Following requirements must be met if you choose to use existing IAM user credentials for EMP.

1. The AWS account credentials must be configured to have required privileges. This [policy json file](https://github.com/platform9/support-locker/tree/master/emp/emp-aws-policies) lists the privileges required.
2. Make sure that the AWS credentials you provide are [long term credentials](https://docs.aws.amazon.com/sdkref/latest/guide/access-iam-users.html) .
3. The AWS user that you plan to use with EMP **must have access to all the EKS clusters that you plan to associate with your EMP instance**. If this AWS user did not create the EKS clusters then you may need to grant access to the EKS clusters to them by [enabling IAM access](https://docs.aws.amazon.com/eks/latest/userguide/add-user-role.html) .
4. **IMPORTANT** - You will need to either edit your existing IAM users username to add either “**pf9**” or “**platform9**" as a prefix, or add that prefix while referring to the user in the `aws-auth` config map. For instance, if your IAM username is **john-deo**, it will look like **pf9-john-deo** or **platform9-john-deo** when referred in aws-auth config map as shown in below example.

$plugin[{
    "type": "callout",
    "data": {
        "text": "If the IAM username for your AWS user does not already contain the \"pf9\" or \"platform9\" prefix, you must add that prefix while referring to the username in the ConfigMap. \n\nFor instance, if your current IAM user's username is john-deo, change it to the following when referring to it in the configmap  **pf9-john-deo** or **platform9-john-deo.**\n\nNot doing this will result in authentication error while creating an EMP.",
        "type": "warning",
        "title": "Important"
    }
}]$

### Provide Existing User Access To The EKS Cluster

Follow the steps below to provide AWS user that you plan to use with EMP access to the EKS clusters that you plan to import into EMP. 

You can either use eksctl or directly edit the configmap for each EKS cluster to do this step. 

#### Use eksctl

Run the following command using eksctl for each EKS cluster that you wish to grant access. 

If the IAM username for your AWS user does not already contain the "pf9" or "platform9" prefix, add that prefix while referring to the username in the ConfigMap here.

For instance, if your current IAM user's username is john-deo, change it to the following when referring to it in the configmap: **pf9-john-deo** or **platform9-john-deo.**

$plugin[{
    "type": "code-block",
    "data": {
        "languageBlocks": [
            {
                "code": "$ eksctl create iamidentitymapping --cluster <cluster-name> --region <region> --arn <emp-user-ARN> --username <emp-user-name> --group system:masters --no-duplicate-arns",
                "language": "json"
            }
        ]
    }
}]$

Example command when your IAM username is "john-deo"

$plugin[{
    "type": "code-block",
    "data": {
        "languageBlocks": [
            {
                "code": "$ eksctl create iamidentitymapping --cluster <cluster-name> --region <region> --arn arn:aws:iam::555555555555:user\/platform9-john-deo --username platform9-john-deo --group system:masters --no-duplicate-arns",
                "language": "json"
            }
        ]
    }
}]$

#### Directly Edit AWS-Auth ConfigMap

Perform the steps below **for each cluster** you want to add to your EMP instance.

You need to edit the `aws-auth` ConfigMap for the EKS cluster under the `kube-system` namespace. This ConfigMap contains user mappings for authenticating users with the EKS cluster. 

Use the following command to edit the configmap. 

$plugin[{
    "type": "code-block",
    "data": {
        "languageBlocks": [
            {
                "code": "# kubectl edit -n kube-system configmap\/aws-auth",
                "language": "json"
            }
        ]
    }
}]$

This is what your ConfigMap may look like before you make the edits:

$plugin[{
    "type": "code-block",
    "data": {
        "languageBlocks": [
            {
                "code": "# Please edit the object below. Lines beginning with a '#' will be ignored,\n# and an empty file will abort the edit. If an error occurs while saving this file will be\n# reopened with the relevant failures.\n#\napiVersion: v1\ndata:\n  mapRoles: |\n    - groups:\n      - system:bootstrappers\n      - system:nodes\n      rolearn: arn:aws:iam::555555555555:role\/myAmazonEKSNodeRole\n      username: system:node:{{EC2PrivateDNSName}}\nkind: ConfigMap\nmetadata:\n  creationTimestamp: \"2024-04-12T15:42:39Z\"\n  name: aws-auth\n  namespace: kube-system\n  resourceVersion: \"1289\"\n  uid: 9640433b-1f75-4256-8a78-16a0be491dd4",
                "language": "json"
            }
        ]
    }
}]$

Add or append the "mapUsers" section in this ConfigMap. Replace `<Your_EMP_User_ARN>` with your AWS EMP user ARN and `<Your_EMP_Username>` with your desired username for the EMP user. 

If the IAM username for your AWS user does not already contain the "pf9" or "platform9" prefix, add that prefix while referring to the username in the ConfigMap here. 

For instance, if your current IAM user's username is john-deo, change it to the following when referring to it in the configmap:  **pf9-john-deo** or **platform9-john-deo.**

$plugin[{
    "type": "code-block",
    "data": {
        "languageBlocks": [
            {
                "code": "# Please edit the object below. Lines beginning with a '#' will be ignored,\n# and an empty file will abort the edit. If an error occurs while saving this file will be\n# reopened with the relevant failures.\n#\napiVersion: v1\ndata:\n  mapRoles: |\n    - groups:\n      - system:bootstrappers\n      - system:nodes\n      rolearn: arn:aws:iam::1234567898:role\/myAmazonEKSNodeRole\n      username: system:node:{{EC2PrivateDNSName}}\n\tmapUsers: |\n    - userarn: <Your_EMP_User_ARN>\n      username: <Your_EMP_Username>\n      groups:\n      - system:masters\nkind: ConfigMap\nmetadata:\n  creationTimestamp: \"2024-04-12T15:42:39Z\"\n  name: aws-auth\n  namespace: kube-system\n  resourceVersion: \"1289\"\n  uid: 9640433b-1f75-4256-8a78-16a0be491dd4",
                "language": "json"
            }
        ]
    }
}]$

These mappings allow the specified users to authenticate with the EKS cluster and be assigned the permissions associated with their respective groups.

## Validate User Credentials

You can run the following steps to validate the IAM credentials of the user you would like to use with EMP:

1. Use the AWS access key and secret access key corresponding to your IAM user to configure the credentials for AWS CLI in the ~/.aws/credentials file. 
2. Use the AWS CLI to download the `kubeconfig` of the EKS cluster being associated with EMP.
3. Use `kubectl` along with the `kubeconfig` to try to access following Kubernetes resources: secrets, pods, configmaps, clusterrolebindings, clusterrole, serviceaccount, daemonset, deployments, service and mutatingwebhookconfiguration in the `kube-system` namespace. 

If you are unable to access any of the resources above, your IAM credentials may not be configured correctly.

