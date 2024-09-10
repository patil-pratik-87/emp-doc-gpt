---
type: page
title: ALB for EMP
listed: true
slug: alb-for-emp
description: 
index_title: ALB for EMP
hidden: 
keywords: 
tags: 
---published

This guide will walk you through the steps to effectively use AWS Application Load Balancers(ALB) within your EMP environment.

### Installation

To install the [AWS Load Balancer Controller](https://docs.aws.amazon.com/eks/latest/userguide/aws-load-balancer-controller.html), responsible for managing ALBs, run the [ALB installation script](https://github.com/platform9/support-locker/blob/master/emp/nlb-alb-scripts/awslb-ctrl-install.sh). This controller ensures seamless integration between Kubernetes services and ALBs, providing reliable load balancing for your applications.

### Configuration

#### Subnet Tags

Before changing the service type, ensure that [specific tags are added to your public or private subnets](https://kubernetes-sigs.github.io/aws-load-balancer-controller/v2.2/deploy/subnet_discovery/). These tags allow the AWS Load Balancer Controller to discover the subnets and efficiently route traffic to your services.

For Public Subnets:

$plugin[{
    "type": "code-block",
    "data": {
        "languageBlocks": [
            {
                "code": "kubernetes.io\/cluster\/<cluster_name>: shared\nkubernetes.io\/role\/elb: 1",
                "language": "none"
            }
        ]
    }
}]$

For Private Subnets:

$plugin[{
    "type": "code-block",
    "data": {
        "languageBlocks": [
            {
                "code": "kubernetes.io\/cluster\/<cluster_name>: shared\nkubernetes.io\/role\/internal-elb: 1",
                "language": "none"
            }
        ]
    }
}]$

Replace &lt;cluster_name&gt; with the name of your EKS cluster. These tags are crucial for enabling smooth communication between the AWS Load Balancer Controller and your subnets.

#### Security Group Tags

Additionally, add a specific tag to the bare metal security group. This tag helps in the automatic registration and discovery of target groups for the EKS cluster.

$plugin[{
    "type": "code-block",
    "data": {
        "languageBlocks": [
            {
                "code": "kubernetes.io\/cluster\/<cluster_name>: shared",
                "language": "none"
            }
        ]
    }
}]$

#### Service Annotations

To expose a Kubernetes service using an ALB, you need to add specific AWS load balancer annotations to the service definition.

$plugin[{
    "type": "code-block",
    "data": {
        "languageBlocks": [
            {
                "code": "metadata:\n  annotations:\n    kubernetes.io\/ingress.class: alb\n    alb.ingress.kubernetes.io\/target-type: ip\n    alb.ingress.kubernetes.io\/scheme: internet-facing",
                "language": "none"
            }
        ]
    }
}]$

These annotations configure the ALB settings for the service, specifying its type, target type, and scheme.

### Usage

Once you create the service with the necessary annotations, an automatic load balancer endpoint is generated. It might take a few minutes for the associated pod to become registered as healthy in AWS Target Groups. Once registered, the ALB efficiently distributes incoming traffic across the available pods.

### Uninstallation

To uninstall the ALB and its components, simply run the [ALB rollback script](https://github.com/platform9/support-locker/blob/master/emp/nlb-alb-scripts/awslb-ctrl-rollback.sh). This script cleans up any resources created during the installation process, ensuring a smooth rollback procedure if needed.

