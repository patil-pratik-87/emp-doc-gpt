---
type: page
title: CIDR Configuration
listed: true
slug: cidr-config
description: 
index_title: CIDR Configuration
hidden: 
keywords: 
tags: 
---published

This document guides you in resolving CIDR conflicts when integrating EMP with your existing EKS clusters.

### EMP Default CIDRs:

EMP uses the following default CIDRs:

- **Container CIDR (10.20.0.0/16):** This range allocates IP addresses to containers within the EMP environment.
- **Pod CIDR (10.21.0.0/16):** This range assigns virtual IP addresses to services running on the bare metal pool.
- **VM Network CIDR (10.0.2.0/24):** This range allocates IP addresses to EVMs on bare metal nodes.

### Resolving CIDR Conflicts:

When integrating EMP with EKS clusters, conflicts may arise if the CIDR range used by your EKS cluster overlaps with one of EMP's default CIDR ranges.

To resolve CIDR conflicts, follow these steps:

- When you select an EKS cluster during EMP creation, the advanced section below the cluster selection grid will automatically expand if conflicts are detected. This indicates that there are CIDR conflicts that need to be resolved.
- Review the conflicting CIDR values. Adjust the CIDR values to ensure they do not overlap with existing EMP internal CIDRs.

Suppose your EKS cluster is using the following CIDR ranges:

$plugin[{
    "type": "code-block",
    "data": {
        "languageBlocks": [
            {
                "code": "VM Network CIDR: 10.0.0.0\/16\n\nContainer CIDR: 10.20.0.0\/16\n\nPod CIDR: 10.21.0.0\/16",
                "language": "none"
            }
        ]
    }
}]$

In this case, the Container CIDR and Pod CIDR of your EKS cluster overlap with the EMP internal CIDRs. You need to adjust the CIDR values to avoid conflicts. You can change the Container CIDR and Pod CIDR of your EKS cluster to non-overlapping ranges. Here are the adjusted CIDRs:

$plugin[{
    "type": "code-block",
    "data": {
        "languageBlocks": [
            {
                "code": "VM Network CIDR: 10.0.0.0\/16 (unchanged)\n\nContainer CIDR: 10.22.0.0\/16 (changed to avoid overlap with EMP Container CIDR)\n\nPod CIDR: 10.23.0.0\/16 (changed to avoid overlap with EMP Pod CIDR)",
                "language": "none"
            }
        ]
    }
}]$

- After adjusting the CIDR values, you will see that there are no overlapping errors in the advanced section.
- Once the conflicts are resolved and the CIDR values are adjusted, you can proceed with creating the EMP with your EKS clusters.

