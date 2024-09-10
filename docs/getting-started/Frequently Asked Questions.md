---
type: page
title: Frequently Asked Questions
listed: true
slug: frequently-asked-questions
description: 
index_title: FAQ
hidden: 
keywords: 
tags: 
---published

## Why EMP

$plugin[{
    "type": "custom-html",
    "data": {
        "contents": "<details class=\"AccordionSectionStyles__StyledAccordionItem-sc-1m27gtb-3 fbAaZS\" open=\"\">\n  <summary class=\"AccordionSectionStyles__StyledAccordionItemTitle-sc-1m27gtb-2 fuUTTz\">\n     How does EMP help DevOps teams and Developers?\n  <\/summary>\n  <div class=\"AccordionSectionStyles__StyledAccordionItemBody-sc-1m27gtb-4 gOGZoq\">\n    <p>Read <a private-link=\"true\" link-type=\"page\" href=\"\/docs\/emp-docs\/emp\/what-is-emp#emp-benefits-for-developers-and-devops\">EMP Benefits for Developers & DevOps<\/a><\/p>\n  <\/div>\n<\/details>"
    }
}]$

$plugin[{
    "type": "custom-html",
    "data": {
        "contents": "<details class=\"AccordionSectionStyles__StyledAccordionItem-sc-1m27gtb-3 fbAaZS\" open=\"\">\n  <summary class=\"AccordionSectionStyles__StyledAccordionItemTitle-sc-1m27gtb-2 fuUTTz\">\n     Why should we consider EMP when we are already using other cost management tools?\n  <\/summary>\n  <div class=\"AccordionSectionStyles__StyledAccordionItemBody-sc-1m27gtb-4 gOGZoq\">\n    <p>Read <a private-link=\"true\" link-type=\"page\" href=\"\/docs\/emp-docs\/emp\/what-is-emp#emp-vs-other-kubernetes-cost-management-tools\">EMP vs Other Kubernetes Cost Optimization Tools<\/a> to understand EMP differentiation vs other Kubernetes Cost Optimization and Monitoring Tools<\/p>\n  <\/div>\n<\/details>"
    }
}]$

$plugin[{
    "type": "custom-html",
    "data": {
        "contents": "<details class=\"AccordionSectionStyles__StyledAccordionItem-sc-1m27gtb-3 fbAaZS\" open=\"\">\n  <summary class=\"AccordionSectionStyles__StyledAccordionItemTitle-sc-1m27gtb-2 fuUTTz\">\n     What Kubernetes expertise is required to run EMP?\n  <\/summary>\n  <div class=\"AccordionSectionStyles__StyledAccordionItemBody-sc-1m27gtb-4 gOGZoq\">\n    <p>Any Kubernetes administrator can implement EMP. While implementing EMP does not require deep Kubernetes expertise, a basic understanding and knowledge of Kubernetes concepts and an in-depth understanding of your existing EKS environment are required.<\/p>\n  <\/div>\n<\/details>"
    }
}]$

## Integration

$plugin[{
    "type": "custom-html",
    "data": {
        "contents": "<details class=\"AccordionSectionStyles__StyledAccordionItem-sc-1m27gtb-3 fbAaZS\" open=\"\">\n  <summary class=\"AccordionSectionStyles__StyledAccordionItemTitle-sc-1m27gtb-2 fuUTTz\">\n     What cloud platforms and sofware does EMP support?\n  <\/summary>\n  <div class=\"AccordionSectionStyles__StyledAccordionItemBody-sc-1m27gtb-4 gOGZoq\">\n    <p>Read <a private-link=\"true\" link-type=\"page\" href=\"\/docs\/emp-docs\/emp\/supported-cloud-infra\">Supported Clouds & Infra<\/a><\/p>\n  <\/div>\n<\/details>"
    }
}]$

$plugin[{
    "type": "custom-html",
    "data": {
        "contents": "<details class=\"AccordionSectionStyles__StyledAccordionItem-sc-1m27gtb-3 fbAaZS\" open=\"\">\n  <summary class=\"AccordionSectionStyles__StyledAccordionItemTitle-sc-1m27gtb-2 fuUTTz\">\n     Does EMP require changes to my EKS clusters?\n  <\/summary>\n  <div class=\"AccordionSectionStyles__StyledAccordionItemBody-sc-1m27gtb-4 gOGZoq\">\n    <p>EMP integrates seamlessly with your existing EKS clusters and requires zero changes to your clusters. Just provide your AWS credentials, and within minutes, you can install EMP and configure it to work with your existing, or new EKS clusters. You can then direct some or all of your workloads to run on EMP nodes.<\/p>\n  <\/div>\n<\/details>"
    }
}]$

$plugin[{
    "type": "custom-html",
    "data": {
        "contents": "<details class=\"AccordionSectionStyles__StyledAccordionItem-sc-1m27gtb-3 fbAaZS\" open=\"\">\n  <summary class=\"AccordionSectionStyles__StyledAccordionItemTitle-sc-1m27gtb-2 fuUTTz\">\n     Does EMP require changes to my applications?\n  <\/summary>\n  <div class=\"AccordionSectionStyles__StyledAccordionItemBody-sc-1m27gtb-4 gOGZoq\">\n    <p>No, EMP performs its optimization automatically in the background without any application changes.<\/p>\n  <\/div>\n<\/details>"
    }
}]$

$plugin[{
    "type": "custom-html",
    "data": {
        "contents": "<details class=\"AccordionSectionStyles__StyledAccordionItem-sc-1m27gtb-3 fbAaZS\" open=\"\">\n  <summary class=\"AccordionSectionStyles__StyledAccordionItemTitle-sc-1m27gtb-2 fuUTTz\">\n     What applications is EMP suitable for?\n  <\/summary>\n  <div class=\"AccordionSectionStyles__StyledAccordionItemBody-sc-1m27gtb-4 gOGZoq\">\n    <p>EMP is suitable for all applications that run on Kubernetes. This includes web applications that run java or scala, data analytics workloads, etc.<\/p>\n  <\/div>\n<\/details>"
    }
}]$

$plugin[{
    "type": "custom-html",
    "data": {
        "contents": "<details class=\"AccordionSectionStyles__StyledAccordionItem-sc-1m27gtb-3 fbAaZS\" open=\"\">\n  <summary class=\"AccordionSectionStyles__StyledAccordionItemTitle-sc-1m27gtb-2 fuUTTz\">\n     Will EMP impact my application SLAs?\n  <\/summary>\n  <div class=\"AccordionSectionStyles__StyledAccordionItemBody-sc-1m27gtb-4 gOGZoq\">\n    <p>No. One of the key value propositions of EMP is that it guarantees your application\u2019s SLA 100% of the time. EMP fully understands the resource request and limit values set by your Developers for your applications. EMP combines this information with the application\u2019s actual resource usage to dynamically adjust the amount of resources given to your application. So when your application actually needs the peak resources it\u2019s configured to use, it will always be given those resources. EMP employs technologies such as live migration of your virtual machine instances behind the scenes to no pod disruption is required in order to give your application the resources it requires. This means zero application downtime. Read more here about <a private-link=\"true\" link-type=\"page\" href=\"\/docs\/emp-docs\/emp\/live-migration\">EMP Live Migration<\/a>.<\/p>\n  <\/div>\n<\/details>"
    }
}]$

## Supported Software

$plugin[{
    "type": "custom-html",
    "data": {
        "contents": "<details class=\"AccordionSectionStyles__StyledAccordionItem-sc-1m27gtb-3 fbAaZS\" open=\"\">\n  <summary class=\"AccordionSectionStyles__StyledAccordionItemTitle-sc-1m27gtb-2 fuUTTz\">\n     What Kubernetes platforms does EMP support?\n  <\/summary>\n  <div class=\"AccordionSectionStyles__StyledAccordionItemBody-sc-1m27gtb-4 gOGZoq\">\n    <p>See <a private-link=\"true\" link-type=\"page\" href=\"\/docs\/emp-docs\/emp\/pre-requisites\">Pre-requisites<\/a> for supported platforms.<\/p>\n  <\/div>\n<\/details>"
    }
}]$

## Support & Customer Success

$plugin[{
    "type": "custom-html",
    "data": {
        "contents": "<details class=\"AccordionSectionStyles__StyledAccordionItem-sc-1m27gtb-3 fbAaZS\" open=\"\">\n  <summary class=\"AccordionSectionStyles__StyledAccordionItemTitle-sc-1m27gtb-2 fuUTTz\">\n     What support does Platform9 provide?\n  <\/summary>\n  <div class=\"AccordionSectionStyles__StyledAccordionItemBody-sc-1m27gtb-4 gOGZoq\">\n    <p>Read <a private-link=\"true\" link-type=\"page\" href=\"\/docs\/emp-docs\/emp\/Support\">EMP Support & Customer Success<\/a>\n<\/p>\n  <\/div>\n<\/details>"
    }
}]$

$plugin[{
    "type": "custom-html",
    "data": {
        "contents": "<details class=\"AccordionSectionStyles__StyledAccordionItem-sc-1m27gtb-3 fbAaZS\" open=\"\">\n  <summary class=\"AccordionSectionStyles__StyledAccordionItemTitle-sc-1m27gtb-2 fuUTTz\">\n     I have more questions!\n  <\/summary>\n  <div class=\"AccordionSectionStyles__StyledAccordionItemBody-sc-1m27gtb-4 gOGZoq\">\n    <p><a private-link=\"true\" link-type=\"page\" href=\"\/docs\/emp-docs\/emp\/Support\">Contact EMP Support<\/a>. We are here to help.\n<\/p>\n  <\/div>\n<\/details>"
    }
}]$

