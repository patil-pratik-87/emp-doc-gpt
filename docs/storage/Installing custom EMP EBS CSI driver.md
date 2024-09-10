---
type: page
title: Installing custom EMP EBS CSI driver
listed: true
slug: installing-custom-ebs-csi-driver
description: 
index_title: Installing custom EMP EBS CSI driver
hidden: 
keywords: 
tags: 
---published

If you are using AWS EBS as a storage layer for your EKS cluster, and you have a requirement to use EBS CSI version that is less than `1.25.0`, then you will need to install the custom EMP EBS CSI driver. This driver will make required configuration changes to upstream EBS driver, so that EMP EVMs can utilize features such as volume multi-attach.

$plugin[{
    "type": "callout",
    "data": {
        "text": "Only install the EMP custom EBS CSI driver if you must use EBS CSI driver upstream version less than 1.25.0. If you do not have a requirement to use EBS CSI driver version lower than 1.25.0, then follow [auto$](\/emp\/emp-ebs-csi-config) instead.",
        "type": "error",
        "title": "Important"
    }
}]$

### Prerequisites

- If you intend to use the Volume Snapshot feature, the [Kubernetes Volume Snapshot CRDs](https://github.com/kubernetes-csi/external-snapshotter/tree/master/client/config/crd)  must be installed before the EMP EBS CSI driver is installed. For installation instructions on snapshot CRDs, see [CSI Snapshotter Usage](https://github.com/kubernetes-csi/external-snapshotter#usage).

### Step 1: Deploy EMP EBS Driver

You can deploy the EMP EBS CSI driver from the Platform9 github repository via Kustomize.

$plugin[{
    "type": "code-block",
    "data": {
        "languageBlocks": [
            {
                "code": "kubectl apply -k \"https:\/\/github.com\/platform9\/support-locker\/tree\/master\/emp\/ebs_csi_driver\"",
                "language": "none"
            }
        ]
    }
}]$

### Step 3: Verify

Once the driver has been deployed, verify the pods are running:

$plugin[{
    "type": "code-block",
    "data": {
        "languageBlocks": [
            {
                "code": "kubectl get pods -n kube-system -l app.kubernetes.io\/name=aws-ebs-csi-driver",
                "language": "none"
            }
        ]
    }
}]$

### Uninstalling the EMP EBS CSI Driver

Note: If your cluster is using EBS volumes, there should be no impact to running workloads. However, while the ebs-csi-driver daemonsets and controller are deleted from the cluster, no new EBS PVCs will be able to be created, and new pods that are created which use an EBS PV volume will not function (because the PV will not mount) until the driver is successfully re-installed. Uninstall the self-managed EBS CSI Driver with Kustomize, depending on your installation method.

$plugin[{
    "type": "code-block",
    "data": {
        "languageBlocks": [
            {
                "code": "kubectl delete -k \"github.com\/platform9\/support-locker\/emp\/ebs_csi_driver\"",
                "language": "none"
            }
        ]
    }
}]$

