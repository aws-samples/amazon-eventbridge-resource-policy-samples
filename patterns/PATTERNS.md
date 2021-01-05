# Multi-account design patterns with Amazon EventBridge

> For more information regarding these patterns see AWS re:Invent 2020 session [Building event-driven applications with Amazon EventBridge](https://virtual.awsevents.com/media/t/1_ynykxz80/186983983) which is available on demand.

In this section, there are two sample applications that implement the patterns for single-bus and multi-bus topologies across multiple accounts.

Having an "account-per-service" strategy is what many AWS users like doing because having multiple accounts provides services a blast radius, it provides additional security boundaries, and allows you to easily track service costs.

## [Single-bus, multi-account account pattern](single-bus-multi-account-pattern/README.md)

When you use EventBridge with multiple accounts, even if you adopt a singe bus topology, you need for additional event buses in the receiving accounts. This bus to communication is what facilitates the transfer of events between account boundaries.

It is very typical for organizations to have a "DevOps" team that is responsible for managing a shared resource via a single event bus. Each service team owns and manages its own application stack, while the DevOps team manages the stack that defines event bus rules and target configurations for the services integrations.  

With a multi-account scenario, the routing patterns are still managed by the rule in the DevOps bus, but the target configurations that were managed by the rules in the DevOps bus now point to the receiving event bus in the target accounts, and the service integration for the applications migrate to event bus in the receiving account.

![Single-bus, multi-account](../docs/images/single-bus-multi-account.png "Single-bus, multi-account")

## [Multi-bus, multi-account account pattern](multi-bus-multi-account-pattern/README.md)
In this pattern, each of the event buses are owned by the service teams. Each of the service teams manages their own buses. There is no centralized management of routing logic or target configuration.

Once the integration between sending and receiving buses has been established to facilitate cross account delivery of events, service teams manage.

![Multi-bus, multi-account](../docs/images/multi-bus-multi-account.png "Single-bus, multi-account")

If you have any questions, please raise an issue in the GitHub repo.