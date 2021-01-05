# Single-bus, multi-account pattern

![Multi-bus, multi-account pattern](../../docs/images/single-bus-multi-account.png "Multi-bus, multi-account pattern")

## Characteristics

- Introduces the need for multiple event buses to transfer event between accounts
- Routing rules still via central bus
- Target rules migrate to service account event bus

### Team

- Service teams manage target configurations, but not routings

### Considerations

- Additional cross-account policy management (compared to single-bus, single account pattern)

## Installation Instructions

### Requirements

To run these samples in your own accounts you need to have the following tooling:

* AWS CLI already configured with Administrator permission
* [AWS SAM CLI installed](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)

1. [Create 4 AWS accounts](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have them and login

1. Clone this repo onto your local development machine:

``` bash
git clone https://github.com/aws-samples/amazon-eventbridge-resource-policy-samples
```

### Getting started

1. Deploy 