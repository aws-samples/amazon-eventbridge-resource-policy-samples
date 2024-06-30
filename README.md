# Amazon EventBridge resource policy samples

[Amazon EventBridge](https://aws.amazon.com/eventbridge) resource policies that make it easier to build applications that work across accounts. Resource policies provide you with a powerful mechanism for modeling your event buses across multiple accounts, and give you fine-grained control over EventBridge API invocations.

This repository contains sample implementations for Amazon EventBridge resource policies.

## 1. E-commerce example walk-through

This sample application walks you through how to use Amazon EventBridge resource policies as presented in [feature release blog post](https://aws.amazon.com/blogs/compute/simplifying-cross-account-access-with-amazon-eventbridge-resource-policies)

**[Get started with the e-commerce sample >](blog/README.md)**

![Walkthrough architecture](docs/images/ecommerce-example.png "Walkthrough architecture")

## 2. Multi-account design patterns

The samples in this section provide sample implementations using **"single-bus, multi-account"**, and **"multi-bus, multi-account"** patterns as presented in the AWS re:Invent 2020 session [Building event-driven applications with Amazon EventBridge](https://bit.ly/3KY9Mjc) which is available on-demand on YouTube.

**[Explore all the multi-account design patterns >](patterns/README.md)**

## Resources

### Videos

For more on this topic, check out these re:Invent recordings:

#### [Building event-driven applications with Amazon EventBridge](https://bit.ly/3KY9Mjc)

[![Walkthrough architecture](docs/images/reinvent_building.png "Building event-driven applications with Amazon EventBridge")](https://bit.ly/3KY9Mjc)

#### [Designing event-driven integrations using Amazon EventBridge](https://bit.ly/4eH9omB)

[![Walkthrough architecture](docs/images/reinvent_designing.png "Designing event-driven integrations using Amazon EventBridge")](https://bit.ly/4eH9omB)

### Workshops

#### [AWS Serverless Developer Experience](https://catalog.workshops.aws/serverless-developer-experience/en-US)

The AWS Serverless Developer Experience workshop offers hands-on experience building a serverless solution using AWS SAM and AWS SAM CLI. It covers event-driven architectures, messaging patterns, orchestration, observability, and their implementation. You'll explore open-source tools, Powertools for AWS Lambda, and simplified CI/CD deployments with AWS SAM Pipelines. The goal is to provide an immersive serverless development experience.

### Additional resources

For more serverless learning resources, visit [Serverless Land](https://serverlessland.com/).

## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This library is licensed under the MIT-0 License. See the LICENSE file.

Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
