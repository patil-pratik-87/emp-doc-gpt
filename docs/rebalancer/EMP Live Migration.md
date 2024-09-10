---
type: page
title: EMP Live Migration
listed: true
slug: live-migration
description: 
index_title: EMP Live Migration
hidden: 
keywords: 
tags: 
---published

### Overview

EMP's EVM live migration is a unique and differentiated feature that allows the movement of running EVMs between bare metal nodes within an EMP bare metal pool. This process occurs without powering off the EVM or disrupting the pods running on it, ensuring uninterrupted uptime and availability of your Kubernetes workloads.

### Live migration process

The live migration process involves transferring the EVM state from the source to the target bare metal node while the source EVM workload continues to run. This strategy is fast, safe, and easily cancellable, making it ideal for minimizing downtime in most scenarios.

$plugin[{
    "type": "image",
    "data": {
        "url": "https:\/\/uploads.developerhub.io\/prod\/ZGrW\/qd5a49emav311wx545p4kidjibrbia1435crsvs8k4f10ewjbamed99m6ghpedw5.png",
        "mode": "full",
        "width": 861,
        "height": 601,
        "caption": null
    }
}]$

### Key Components

1. **State and Memory Transfer**: Copies the entire state and memory of the EVM from source to target.
2. **IP Address Management**: Migrates all associated IP addresses, including the EVM's primary IP and those of any running pods.
3. **Volume Migration**: Transfers all attached EBS or EFS volumes from source to target bare metal.

## Live migration stages

### Source Brownout

This is the initial and typically longest stage of the live migration process.

- The EVM continues to run on the source bare metal node.
- Memory pages and EVM state are continuously copied to the target node.
- Normal operations continue on the source EVM with minimal performance impact.

**Factors affecting duration:**

- EVM Memory Size:
    - Larger memory configurations take longer to copy.
    - Because all the EVM's RAM contents need to be copied from the source node to the destination node.
    - More memory means more data to transfer.

    - Example: An EVM with 256GB RAM will generally take longer than a 64GB RAM.

- Memory Write Rate:
    - High memory write activity creates more "dirty" pages that must be synced again.
    - CPU-intensive workloads with less memory churn migrate faster than memory-intensive ones.

- Network Bandwidth:
    - Higher bandwidth between source and target nodes can significantly speed up this stage.

### Blackout

This is the most critical and usually the briefest stage of the migration process.

- The EVM is momentarily paused on the source.
- Final memory pages and CPU state are copied to the target.
- The EVM is resumed on the target node.

**Factors affecting duration:**

- EBS Volume Type:
    - Newer generation (io1, io2): minimal blackout.
    - Older generation (gp2, gp3): Can take milliseconds to a few seconds.

- Number and Size of Attached Volumes:
    - More or larger volumes may extend the blackout period slightly.

- Current I/O Activity:
    - High I/O activity at the moment of transition can increase blackout time.

For this reason, EMP recommends working with next-generation EBS volumes for best VM migration performance.

### Target Brownout

This final stage ensures all components are fully transitioned to the target node.

- The EVM is now running on the target node.
- Network states and connections are being finalized.
- The source EVM may still exist but is inactive.

**Factors affecting duration:**

- Network Complexity:
    - More complex network configurations or more active connections may extend this stage.

EMP continuously monitors and can abort the migration process if any issues are detected, reverting to the source EVM with minimal impact. This fail-safe mechanism adds an extra layer of reliability to the live migration feature.

## Impact on pods

The live migration process has minimal to no impact on your workload. The only stage with potential performance impact is the brief blackout stage.

In EMP's live migration:

1. IP addresses associated with the EVM and its pods are maintained throughout the migration.
2. The migration occurs within the same network subnet.
3. No change in DNS records or IP addresses would require propagation.

The migration is designed to be transparent to the network layer, meaning:

- The EVM keeps its IP address(es).
- Pods running on the EVM maintain their IP addresses.
- No DNS changes are made or required.

This design ensures that network connections to the EVM and its pods remain intact throughout and after the migration process.

### Performance Examples

Consider an EVM instance of **m5.4xlarge** size (16 VCPU, 64 GB Memory), with a single 100GB EBS volume attached.

Let's observe the time it takes for the live migration to finish.

$plugin[{
    "type": "table",
    "data": {
        "cols": 3,
        "rows": 4,
        "widths": [
            248,
            0
        ],
        "contents": [
            [
                "**Task**",
                "**Blackout Time**",
                "**Brownout Time**"
            ],
            [
                "Empty EVM Migration",
                "0 sec",
                "25 seconds"
            ],
            [
                "EVM with 1 pod configured with 100GB memory and 100GB io2 EBS volume",
                "0 sec",
                "4 minutes 50 seconds"
            ],
            [
                "EVM with 1 pod configured with 100GB memory and 100GB **gp3 EBS volume**",
                "~7 sec",
                "4 minutes 50 seconds"
            ],
            [
                "EVM with 1 pod configured with 100GB memory and 100GB io2 EBS volume - Stress test rapidly writing data to memory in pod",
                "0 sec",
                "20 minutes"
            ]
        ]
    }
}]$

