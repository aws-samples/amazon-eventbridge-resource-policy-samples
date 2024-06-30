# Multi-account design patterns with Amazon EventBridge

> For more information regarding these patterns see AWS re:Invent 2020 session [Building event-driven applications with Amazon EventBridge](https://virtual.awsevents.com/media/t/1_ynykxz80/186983983) which is available on demand.

In this section, there are two sample applications that implement the patterns for single-bus and multi-bus topologies across multiple accounts. 

In both cases we are illustrating 3 service teams creating a blue, purple and orange microservice.  I’ve named them after colors to keep them as agnostic as possible and allow you to substitute your own names for your own particular use cases.  The important thing to remember is that they each represent a unique service boundary that is using EventBridge to publish and subscribe to events from other services.

Each service has its own own autonomous development team not dissimilar to AWS’ two pizza team concept.

The Purple service subscribe to Event 1 (E1) from the Blue service and Event 3 (E3) from the Orange Service, and both the Blue and Orange services subscribing to Event 2 (E2), which is published by the Purple service.

## Single-bus, multi-account account pattern

When you use Amazon EventBridge with multiple accounts, event buses need to be created in the account receiving events. At this point in time, EventBridge does not allow you to directly invoke services (such as AWS Lambda) in other accounts. This bus-to-bus communication is what facilitates the transfer of events between account boundaries.

It is very typical for organizations to have a "DevOps" team that is responsible for managing a shared resource via a single event bus. Each service team owns and manages its own application stack, while the DevOps team manages the stack that defines event bus rules and target configurations for the services integrations.  

![Single-bus, multi-account](../docs/images/single-bus-multi-account.png "Single-bus, multi-account")

**Walkthrough the [Single-bus, multi-account account pattern](single-bus-multi-account-pattern/README.md) >>**

## Multi-bus, multi-account account pattern

In this pattern, each of the event buses are owned by the service teams. Each of the service teams manages their own buses. There is no centralized management of routing logic or target configuration.

Service teams need to be aware of the services that are interested in subscribing to events they are publishing. Each event bus sets it's own EventBusPolicy to scope what event sources can publish to the bus, and create EventBusPolicies defining which accounts can manage rules and targets on their account.

![Multi-bus, multi-account](../docs/images/multi-bus-multi-account.png "Multi-bus, multi-account")

**Walkthrough the [Multi-bus, multi-account account pattern](multi-bus-multi-account-pattern/README.md) >>**

## Cross-region event routing with Amazon EventBridge

In this scenario, a company has their base of operations located in Asia Pacific (Singapore) with applications distributed across two additional Regions in US East (N. Virginia) and Europe (Frankfurt).  The applications in US East (N. Virginia) and Europe (Frankfurt) are using Amazon EventBridge for their respective applications and services.  The security team in Asia Pacific (Singapore) wishes to analyse events from the respective applications as well as receive AWS CloudTrail events for specific API calls made to specific operations to monitor infrastructure security.

**Walkthrough the [Cross-region, cross-account pattern](cross-region-cross-account-pattern/README.md) >>**

![Cross-Region](../docs/images/cross-region.png "Cross-Region")
