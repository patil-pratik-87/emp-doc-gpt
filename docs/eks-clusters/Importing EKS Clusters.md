---
type: page
title: Importing EKS Clusters
listed: true
slug: importing-eks-clusters
description: 
index_title: Importing EKS Clusters
hidden: 
keywords: 
tags: 
---published

EMP integrates with your new or existing AWS EKS clusters, enabling you to start incrementally adding new EVM nodes as worker nodes for your EKS cluster and then start migrating some or all of your workloads to the newly created EVM worker nodes. 

Note that importing EKS clusters into EMP **does not alter or restrict your access to any Kubernetes or EKS features**. You can continue using EBS volumes, VPC networking, CLI tools, and all other AWS ecosystem services as well as all Kubernetes commands without any modifications.

$plugin[{
    "type": "callout",
    "data": {
        "text": "importing EKS clusters into EMP **does not alter or restrict your access to any Kubernetes or EKS features**. You can continue to use all AWS ecosystem services along with your EKS clusters. You can also continue to use all Kubernetes features.",
        "type": "info",
        "title": "Info"
    }
}]$

1. **Compatibility with AWS EKS Clusters:** EMP is designed to work with any AWS EKS clusters that runs on x86 based infrastructure. EMP does not currently support AWS ARM-based Graviton instance types. Support for Graviton is coming in future. 

$plugin[{
    "type": "callout",
    "data": {
        "text": "EMP does not currently support AWS Graviton ARM-based instance types. Support for Graviton is coming in future. If you have more questions re this, contact [support@platform9.com](mailto:support@platform9.com)",
        "type": "warning",
        "title": "Important"
    }
}]$

1. **Multiple EKS Clusters per EMP:** You can associate multiple EKS clusters with a single instance of EMP. This approach is recommended as it enables you to achieve the best utilization across your EKS clusters in a given region.
2. **Region and Availability Zone support:** An instance of EMP is restricted to a single AWS region. If working with multiple AWS regions, you will need to create multiple EMP instances, at least one per region. Within a region, your EKS cluster may have worker nodes distributed across different Availability Zones (AZs) for high availability. EMP supports this scenario and enables you to select one or more Availability Zones when creating your bare metal pool. EMP bare metal pool will then create bare metal nodes across these AZs to ensure high availability for your workloads.

