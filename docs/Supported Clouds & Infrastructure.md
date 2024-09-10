---
type: page
title: Supported Clouds & Infrastructure
listed: true
slug: supported-clouds-infra
description: 
index_title: Supported Clouds & Infrastructure
hidden: 
keywords: 
tags: 
---published

## Supported Clouds and Infrastructure

1. **Public cloud & Kubernetes service**: AWS and EKS. Support for other clouds coming in future.
2. **Networking**: AWS VPC CNI. No other CNI supported today.
3. **CPU Architecture**: x86 only. Support for Graviton coming soon. Support for GPUs coming in future.
4. **Load balancer**: [AWS NLB](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/introduction.html) or [AWS ALB](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html) load balancers with the target type "IP".
5. **EBS volume types**: All EBS volume types supported. Recommend using io1 / io2 volume types for best EVM live migration performance.

## Supported Software

#### Operating Systems

- EVMs Operating System version: Ubuntu 22.04.

#### Kubernetes Versions

- EKS cluster versions: **v1.27** to **v1.30**

## Supported Web Browsers

EMP User Interface supports following web browsers.

- Google Chrome
- Mozilla Firefox
- Safari

#### Screen Resolution

- For best performance, we recommend a screen resolution of 1440 x 900 or higher
- For screens with lower resolution, adjust browser zoom or display settings for best experience

