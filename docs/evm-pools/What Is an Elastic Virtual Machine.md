---
type: page
title: What Is an Elastic Virtual Machine
listed: true
slug: what-is-evm
description: 
index_title: What Is EVM
hidden: 
keywords: 
tags: 
---published

Elastic Virtual Machines (EVMs) are a key component of EMP, offering flexible and efficient compute resources for your cloud workloads. 

EVMs are virtualised instances running on bare metal servers managed through EMP Bare Metal Pools. An EVM looks and feels exactly like a regular EC2 virtual machine, except that it's created by EMP on an AWS bare metal node.  These instances are designed to offer the performance benefits of dedicated physical servers while allowing for dynamic resource allocation and management. EVMs are at the heart of an EMP and will serve as worker nodes for your EKS clusters.

EVMs act as worker nodes for your Kubernetes cluster and are responsible for hosting your application pods. They provide the computational resources required to run containerised applications. EVMs are auto-scaled by EMP based on workload needs. 

## Benefits of EVMs

1. **Bridging Performance and Flexibility:** EVMs combine the performance advantages of bare metal servers with the flexibility of virtualization. An EVM looks and feels exactly like a regular EC2 virtual machine, except that it's created by EMP on an AWS bare metal node. This makes them suitable for all workload types, from high-performance computing to web applications.
2. **Zero-touch Lifecycle Management:** EMP handles complete lifecycle management of all your EVMs. This includes provisioning, scaling, monitoring, and maintenance, allowing DevOps teams to focus on their applications without worrying about infrastructure management.

