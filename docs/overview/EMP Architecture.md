---
type: page
title: EMP Architecture
listed: true
slug: emp-architecture
description: 
index_title: EMP Architecture
hidden: 
keywords: 
tags: 
---published

This document describes the architecture and design of EMP, and how EMP seamlessly integrates with your new or existing AWS EKS environment and enables you to start deploying a portion of your workloads to EVM nodes. 

For a quick overview of EMP and the key benefits, refer to [auto$](/emp/what-is-emp)

For help on getting started with EMP, refer to [Getting Started With EMP](/emp/getting-started)

$plugin[{
    "type": "callout",
    "data": {
        "text": "This document assumes a basic familiarity with and understanding of Kubernetes as well as AWS's native Kubernetes offering (EKS). If you are new to Kubernetes and\/or AWS EKS, refer to [Kubernetes Documentation](https:\/\/kubernetes.io\/docs\/home\/) and [AWS EKS Documentation](https:\/\/aws.amazon.com\/eks\/) for more info.",
        "type": "info",
        "title": "Important"
    }
}]$

The following diagram provides a high level overview of EMP services.

$plugin[{
    "type": "image",
    "data": {
        "url": "https:\/\/uploads.developerhub.io\/prod\/ZGrW\/amc892h5fzqkwlqeithv9l1ug3n0iuz2d5s9axmflw0sxlz6jposqlbh1q2gtn1o.png",
        "mode": "responsive",
        "width": 1678,
        "height": 896,
        "caption": null
    }
}]$

EMP integrates easily with your AWS environment once deployed, and enables you to integrate with your new or existing EKS clusters. 

EMP has a few key services that gets deployed in your AWS environment upon successful creation of your first EMP instance.

1. **EMP Service -** This service is hosted by Platform9 and provides:
    1. Authentication and authorization.
    2. EMP UI

2. **EMP Admission Controller -** This component is deployed in each of your EKS Clusters once you associate them with an EMP instance. This component acts as a router to direct pods to be [provisioned onto the EMP Elastic VM nodes](/emp/provision-workloads-on-evms) instead of regular EC2 VM nodes. It works with an EMP Profile which provides rules to direct certain applications to EMP EVM nodes. This setup enables you to effectively test EMP by deploying some components of your application on EMP Elastic VM (EVM) nodes, while leaving rest of the components running on regular EC2 nodes.
3. **Bare metal EC2 nodes -** EMP deploys AWS bare metal EC2 instances behind the scenes. These nodes are then used to create Elastic VMs (EVMs) that in turn act as worker nodes for your EKS clusters. 
4. **Rebalancer -** EMP rebalancer is an EMP service that runs behind the scenes on the pool of bare metal machines that gets created for an instance of EMP. The rebalancer continuously monitors EVMs for CPU and Memory demand and utilization metrics. The rebalancer live migrates EVMs across the pool of bare metal machines to evenly distribute the resource demand across the pool of bare metal resources. 
5. **Custom CNI and CSI for EVMs**
    - **Custom CNI:** The EVMs in EMP leverage a custom CNI for networking, allowing them to efficiently communicate within EKS clusters. The custom CNI is designed to ensure required networking configurations suitable for the specific needs of Elastic VMs.
    - **Custom CSI:** EVMs also integrate with a [custom CSI](https://platform9.com/docs/emp-docs/emp/installing-custom-ebs-csi-driver), which manages the storage resources for the EVMs within the EKS ecosystem.

6. **EMP Cost Analyzer Helm Chart**
    - The EMP Cost Analyzer is an optional component that you have the choice to deploy on each of your EKS clusters. The helm chart works in conjunction with the "Cost Analyzer" component in the EMP UI. If deployed, the helm chart will supply the metrics data that will enable EMP Cost Analyzer to display potential cost savings for your environment when using EMP. The helm chart incorporates three components:
        - Prometheus: An open-source monitoring and alerting toolkit used for collecting and storing time-series data.
        - Node Exporter: A Prometheus exporter that gathers hardware and OS specific metrics from your EKS cluster nodes.
        - Kube State Metrics: Collects metrics about the state of the Kubernetes objects for your EKS cluster.

    - Once the helm chart is deployed, an EMP-specific pod aggregates data from Prometheus and periodically writes this information to a designated Platform9-owned S3 bucket.
    - The collected metrics include information about EKS cluster resource utilization, including details such as pod request and limit values for CPU and memory, and more.
    - EMP Cost Analyzer uses this information to present to you reports about potential cost savings with EMP within your AWS environment.

