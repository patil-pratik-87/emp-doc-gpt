---
type: page
title: Cost Analyzer
listed: true
slug: emp-cost-analyzer
description: 
index_title: Cost Analyzer
hidden: 
keywords: 
tags: 
---published

The EMP Cost Analyzer is designed to provide visibility into the potential savings EMP could provide for your AWS EKS environment.

You can install it as a Helm chart on each of your EKS clusters. Once installed, it collects metrics about your cluster's CPU and memory utilization, pod request and limit configuration, and other related metrics to project potential savings when used with EMP. 

## Components

The EMP Cost Analyzer involves two components:

1. **The Cost Analyzer UI** - This is part of EMP UI. It provides detailed visibility into cost savings for one or more EKS clusters within your AWS environment.
2. **The Cost Analyzer Helm Chart** - You can download the Helm chart from the EMP Cost Analyzer UI and install it on each of your EKS clusters to gain visibility into potential cost savings with EMP.

## Pre-requisites

Before installing the EMP Cost Analyzer Helm Chart on your EKS cluster, ensure the following prerequisites:

- Kubectl installed & configured to operate with the EKS cluster 
- [Helm CLI client installed](https://helm.sh/docs/intro/install/) (version 3.12 or higher)
- Outbound network connectivity

$plugin[{
    "type": "callout",
    "data": {
        "text": "_If the Cost Analyzer Helm chart is installed before or after adding a cluster to EMP, the installation will succeed, but the metrics won't be used in cost recommendations. As a result, you won't see recommendations for these clusters in the Cost Analyzer UI._",
        "type": "warning",
        "title": "Warning"
    }
}]$

## Installation

Once you login, you are now ready to install the EMP Cost Analyzer Helm chart.

1. Log into the EMP UI, navigate to the "Cost Analyzer" left side menu.
2. Click on the "Install" tab.  Here you will find the instructions to download the Cost Analyzer helm chart. 

execute the following command:

$plugin[{
    "type": "code-block",
    "data": {
        "languageBlocks": [
            {
                "code": "helm upgrade --install emp-cost-agent \\\n  oci:\/\/quay.io\/platform9\/emp-helm-charts\/emp-cost-agent \\\n  --namespace emp --create-namespace \\\n  --set empProfiler.empReportSync=\"<report-location>\" \\\n  --set empProfiler.token=\"<token>\"",
                "language": "none"
            }
        ]
    }
}]$

- `helm upgrade install`: Initiates the Helm installation process for the EMP Cost Analyzer and names it emp-cost-agent.
- `oci://quay.io/`: Specifies the Helm chart repository and the specific chart (`emp-cost-agent`) to be installed. In this case, it points to the `quay.io` repository and retrieves the `emp-cost-agent` chart.
- `--namespace emp --create-namespace`: Specifies the namespace (`emp`) for deploying the EMP Cost Analyzer and creates the namespace if it doesn't exist.
- `empProfiler.empReportSync`: Specifies the report location utilized by the EMP Cost Analyzer for storing collected metrics data and reports. The report location is created and managed by Platform9.
- `empProfiler.token`: Specifies the token used by Cost Analyzer to push reports.

$plugin[{
    "type": "callout",
    "data": {
        "text": "After installing the EMP Cost Analyzer Helm Chart, please allow at least **1 hour** for the Cost Analyzer to start generating the report.",
        "type": "info",
        "title": "Info"
    }
}]$

## Uninstallation

Run the following command to uninstall the EMP Cost Analyzer:

$plugin[{
    "type": "code-block",
    "data": {
        "languageBlocks": [
            {
                "code": "helm uninstall emp-cost-agent --namespace emp",
                "language": "none"
            }
        ]
    }
}]$

### Data Collection for Cost Reporting

The EMP Cost Analyzer gathers and processes essential data from your EKS clusters to generate comprehensive cost reports, including:

- CPU Utilization (Average, Peak, Median)
- Memory Utilization (Average, Peak, Median)
- Sum of Requests of all Pods (CPU, Memory)
- Sum of Limits of all Pods (CPU, Memory)
- Node Details:
    - Instance Types and Family-wise Count
    - Mapping of Availability Zones (AZs)
    - Master/Worker Count
    - Number of Pods Scheduled on Node

- PVCs (If attached)

EMP does not collect, process, store, or access personal information or data about users.

