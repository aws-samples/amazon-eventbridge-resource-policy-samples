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
