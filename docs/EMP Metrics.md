---
type: page
title: EMP Metrics
listed: true
slug: emp-metrics
description: 
index_title: EMP Metrics
hidden: 
keywords: 
tags: 
---published

Each EMP instance reports metrics data that shows information about EMP performance over a period of time.

#### VM Steal Time 

VM steam time is the percentage of time the EVM CPU process is waiting on the physical CPU of the bare metal host for its share of CPU time. CPU steal time is reported in seconds. 

A high steal time value indicates that there may be high CPU contention on the bare metal node that this EVM is running on. 

#### VM Memory Swap Amount

VM memory swap amount indicates the average amount of memory (in GB) that was swapped over the given period of time. 

The amount of EVM memory swap utilized has a direct correlation to the impact of over-commitment on the EVM performance. If all EVMs on a given bare metal node start utilizing all of the memory allocated to them, and the bare metal memory is over-committed, then some or all of the EVMs may experience memory swap activity where a portion of the EVM's memory is swapped to disk to make room for memory from other EVMs.

