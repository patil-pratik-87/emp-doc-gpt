---
type: page
title: Supported load balancer for EMP
listed: true
slug: supported-load-balancer-for-emp
description: 
index_title: Supported load balancer for EMP
hidden: 
keywords: 
tags: 
---draft

EMP only supports using AWS NLB or AWS ALB for load balancing. The following table describes load balancers supported and not supported by EMP. 

Note that NLB and ALB are also [recommended load balancers by AWS](https://aws.amazon.com/elasticloadbalancing/faqs/#:~:text=If%20you%20need%20to%20load,recommend%20using%20Network%20Load%20Balancer.) .

$plugin[{
    "type": "table",
    "data": {
        "cols": 2,
        "rows": 3,
        "widths": [
            366
        ],
        "contents": [
            [
                "**Supported**",
                "**Not Supported**"
            ],
            [
                "Network Load Balancer (NLB)",
                "Classic Load Balancer (CLB)"
            ],
            [
                "Application Load Balancer (ALB)",
                "Gateway Load Balancers (GLB)"
            ],
            [
                "",
                "Third-party load balancers"
            ]
        ]
    }
}]$

$plugin[{
    "type": "callout",
    "data": {
        "text": "EMP only supports the target type \"IP\" for load balancers. Please ensure that your NLB\/ALB configurations align with this requirement to avoid compatibility issues with EMP.",
        "type": "warning",
        "title": "Warning"
    }
}]$

Following guides provide steps to configure these load balancer types in your AWS environment. 

- [auto$](/emp/nlb-for-emp)
- [auto$](/emp/alb-for-emp)

### Why EMP Doesn't Support the Elastic Load Balancer (ELB)?

#### Lack of Instance IDs

- AWS's Elastic Load Balancer (ELB) normally works with something called "Instance" targets.
- These targets use instance IDs, which are like unique names for regular virtual machines in AWS.
- EMP's Elastic Virtual Machines (EVMs) are different from regular virtual machines.
- EVMs don't have instance IDs, so they can't be used as "Instance" targets.

#### How EMP Uses IP Addresses Instead

- Since EVMs don't have instance IDs, they use IP addresses to identify themselves.
- The load balancer for EMP is set up to use these IP addresses directly.
- This is why EMP only supports the "IP" target type for load balancing.

This approach lets the load balancer route traffic to the EVMs based on their IP addresses, regardless of whether they have an instance ID.

---published

EMP only supports using AWS NLB or AWS ALB for load balancing. The following table describes load balancers supported and not supported by EMP. 

Note that NLB and ALB are also [recommended load balancers by AWS](https://aws.amazon.com/elasticloadbalancing/faqs/#:~:text=If%20you%20need%20to%20load,recommend%20using%20Network%20Load%20Balancer.) .

$plugin[{
    "type": "table",
    "data": {
        "cols": 2,
        "rows": 3,
        "widths": [
            366
        ],
        "contents": [
            [
                "**Supported**",
                "**Not Supported**"
            ],
            [
                "Network Load Balancer (NLB)",
                "Classic Load Balancer (CLB)"
            ],
            [
                "Application Load Balancer (ALB)",
                "Gateway Load Balancers (GLB)"
            ],
            [
                "",
                "Third-party load balancers"
            ]
        ]
    }
}]$

$plugin[{
    "type": "callout",
    "data": {
        "text": "EMP only supports the target type \"IP\" for load balancers. Please ensure that your NLB\/ALB configurations align with this requirement to avoid compatibility issues with EMP.",
        "type": "warning",
        "title": "Warning"
    }
}]$

Following guides provide steps to configure these load balancer types in your AWS environment. 

- [auto$](/emp/nlb-for-emp)
- [auto$](/emp/alb-for-emp)

