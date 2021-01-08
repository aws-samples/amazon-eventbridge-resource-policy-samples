# Multi-account design patterns with Amazon EventBridge

> For more information regarding these patterns see AWS re:Invent 2020 session [Building event-driven applications with Amazon EventBridge](https://virtual.awsevents.com/media/t/1_ynykxz80/186983983) which is available on demand.

In this section, there are two sample applications that implement the patterns for single-bus and multi-bus topologies across multiple accounts.

## [Single-bus, multi-account account pattern](single-bus-multi-account-pattern/README.md)

When you use EventBridge with multiple accounts, even if you adopt a singe bus topology, you need for additional event buses in the receiving accounts. This bus to communication is what facilitates the transfer of events between account boundaries.

It is very typical for organizations to have a "DevOps" team that is responsible for managing a shared resource via a single event bus. Each service team owns and manages its own application stack, while the DevOps team manages the stack that defines event bus rules and target configurations for the services integrations.  

![Single-bus, multi-account](../docs/images/single-bus-multi-account.png "Single-bus, multi-account")

### Walkthrough the [Single-bus, multi-account account pattern](single-bus-multi-account-pattern/README.md) >>

## [Multi-bus, multi-account account pattern](multi-bus-multi-account-pattern/README.md)
In this pattern, each of the event buses are owned by the service teams. Each of the service teams manages their own buses. There is no centralized management of routing logic or target configuration.

Service teams need to be aware of the services that are interested in subscribing to events they are publishing. Each event bus sets it's own EventBusPolicy to scope what event sources can publish to the bus, and create EventBusPolicies defining which accounts can manage rules and targets on their account.

![Multi-bus, multi-account](../docs/images/multi-bus-multi-account.png "Multi-bus, multi-account")

### Walkthrough the [[Multi-bus, multi-account account pattern](multi-bus-multi-account-pattern/README.md) >>