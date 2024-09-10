---
type: page
title: Pricing FAQ
listed: true
slug: pricing-faq
description: 
index_title: Pricing FAQ
hidden: 
keywords: 
tags: 
---published

## EMP Flat-rate Pricing FAQ

### How does EMP flat-rate pricing work?

At the end of each month we calculate the following for all EVM instances you had running during that month:

1. What your AWS price would have been for running the EVMs, taking into account your current savings plan, EDP or other details. This is your 'Before Cost'.
2. Your actual spend on bare metal instances for that month. This is your 'After Cost'

The difference between 1 and 2 is your savings with EMP. We then charge you a % of the savings, assuming the savings were greater than zero. 

So for eg, say in the current month, you had 5 EVMs running of size m5.4xlarge for the entire month, and based on your current savings plan based rate it would have costed you $100 to run those EVMs. Then that would be your 'Before Cost'. Say with EMP we ran these EVMs on 1 m5.metal bare metal instance, and the cost of running that instance for that month was $50. This is your 'After Cost'. The difference is $50 which accounts for 50% savings. And we will charge you a certain pre-defined % off $50 to you for that month - in an invoice.

### How is EMP billed?

EMP is billed via a monthly invoice sent to you at the end of each month. 

### How do you work with my existing Savings Plan, EDP, other discounts?

Yes. In most cases, your existing savings plans, EDP or other commitment based discounts should apply to any bare metal instances deployed with EMP. [Contact us](/emp/Support) with your specific pricing commitment details and we'd be happy to assist.

## EMP Pre-Commit Discount Pricing FAQ

### How does pre-commit discount pricing work? 

Pre-commit discount based pricing for EMP works similar to a savings plan for AWS. If you pre-commit and pre-pay a certain amount upfront as part of your EMP contract, you will receive a discount on the % of savings rate that EMP charges you, up to the pre-commit amount. 

For example, say your are saving $10K per month with EMP for your EKS environment, $120K per year. With flat-rate pricing, you will be charged $2.5K per month - 25% of savings. If you pre-commit to paying say $5K per month or $60K annually and pre-pay that, then every month your savings up to $5K will be charged at a discounted rate (discussed and finalized as part of contract negotiation) vs the 25%. [Contact us](/emp/Support) with questions for more specific examples of pre-commit discount pricing.

