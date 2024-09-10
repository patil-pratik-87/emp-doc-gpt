---
type: page
title: What Are Bare Metal Pools
listed: true
slug: bare-metal-pools
description: 
index_title: What Are Bare Metal Pools
hidden: 
keywords: 
tags: 
---published

## What is Bare Metal

**Bare Metal** refers to physical servers or compute instances that are not virtualized. A typical Amazon EC2 instance is most often a virtual machine. However, EC2 does offer users the ability to provision bare metal EC2 instances that provide full access to the host hardware.

EMP leverages EC2 bare metal instances to derive best performance out of the provisioned compute hardware.

## What are Bare Metal Pools

A **Bare Metal Pool** within an EMP instance is a collection of one or more AWS bare metal servers. EMP uses these servers to create Elastic Virtual Machines (EVMs). These EVMs, in turn, serve as worker nodes for your EKS clusters. 

Bare Metal Pools are designed to provide the underlying physical infrastructure for your cloud-based workloads. They offer dedicated bare metal servers for your VMs, combining the advantages of physical hardware performance with the flexibility of cloud-based management.

