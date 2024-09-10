---
type: page
title: Getting Started
listed: true
slug: getting-started
description: 
index_title: Getting Started
hidden: 
keywords: 
tags: 
---published

This document describes the steps to start optimizing your first EKS cluster using an Elastic Machine Pool (EMP).

## You will need:

- Follow [auto$](/emp/iam-prereqs) to configure the IAM user role to operate with EMP.
- 1 AWS Key Pair: Pre-create at least one AWS key pair. This will be used to inject in each bare metal instance and can be used for access and debugging.
- 1 Public Key: Specify a public key during EVM pool creation. This key will be injected into each EVM instance and can be used for access and debugging. 

## Step 1 - Specify Cloud Credentials

A 'Cloud Provider' enables you to specify cloud credentials of the AWS IAM user account you want to use to provision an instance of EMP. 

Follow [Create Cloud Provider](/emp/cloud-provider) for steps to create your first cloud provider.

## Step 2 - Create an EMP Instance

Log into the EMP UI and follow the "Create EMP" wizard to create your first instance of EMP.

- Select your cloud credentials you specified above, then select the AWS region where your EKS cluster currently resides 
- Select the EKS cluster you wish to optimize from the list of EKS clusters.
- Select the security group configuration options to enable communication between EKS control plane and EMP created worker nodes (EVMs) and between EVM and non EVM nodes. Refer to [auto$](/emp/eks-cluster-security-groups) for more info.
- Select the AWS EC2 bare metal instance type to create a new bare metal pool. The instance type should be from the same instance family as the EC2 instances you use for your EKS cluster today. For eg, if you use r5.8xlarge instances for EC2 workers, choose r5.metal instance  Read [auto$](/emp/bare-metal-pool-configuration) for options to configure.
- For VPC configuration, select an existing VPC that your EKS cluster is part of. Read [auto$](/emp/bare-metal-pool-vpc-config) for an in depth understanding of the options available here.
- **Create EVM Pool**: An EVM pool is like a node group. Create one EVM pool for your EKS cluster. Choose the same EC2 instance type you use for your EKS cluster today. See [Configuration Options for EVM Pool Creation](/emp/elastic-virtual-machine-pools#configuration-options-for-evm-pool-creation) for more details. 
- Finalize and create the EMP instance.

Creating the EMP instance **may take up to** **30 minutes**. You can monitor the status of the EMP instance from the 'Overview' screen in the EMP UI. Once created, EMP instance status will change to **Ready**.

You can now see the EVM worker nodes in your AWS EKS dashboard alongside your regular EC2 worker nodes. You can also see the AWS bare metal instances provisioned in your EC2 dashboard.

## Step 3 - Provision First Workloads on EVMs

- If you are using EBS volumes for pods, you may need to configure the EBS CSI driver. Follow the [auto$](/emp/emp-ebs-csi-config) for instructions.
- Refer to [auto$](/emp/provision-workloads-on-evms) for steps to do add tolerations to your existing pods to enable them to run on the EVM nodes.

