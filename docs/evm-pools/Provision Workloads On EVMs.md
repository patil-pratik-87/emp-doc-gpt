---
type: page
title: Provision Workloads On EVMs
listed: true
slug: provision-workloads-on-evms
description: 
index_title: Provision Workloads On EVMs
hidden: 
keywords: 
tags: 
---published

This document describes the steps to provision your EKS cluster workloads to your Elastic Virtual Machine (EVM) nodes.

Once you create and configure an EMP instance to work with a set of EKS clusters, you can start deploying workloads on the EVM worker nodes created as part of your newly created EMP instance.

The EVM nodes that get provisioned as part of an EMP instance are created with the following taint:

$plugin[{
    "type": "code-block",
    "data": {
        "languageBlocks": [
            {
                "code": "emp.pf9.io\/EMPSchedulable=true:NoSchedule",
                "language": "json"
            }
        ]
    }
}]$

To ensure that any new pod instances are provisioned on EVM worker nodes, you must include `tolerations` and `nodeSelector` in your deployment specification.

## Automate the addition of tolerations

EMP provides a webhook to help automate adding `tolerations` and `nodeSelector` to your workloads. This webhook will add `tolerations` and `nodeSelector` to all new pod creation requests in the namespaces specified in the ConfigMap used to configure the webhook. 

To set up the webhook, follow these steps:

1. Create the following ConfigMap on your EKS cluster. This ConfigMap will configure the `emp-pod-webhook`.
2. The ConfigMap must be named `emp-profile-cm` and it must be placed in the `default` namespace.
3. You can provide labels or namespaces within the ConfigMap to enable the `emp-pod-webhook` to identify and select pods.

$plugin[{
    "type": "callout",
    "data": {
        "text": "The ConfigMap that configures the EMP webhook must be named _\"emp-profile-cm\"_ and it must be placed in the _\"default\"_ namespace. Additionally, the ConfigMap is required to be in the following format.",
        "type": "warning",
        "title": "Important"
    }
}]$

$plugin[{
    "type": "code-block",
    "data": {
        "languageBlocks": [
            {
                "code": "apiVersion: v1\nkind: ConfigMap\nmetadata:\n  name: emp-profile-cm\n  namespace: default\ndata:\n  labels: |\n    {\n        \"ElasticWorkload\": \"true\",\n        \"example-label\": \"example-value\"\n    }\n  namespaces: |\n    [\n        \"default\",\n        \"example-namespace\"\n    ]",
                "language": "none"
            }
        ]
    }
}]$

3. Apply the ConfigMap to your EKS cluster using the following command:

$plugin[{
    "type": "code-block",
    "data": {
        "languageBlocks": [
            {
                "code": "kubectl apply -f emp-profile-cm.yaml",
                "language": "none"
            }
        ]
    }
}]$

This command deploys the ConfigMap and configures the `emp-pod-webhook` to add `tolerations`  and `nodeSelector` to pods in the specified namespaces.

## Manually add tolerations

If you prefer to manually add `tolerations` and `nodeSelector` to your specifications, There are two ways you can do it. 

#### Deployment YAML Configuration

To update your Deployment to include the necessary `tolerations` and `nodeSelector`, follow these steps:

1. Edit the YAML configuration file for your Deployment.
2. Add the following `toleration` and `nodeSelector` to the `spec.template.spec` section of your Deployment YAML:

$plugin[{
    "type": "code-block",
    "data": {
        "languageBlocks": [
            {
                "code": "tolerations:\n- key: \"emp.pf9.io\/EMPSchedulable\"\n  operator: \"Equal\"\n  value: \"true\"\n  effect: \"NoSchedule\"\nnodeSelector:\n  emp.pf9.io\/owned: \"true\"",
                "language": "none"
            }
        ]
    }
}]$

This toleration allows the pods in your Deployment to be scheduled on EVM worker nodes with the `emp.pf9.io/EMPSchedulable` taint.

3. Save the changes to the YAML file and apply the updated configuration to your EKS cluster.
4. Note that any existing pods already deployed for the given deployment spec will continue to run on the non EVM worker nodes. You will need to restart the existing deployment after applying the required tolerations for them to be deployed on the EVM nodes.

Once these `tolerations` and `nodeSelector` are added to your deployment spec, any new instance of that pod will get provisioned on to the EVM worker nodes.

#### DaemonSet YAML Configuration

To update your DaemonSet to include the necessary tolerations and nodeSelector, follow these steps:

1. Edit the YAML configuration file for your DaemonSet.
2. Add the following `toleration` to the `spec.template.spec` of your DaemonSet YAML:

$plugin[{
    "type": "code-block",
    "data": {
        "languageBlocks": [
            {
                "code": "tolerations:\n- key: \"emp.pf9.io\/EMPSchedulable\"\n  operator: \"Equal\"\n  value: \"true\"\n  effect: \"NoSchedule\"",
                "language": "none"
            }
        ]
    }
}]$

This configuration allows the pods in your DaemonSet to be scheduled on both EC2 nodes and EVM worker nodes.

3. Save the changes to the YAML file and apply the updated configuration to your EKS cluster.
4. Note that any existing pods already deployed for the given spec will continue to run on the non EVM worker nodes. You will need to restart the existing DaemonSet after applying the required tolerations for them to be deployed on the EVM nodes.
5. **Optionally** you can add the following `nodeselector` to your DaemonSet spec to provision the DaemonSet pods EMP EVM nodes only. 

$plugin[{
    "type": "code-block",
    "data": {
        "languageBlocks": [
            {
                "code": "nodeSelector:\n  emp.pf9.io\/owned: \"true\"",
                "language": "json"
            }
        ]
    }
}]$

$plugin[{
    "type": "callout",
    "data": {
        "text": "**Existing Pods**: Any pods already deployed for the given spec will continue running on non-EVM worker nodes. You will need to restart the existing deployment\/daemonset after applying the required `tolerations` for them to be deployed on the EVM nodes.\n\n**New Pods**: Once these `tolerations` are added to your spec, any new instance of that pod will be provisioned on the EVM worker nodes.",
        "type": "info",
        "title": "Important Note"
    }
}]$

## Incrementally move workloads to EVMs

When working with EMP for the first time, we recommend that you incrementally move portions of your workload on to EVM nodes, then test those workload components over 1-2 weeks to ensure that the performance is as expected, then migrate more components of the workload to run on EVMs. 

The eventual goal should be to run all workloads on a given EKS cluster on EVMs, for maximum utilization and cost reduction benefits.  

## Remove taints from an EVM node

If you're considering comparing the performance of EVM-based workloads with EC2-based ones, removing the taints from the nodes makes it easier. Just remove the taints and let the workloads distribute naturally between the two types of nodes. 

$plugin[{
    "type": "callout",
    "data": {
        "text": "- Load balancers with non-IP targets won't route traffic to workloads on EVMs.\n- Workloads using non-io2 EBS volumes will have [longer pauses](\/emp\/io2-migration-guide-for-emp) if the EVM hosting them moves to another bare metal node.",
        "type": "warning",
        "title": "Side effects of removing taints from an EVM"
    }
}]$

Here is how you can remove the taints from the EVM node.

Identify the name of the EVM node from where you want to remove the taint. You can use the following command to list all nodes and their taints:

$plugin[{
    "type": "code-block",
    "data": {
        "languageBlocks": [
            {
                "code": "kubectl get nodes -o wide",
                "language": "none"
            }
        ]
    }
}]$

Once you have identified the node, you need to edit its configuration to remove the taint. You can do this using the following command, replacing `<node-name>`  with the name of your EVM node:

$plugin[{
    "type": "code-block",
    "data": {
        "languageBlocks": [
            {
                "code": "kubectl edit node <node-name>",
                "language": "none"
            }
        ]
    }
}]$

This command will open the node configuration in your default text editor. Look for the section that defines the `taints`  for the node. It will look something like this:

$plugin[{
    "type": "code-block",
    "data": {
        "languageBlocks": [
            {
                "code": "spec:\n  taints:\n  - effect: NoSchedule\n    key: emp.pf9.io\/EMPSchedulable\n    value: \"true\"",
                "language": "none"
            }
        ]
    }
}]$

To remove the taint, simply delete the entire `taints`  section from the configuration file.

Save the changes and exit the text editor. The node configuration will be updated automatically, and the taint will be removed from the node.

You can verify that the taint has been removed by running the following command:

$plugin[{
    "type": "code-block",
    "data": {
        "languageBlocks": [
            {
                "code": "kubectl describe node <node-name>",
                "language": "none"
            }
        ]
    }
}]$

Look for the absence of the taint in the output of this command. Once the taint has been removed, workloads will be able to schedule onto the EVM node without any restrictions.

## Pod deployment behind the scenes

The following diagram describes the workflow around how new pods in your EKS cluster will get provisioned on either an EVM node or a non EVM node, based on pod taint configuration. 

$plugin[{
    "type": "image",
    "data": {
        "url": "https:\/\/uploads.developerhub.io\/prod\/ZGrW\/45nit1dqei5kcu1v8mfennnyim26917qamxlaqacobw4gibthorwo3ou7bjazb74.png",
        "mode": "responsive",
        "width": 2670,
        "height": 1208,
        "caption": null
    }
}]$

When an instance of EMP is being created, EMP admission controller gets deployed in each of your EKS clusters that you associate with that EMP instance. The admission controller then intercepts every new pod deployment request and acts as a router to direct pods to be provisioned onto the EMP Elastic VM nodes instead of regular EC2 VM nodes, depending on the taint configuration for that pod. 

The admission controller works with an EMP Profile which provides rules to direct applications with above specified taints to the EMP EVM nodes.

