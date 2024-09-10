---
type: page
title: VPC Peering
listed: true
slug: vpc-peering
description: 
index_title: VPC Peering
hidden: 
keywords: 
tags: 
---published

This document describes EMP VPC Peering feature, when it's required and how to configure it

## When To Enable VPC Peering

VPC peering is required if you choose to map more than one EKS clusters to a single EMP instance, and if they belong to different VPCs. 

If you are mapping only a single EKS cluster to an instance of EMP, or if you are mapping multiple EKS clusters that belong to the same VPC to a single instance of EMP, you do not need to enable VPC peering. 

$plugin[{
    "type": "callout",
    "data": {
        "text": "VPC peering is only required if you choose to map **more than one EKS clusters** to a single EMP instance, **and if they belong to different VPCs**.",
        "type": "warning",
        "title": "Important"
    }
}]$

## What is VPC Peering

VPC peering is an AWS construct that establishes a private network connection between two VPCs. This enables secure and direct communication between the two VPCs. Resources in peered VPCs can communicate with each other **as if they are within the same network**. You can create a VPC peering connection between your own VPCs, with a VPC in another AWS account, or with a VPC in a different AWS region, etc.

Please refer to [AWS VPC Peering](https://docs.aws.amazon.com/vpc/latest/peering/what-is-vpc-peering.html) documentation for an in depth understanding of VPC Peering.

EMP uses VPC peering to ensure secure and private network connectivity between the EKS clusters across different VPCs and the EMP bare metal nodes.

The bare metal pool is created in a standalone VPC and different EKS cluster VPCs are connected to the bare metal pool VPC using VPC peering.

$plugin[{
    "type": "callout",
    "data": {
        "text": "VPC peering must be turned on if you wish to map multiple EKS clusters to a single EMP instance.",
        "type": "info",
        "title": "Important"
    }
}]$

## Why Does EMP Use VPC Peering

VPC peering feature enables you to map multiple EKS clusters that belong to different VPCs, to the same EMP instance. 

This is valuable when you have multiple EKS clusters in your environment that are relatively small, so having individual EKS cluster mapped to a separate instance of EMP **may not provide the necessary cost** **savings** to you. 

However, if you map multiple EKS clusters within the same region to the same instance of EMP, then EMP can leverage the same underlying bare metal pool to host workloads across these clusters, resulting in **potentially better cost savings**. 

## Configure EMP VPC Peering

When creating a new instance of EMP, you have the option to utilize VPC peering for the network configuration of the bare metal pool for that EMP instance. 

### With VPC Peering Enabled

When VPC peering is enabled, your EKS clusters and the bare metal pool **must operate within separate VPCs.** In addition, the EKS cluster **IP address ranges (CIDRs) must not overlap with each other**. 

When creating a new instance of EMP, if you choose to enable VPC peering, then after you select one EKS cluster from your available EKS clusters list, the EMP creation wizard will filter out:

1. All other EKS clusters that have conflicting CIDRs with the selected EKS cluster's VPC

$plugin[{
    "type": "callout",
    "data": {
        "text": "When creating a new instance of EMP, if you choose to **enable VPC peering**, then after you select one EKS cluster from your available EKS clusters list, the EMP creation wizard will filter out:\n\n1. All other EKS clusters that have conflicting CIDRs with the selected EKS cluster's VPC",
        "type": "info",
        "title": "Important"
    }
}]$

### With VPC Peering Disabled

If you choose to disable VPC peering when creating a new instance of EMP, **your EKS clusters and the bare metal pool must use the same VPC**. 

In this case, in the EMP creation wizard, after you select one EKS cluster from your available EKS clusters list, the wizard will filter out:

1. All other EKS clusters that are NOT in the same VPC

In this scenario, when the bare metal pool gets provisioned, it will be created in the same VPC as that of your chosen EKS cluster(s) above. 

$plugin[{
    "type": "callout",
    "data": {
        "text": "When creating a new instance of EMP, if you choose to **disable VPC peering**, then after you select one EKS cluster from your available EKS clusters list, the EMP creation wizard will filter out:\n\n1. All other EKS clusters that are NOT in the same VPC as the selected cluster",
        "type": "info",
        "title": "Important"
    }
}]$

