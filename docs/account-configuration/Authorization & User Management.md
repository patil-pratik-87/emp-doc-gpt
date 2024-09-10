---
type: page
title: Authorization & User Management
listed: false
slug: authorization---user-management
description: 
index_title: Authorization & User Management
hidden: 1
keywords: 
tags: 
---published

## Login & Authorisation

Each new deployment of EMP comes with a dedicated org using which you can access the EMP portal. 

EMP uses [Auth0](https://auth0.com/docs/get-started/auth0-overview) as identity and single sign on provider for authentication and authorization of users. Each new user that needs access to EMP portal needs to have a separate account created within Auth0 under your organization. Your platform administrator team working with the Platform9 customer success team should be able to get this setup.

Contact your platform administrator team for details about your organization's EMP account credentials. 

## User Management

EMP does not support multiple user roles today. Each user within your organization who gets access to your deployment of EMP is essentially an "admin" user. They have access to perform every operation that the EMP UI exposes. 

Support for the following additional roles is part of our roadmap: 

1. A read-only user role who can view everything in the EMP UI, including dashboards and reports, but does not have access to make any chances 
2. A self-service user role with access to limited functionality including adding or removing EKS clusters to an existing EMP instance. 

$plugin[{
    "type": "callout",
    "data": {
        "text": "EMP only supports \"administrator\" user role today. Support for additional user roles is coming in the future.",
        "type": "warning",
        "title": "Important"
    }
}]$

