---
type: page
title: IO2 Migration Guide
listed: true
slug: io2-migration-guide-for-emp
description: 
index_title: IO2 Migration Guide
hidden: 
keywords: 
tags: 
---published

Platform9 EMP recommends the use of AWS EBS volumes of type `io2` for best performance during EVM live migration. This document outlines why io2 volumes are preferred and provides a script that will enable you to transition to `io2` volumes. 

## Why io2 volumes with EMP

EMP utilizes components such as [auto$](/emp/emp-rebalancer) and [auto$](/emp/live-migration) of EVMs to achieve the most optimized usage of the underlying bare metal resources. The EVM live migration process requires that any associated EBS volumes are also migrated over from source bare metal node to target. 

The choice of volume types determines the performance of EVM live migration.

For EBS volumes that do not support multi-attach, the process of detaching the volume from the source bare-metal node and attaching to the target node requires roughly **7 seconds**.

For volumes supporting multi-attach (`io2`), this process is seamless as the volume can simultaneously be attached to both source and target bare metal nodes. 

## Why io2 over io1

The AWS `io1` volumes only offer multi-attach support in specific AWS regions only. US East, US West, and Asia Pacific. In contract, the io2 volumes support a much broader range of AWS regions for multi-attach support. 

How to use the EMP Migration Script

$plugin[{
    "type": "callout",
    "data": {
        "text": "Ensure that the script has the necessary permissions to perform volume-related operations in your AWS environment.",
        "type": "info",
        "title": "Info"
    }
}]$

The following migration script enables transition to io2 volumes.

_Download the Script:_

- Obtain the migration script from [GitHub](https://github.com/platform9/support-locker/blob/master/emp/migrate_to_io2.py).

_Install Python3:_

- Download and install Python3 from [Python.org](https://www.python.org/downloads/) or follow [Ubuntu installation](https://www.cherryservers.com/knowledgebase/linux/install-python-3-8-on-ubuntu-20-04).

_Install Pip:_

- Use the following command for Ubuntu:

$plugin[{
    "type": "code-block",
    "data": {
        "languageBlocks": [
            {
                "code": "sudo apt-get install python3-pip",
                "language": "none"
            }
        ]
    }
}]$

_Install Required Packages:_

- Execute the following commands:

$plugin[{
    "type": "code-block",
    "data": {
        "languageBlocks": [
            {
                "code": "pip install argparse boto3 math logging time botocore threading",
                "language": "none"
            }
        ]
    }
}]$

_Run the Script:_

- Use the provided script with your AWS credentials and region:

$plugin[{
    "type": "code-block",
    "data": {
        "languageBlocks": [
            {
                "code": "python3 migrate_to_io2.py --aws_access_key_id AWS_ACCESS_KEY_ID --aws_secret_access_key AWS_SECRET_ACCESS_KEY --region_id AWS_REGION_ID --volume_ids vol-1xxxxxxxxxxxxxx vol-2xxxxxxxxxxxxxx",
                "language": "none"
            }
        ]
    }
}]$

- Optional: Set IOPS per GB with `--iops_per_gb` (default is 500; maximum allowed by AWS is 64000).

