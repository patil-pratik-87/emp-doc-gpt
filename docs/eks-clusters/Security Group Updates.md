---
type: page
title: Security Group Updates
listed: true
slug: eks-cluster-security-groups
description: 
index_title: Security Group Updates
hidden: 
keywords: 
tags: 
---published

This guide outlines configuring security groups for your EKS clusters when integrating them with an EMP instance. Proper security group configuration enables communication between EKS clusters and EMP EVM nodes.

## Prerequisites

- Familiarity with [EKS security group requirements and considerations](https://docs.aws.amazon.com/eks/latest/userguide/sec-group-reqs.html)
- Access to AWS Console or AWS CLI
- Permission to modify security groups

## Security Groups Overview

### EKS Security Groups

When creating an EKS cluster in AWS, the following security groups are typically created:

1. EKS control plane security group
2. EKS worker node group security group(s)

Additional security groups may be created by your administrator based on your organization's specific security policies.

### EMP Security Groups

Upon creation of a bare metal pool within an EMP instance, a new security group specific to that pool is automatically gets created.

### Enabling Traffic Between EMP and EKS

To ensure proper communication between EMP and EKS, two key steps are required:

1. Update EKS Control Plane Security Group:
    1. Add a rule to allow ALL inbound traffic from the EMP bare metal pool security group.
    2. This enables communication between the EKS control plane and EVM nodes.

2. Update EMP Bare Metal Pool Security Group:
    1. Add rules corresponding to existing node groups of your EKS cluster.
    2. This enables communication between workloads on EVM nodes and non-EVM nodes of the cluster.

The following diagram highlights two main points: 

1. **Inbound Rule Addition**: An inbound security group rule needs to be added to the EKS control plane security group(s) to allow all traffic between the EKS control plane and the EVM nodes in the EMP.
2. **Security Group Selection**: During EMP creation, you select the security groups for the EKS node groups. EMP then adds rules to the bare metal pool security group to allow traffic between the EKS node groups and the EVM nodes.

$plugin[{
    "type": "image",
    "data": {
        "url": "https:\/\/uploads.developerhub.io\/prod\/ZGrW\/gbaldils1al4aotnjphwmsqoqlayjnkh2ayxa8lg3emwbw13ehds3us8934uzugd.png",
        "mode": "full",
        "width": 963,
        "height": 511,
        "caption": null
    }
}]$

Depending on your preference and specific security requirements, the process can be automated through the EMP creation wizard or done manually.

$plugin[{
    "type": "callout",
    "data": {
        "text": "An in depth understanding of what communication must be enabled between your EKS clusters and EMP EVM nodes is crucial for a successful EMP setup. \n\nWhile EMP creation wizard automates the whole process for you, **your organization may have specifically configured security policies that require update outside of what the EMP creation wizard does**. \n\nWe therefore recommend that you read this document carefully and **work with your network administrator** to update any additional required security policies.",
        "type": "info",
        "title": "Important"
    }
}]$

### Configuration Options

#### Option 1: Automated Configuration (Recommended)

The EMP creation wizard can automate the entire process, updating all required security groups on your behalf.

#### Option 2: Manual Configuration

If you prefer to make changes manually or need to accommodate specific organizational security policies, follow these steps:

1. When creating the EMP instance, select the option "_I will make the changes to the required security groups on my own_". 
2. After completing EMP creation wizard, navigate to the EMP grid view in the UI.
3. Click on the EMP instance name in the EMP UI to navigate to the EMP instance you just created. 
4. On this page, verify that the bare metal pool for this EMP has been created, by looking at the "Overall Status" value. 
5. If the "Overall Status" says "Bare Metal Pool Provisioning", then your bare metal pool is still getting created, and the security group ID may not have been populated yet. Wait for the bare metal pool to be provisioned. _This may take up to_ _**30 minutes**__._ 
6. Once the bare metal pool is created, click on the "Bare Metal Pool" tab. 
7. On this tab, under the "Networking" section, you will find the security group ID for this bare metal pool.
8. You will now need to modify the EKS control plane security group for ALL EKS clusters that you are associating with this bare metal pool, to add a NEW security group rule to _allow ALL inbound traffic from this security group ID._ 

## Selecting EKS Worker Node Security Groups for EMP

During the EMP creation process, you'll need to specify which EKS worker node security groups should be associated with your EMP instance.

#### Process:

1. In the EMP creation wizard, you will be asked to select worker node security groups.
2. Choose the security groups corresponding to the EKS clusters you intend to associate with this EMP instance.
3. After selection, EMP automatically handles the following:
    1. Adds rules to the bare metal pool security groups
    2. Configures traffic between non-EVM worker security groups (your existing EKS nodes) and EVM nodes of the cluster (managed by EMP)

## Best Practices:

- Review your EKS cluster configuration before starting the EMP creation process to identify all relevant security groups.
- If you're unsure which security groups to select, consult with your cloud infrastructure team or EKS cluster administrator.
- Document which security groups you've selected for future reference and troubleshooting.

