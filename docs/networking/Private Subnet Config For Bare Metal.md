---
type: page
title: Private Subnet Config For Bare Metal
listed: true
slug: networking-prereqs
description: 
index_title: Private Subnet Config For Bare Metal
hidden: 
keywords: 
tags: 
---published

If deploying bare metal nodes in a private subnet:

1. The private subnet **must have outbound network access**.
2. Recommended approach: Create a NAT gateway for your private subnet.

Follow the [AWS NAT Gateway deployment](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html) instructions for guidance.

### Validating Outbound Connectivity

To confirm outbound connectivity from your private subnet:

1. Deploy an EC2 instance in the private subnet.
2. From the EC2 instance, attempt to access the `emp.pf9.io` domain.
3. Use the following command to validate connectivity:

$plugin[{
    "type": "code-block",
    "data": {
        "languageBlocks": [
            {
                "code": "> curl emp.pf9.io",
                "language": "javascript"
            }
        ]
    }
}]$

A successful connection indicates proper outbound access.

