---
type: page
title: Bare Metal Pool Configuration
listed: true
slug: bare-metal-pool-configuration
description: 
index_title: Bare Metal Pool Configuration
hidden: 
keywords: 
tags: 
---published

$plugin[{
    "type": "callout",
    "data": {
        "text": "EMP currently supports **one bare metal pool per EMP** instance. Multiple bare metal pools per EMP will be supported in future releases.",
        "type": "warning",
        "title": "Info"
    }
}]$

## Configuration Options

### Instance Type Selection

Choose an AWS EC2 metal instance type for your bare metal pool.

Recommendations:

- Select an instance type similar to your current EKS cluster EC2 VM nodes.
- For general use, we suggest **m5.metal**, which offers a balance of computing power, memory, and network bandwidth.

Suitable workloads for **m5.metal** include:

- Web or application servers
- Small to mid-sized databases
- Cluster computing tasks
- Gaming servers
- Caching fleets
- Application development environments

### VPC & Subnet Configuration

Select the Virtual Private Cloud (VPC) type and configure VPC settings for bare metal pool nodes. For detailed information, refer to the [auto$](/emp/bare-metal-pool-vpc-config) guide.

### Availability Zone Selection

Specify the AWS Availability Zone(s) (AZ) for bare metal node deployment.

- Multiple AZ selection: At least one bare metal node will be deployed in each selected AZ.
- Choose this option if your workloads are currently spread across multiple AZs.
- Ensures high availability for workloads deployed on EVMs created in this bare metal pool.

### Scaling

Set the minimum and maximum number of bare metal nodes for your pool.

Key considerations for multi-AZ setups:

1. **If max &lt; number of selected AZs**: Nodes will be deployed in a random subset of AZs. For eg if your max value is 2 but you selected 3 AZs, the bare metal nodes will be deployed in 2 AZs that are randomly selected out of the 3.
2. **If max &gt; number of selected AZs**: Nodes will be distributed evenly across AZs when possible. In case when equal distribution is not possible, one or more AZs will be randomly selected to have more bare metal nodes than others.
3. **For high availability**: Set min = number of selected AZs to ensure at least one node per AZ.

**Note**: You can modify scaling options later using the EMP UI bare metal pool edit feature.

### SSH Key Injection

Select an SSH key from your AWS account to be injected into each new bare metal instance. This SSH key enables secure access to these instances, allowing you to log in for administration purposes.

### Operating System

Currently, only **Ubuntu 20.04** is supported for bare metal instances.

If your environment requires a different hypervisor operating system, please contact [support@platform9.com](mailto:support@platform9.com) and provide additional details.

