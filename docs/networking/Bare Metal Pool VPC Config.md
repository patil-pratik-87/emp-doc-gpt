---
type: page
title: Bare Metal Pool VPC Config
listed: true
slug: bare-metal-pool-vpc-config
description: 
index_title: Bare Metal Pool VPC Config
hidden: 
keywords: 
tags: 
---published

## VPC requirements for multi-cluster EMP setup

#### Single VPC Scenario

When importing multiple EKS clusters into an instance of EMP with VPC peering is disabled, all EKS clusters associated with EMP must reside within the same VPC.

#### Multiple VPC Scenario

When importing multiple EKS clusters with distinct VPCs into a single EMP instance:

1. EKS clusters and the EMP bare metal pool **must operate within separate VPCs**.
2. The IP address ranges (CIDRs) of EKS clusters **must not overlap** with each other or with the bare metal pool VPC CIDR.
3. When VPC Peering is enabled, the cert-manager will not work for an EKS cluster with only EVMs as worker nodes. `cert-manager` needs to be scheduled on EC2-managed nodes.

## VPC config options when creating a bare metal pool

When creating your EMP bare metal pool, EMP provides following options for VPC configuration:

#### Select from an existing VPC

You have the option to select from your existing list of VPCs when VPC peering is enabled. If VPC peering is disabled, the VPC of the EKS cluster you selected in the previous step will be pre-selected for you and you do not have the ability to change that configuration. 

Note that if VPC peering is disabled, then **the EKS clusters you select to map to the bare metal pool must all share the same VPC**. 

$plugin[{
    "type": "callout",
    "data": {
        "text": "If VPC peering is disabled, the EKS clusters you choose to associate with a given instance of EMP **must all share the same VPC**.",
        "type": "warning",
        "title": "Important"
    }
}]$

### Subnet Configuration

For each availability zone where you plan to deploy bare metal instances, you need:

1. One public subnet: **Required**: 
2. One private subnet: Optional but **Highly Recommended**: 

Ensure your VPC meets these subnet requirements for each intended AZ before deploying the EMP instance.

Public Subnet

The **public subnet** is required and is used to deploy a NAT Gateway that the bare metal pool uses to download required packages. 

If no private subnet is specified, the **public subnet will also be used to deploy the bare metal pool nodes**. 

You should only choose to deploy your bare metal nodes in public subnet if:

1. The EKS cluster(s) you are mapping to your EMP instance use public subnet to deploy worker nodes today
2. You are creating a POC / test EMP setup and would like to deploy bare metal nodes in public subnet for ease of debugging 

If using the public subnet to also deploy your bare metal nodes:

1. Make sure that the subnet is configured with "Auto-assign public IPv4 address” set to “yes” on AWS side, to ensure that the bare metal nodes get assigned a public IP address. 
2. If the EKS cluster you are mapping to the EMP instance has it's non-EMP worker nodes deployed in a private subnet, make sure that there is connectivity between the private and public subnets. 

$plugin[{
    "type": "callout",
    "data": {
        "text": "If you are using the public subnet to deploy your bare metal nodes, ensure the subnet is configured with \"**Auto-assign public IPv4 address\"** set to \u201c**yes**\u201d on the AWS side to ensure that the bare metal nodes are assigned a public IP address.",
        "type": "warning",
        "title": "Important"
    }
}]$

#### Private Subnet

The **private subnet** is optional but **highly recommended** for **production** use cases. If you specify a private subnet, the bare metal nodes in your pool will be deployed in the private subnet. If not specified, all bare metal nodes will be deployed in the public subnet.

