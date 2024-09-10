---
type: page
title: EMP Overview
listed: true
slug: what-is-emp
description: 
index_title: EMP Overview
hidden: 
keywords: 
tags: 
---published

Platform9 Elastic Machine Pool (EMP) is a Kubernetes cost optimization platform for public cloud native Kubernetes offerings. EMP helps you reclaim &gt; 70% of your wasted Kubernetes compute that may be sitting idle today, thus reducing your Kubernetes cluster costs by &gt; 70%. 

EMP supports AWS EKS Kubernetes service today. Support for GKE and AKS is coming in the future. 

## [Who Should Use This Documentation?](https://platform9.com/docs/kubernetes/about-pmk#who-is-this-documentation-for)

This documentation is intended for:

- Administrators and operators managing AWS EKS clusters
- DevOps teams seeking to optimize AWS and EKS cloud spend
- IT decision-makers evaluating cost saving solutions for AWS and Kubernetes

For a comprehensive understanding of EKS, please refer to the official [AWS EKS documentation](https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html).

## Key Differentiators of EMP

1. **Go beyond bin-packing.** EMP optimizes your Kubernetes utilization by reclaiming existing unused capacity in your cluster. This enables you to go much further beyond just the bin packing benefits, and actually optimize capacity that is allocated to your pods via request and limit values but not actually utilized. 
2. **Optimize without right-sizing**: Many existing tools try to optimize your Kubernetes resource consumption by modifying your pod's request and limit values. But since EMP can actually tap into existing unused capacity to deploy new workloads, EMP requires making no changes to your pod's request and limit values. 
3. **Rebalance with zero pod downtime**: When EMP needs to scale and add more capacity, or consolidate to better use existing capacity, it can 'live migrate' workloads around to do this. This means zero pod disruption and much higher availability for your stateful workloads. This is specially important for data services, AI/ML or large java web applications. 
4. **Continuous Optimization**: EMP automatically monitor and optimize VM deployments behind the scenes to maximize Kubernetes resource utilization.
5. **Seamless Scaling**: EMP handle usage spikes by scaling out underlying infrastructure and rebalancing workloads without application downtime.

## Key Features of EMP

#### 1. Resource Consolidation

- Utilizes proven virtualization and server consolidation techniques
- Optimizes workload placement on underlying EC2 infrastructure
- Significantly reduces wasted CPU and memory resources in EKS clusters

#### 2. Continuous Monitoring & Real-Time Scaling

- Constantly monitors resource usage across all applications in EKS clusters
- Identifies optimization opportunities in real-time
- Proactively scales resources up or down to maintain efficiency
- Employs live migration techniques to ensure application SLAs are met during adjustments

#### 3. Seamless Integration

- Integrates effortlessly with existing or new EKS clusters
- Requires no modifications to applications or cluster management processes
- Simple enablement process:
    - Enable EMP for your AWS account
    - Select desired EKS clusters
    - Optionally choose specific applications for EMP optimization

#### 4. Zero-Tuning Operations

- Operates autonomously once enabled
- Eliminates the need for manual tuning or configuration
- Saves DevOps teams significant time typically spent on cost-saving measures

## EMP vs Other Kubernetes Cost Management Tools

There are several monitoring and visibility tools available on the market that claim to provide significant cost savings for your Kubernetes environment. CloudHealth, Cloudability, and Datadog are great tools for understanding your cloud costs and identifying areas where you can save money. However, they do not specifically focus on automating the changes needed to increase your overall resource utilization.

Then there are tools such as open source Karpenter that make use of effective bin packing to allocate nodes just in time that fit your pod's resource requirements. However, these tools can not make a dent at optimizing your Kubernetes utilization if there is resource wastage due to high request and limit values. These tools will also involve a 'consolidation' phase where nodes are interrupted to consolidate fragmented pod deployments. This also requires pod restart which many stateful applications can not tolerate.

Then there are tools that make it easy to use spot instances with your EKS clusters to reduce your costs. However, spot instances are not a good fit for stateful applications that can not tolerate node interrupts, thus putting a ceiling on the amount of savings such tools can offer.

Lastly there are tools that makes adjustments to your application's request and limit values as a way to cut costs. But these tools will also require pod restart for the changes to take effect.

As a result, despite the use of these tools, Kubernetes utilization remains low, ranging between 15 and 30%. That means 70% or more of your k8s cloud resources are being completely wasted.

With EMP, there is no change to the request and limit values of your application necessary. Your developers will continue to set the requests and limits on the application pods that they desire, and EMP will work behind the scenes to optimize your EKS resource utilization based on demand.

EMP is complementary to your existing tools and can provide value on top of these technologies by maximizing utilization behind the scenes.

## EMP Benefits For Developers and DevOps

Application developers frequently define the resource requirements of their Kubernetes workloads based on peak CPU and memory requirements. However, real-world usage may frequently vary or be significantly lower than configured values for the majority of the time, necessitating ongoing adjustments to pod request and limit values by DevOps teams or Developers. EMP addresses this by deploying an alternate virtualization layer that monitors actual resource usage of your applications and dynamically allocates compute resources to meet the needs of your application, eliminating the need for manual configuration changes to your pod request and limit values.

Developers can continue to base their application’s request and limit values based on peak usage. At the same time, operations teams gain a powerful lever to rein in expenses.

