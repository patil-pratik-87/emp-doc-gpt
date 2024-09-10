---
type: page
title: EMP EBS CSI Config
listed: true
slug: emp-ebs-csi-config
description: 
index_title: EMP EBS CSI Config
hidden: 
keywords: 
tags: 
---published

This document provides instructions for using the EBS CSI driver with EMP, including the necessary configurations for StorageClasses and PVCs.

### Assumption

This document assumes that

- You have followed the required AWS prerequisites to configure your EKS cluster to use EBS, including setting up the required IAM policies. Follow [this article](https://docs.aws.amazon.com/eks/latest/userguide/ebs-csi.html) for more information on using EBS with EKS.

## EMP EBS Config

To use EBS volumes with EMP EVM worker nodes, you must use the EBS CSI driver upstream version `1.25.0` or later. This driver version incorporates EMP-required features, such as multi-attach support. 

If you must use a version of EBS CSI earlier than 1.25.0, then you will need to install the custom EMP EBS CSI driver. Follow the instructions here to install the [EMP EBS driver](/emp/installing-custom-ebs-csi-driver). 

$plugin[{
    "type": "callout",
    "data": {
        "text": "To ensure compatibility with EMP, use the EBS CSI driver upstream version _`1.25.0`_  or later.\n\nIf you need to install versions of the EBS CSI driver before _`1.25.0`_ , use the [custom CSI driver install instructions](\/emp\/installing-custom-ebs-csi-driver) instead.",
        "type": "info",
        "title": "Compatibility"
    }
}]$

Follow the rest of this document to update your EBS CSI driver version to `1.25.0` or later, and configure it to use multi-attach as default setting.

## Steps to configure EBS

Install the [upstream EBS CSI driver](https://github.com/kubernetes-sigs/aws-ebs-csi-driver/blob/master/docs/install.md) or update your existing CSI driver to the latest version. 

### Configuring EBS Driver

EMP requires that you use EBS volumes of type io2 and with multi-attach functionality enabled, for EVM live migration to operate with best performance. Learn more about [why io2 volumes with EMP](/emp/io2-migration-guide-for-emp).

The next step is to ensure that your EBS CSI driver creates io2 volumes by default using StorageClass. Additionally, use the provided PVC template to enable multi-attach functionality for the io2 volumes.

### StorageClass Config

This StorageClass template will ensure the EBS CSI driver creates io2 volumes.

$plugin[{
    "type": "code-block",
    "data": {
        "languageBlocks": [
            {
                "code": "apiVersion: storage.k8s.io\/v1\nkind: StorageClass\nmetadata:\n  name: <STORAGE CLASS NAME>\nprovisioner: ebs.csi.aws.com\nparameters:\n  type: io2\n  iops: \"<REQUIRED IOPS>\"",
                "language": "none"
            }
        ]
    }
}]$

**Notes:**

- You must set `parameters.type`  to `io2`  to ensure the creation of `io2` volumes.
- You must specify `parameters.iops`.
- You can set additional parameters as needed.

### PVC Config

This PVC template will enable multi-attach functionality for the io2 volumes.

$plugin[{
    "type": "code-block",
    "data": {
        "languageBlocks": [
            {
                "code": "apiVersion: v1\nkind: PersistentVolumeClaim\nmetadata:\n  name: <PVC NAME>\nspec:\n  accessModes:\n    - ReadWriteMany\n  volumeMode: Block\n  storageClassName: <STORAGE CLASS NAME>\n  resources:\n    requests:\n      storage: <SIZE>",
                "language": "none"
            }
        ]
    }
}]$

**Notes:**

- `spec.accessModes` must be set to `ReadWriteMany` to enable multi-attach functionality for the io2 volumes.

The EBS CSI driver will continue to work as expected for non-EVM worker nodes in your EKS cluster. Note that these configurations do not alter the upstream functionality when used with non-EVM EC2 nodes, even if your EKS cluster uses both EVM and non-EVM worker nodes.

