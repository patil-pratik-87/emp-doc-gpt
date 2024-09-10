---
type: page
title: EMP Rebalancer
listed: true
slug: emp-rebalancer
description: 
index_title: EMP Rebalancer
hidden: 
keywords: 
tags: 
---published

### Overview

The EMP Rebalancer optimizes resource utilization within an EMP instance while maintaining high availability for EVMs. It dynamically redistributes EVMs across bare metal nodes to balance CPU and Memory consumption, enhancing overall efficiency and preventing resource utilization spikes.

### Triggering conditions

The EMP Rebalancer initiates a rebalancing operation under the following conditions:

1. **High Resource Utilization**: When memory or CPU usage on any bare metal node exceeds the predefined threshold (default: **80%**).
2. **Uneven Workload Distribution**: Significant imbalance in workload across bare metal nodes (some overloaded, others underutilized).
3. **Node Health Issues**: Hardware failures or network problems lead to node removal and replacement.
4. **Node Consolidation**: Inefficient EVM distribution resulting in low pool utilization (e.g., after EVM scale-in events or decreased EVM resource usage).
5. **Insufficient Capacity**: Lack of capacity to accommodate new EVM creation, requiring a new bare metal node.

### Rebalancing process

The rebalancing process consists of three main steps:

1. **Identify Nodes for Rebalancing**: Locate bare metal nodes that meet trigger conditions and select EVMs for migration.
2. **Select Target Nodes**: Choose suitable target nodes based on resource utilization or create new ones if necessary.
3. **Redistribute EVMs**: Perform live migration of selected EVMs from source to target nodes without service disruption.

### EVM redistribution

EVM redistribution involves live migrating EVM between bare metal nodes without interrupting running pods. For detailed information on the live migration process, refer to the [auto$](/emp/live-migration) documentation.

### Bare Metal Pool Scaling

The Rebalancer may initiate scaling operations on the bare metal pool:

- **Scale Out**: Provision of new bare metal nodes when additional resources are required.
- **Scale In:** Consolidate EVMs onto fewer nodes and decommission unused ones when excess capacity is detected.

Both operations may result in EVM live migrations.

### Performance Considerations

While the Rebalancer is designed to minimize impact, users should be aware of the following:

- Live migrations may cause a slight increase in CPU usage on involved nodes.
- Network traffic increases during EVM transfers.
- Rebalancing operations on very large EVMs may take considerable time.
- Use [labels or taints](/emp/provision-workloads-on-evms) to guide EVM placements and prevent undesired migrations.

