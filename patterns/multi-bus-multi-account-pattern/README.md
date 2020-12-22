# Multi-bus, multi-account pattern

![Multi-bus, multi-account pattern](../../docs/images/multi-bus-multi-account.png "Multi-bus, multi-account pattern")

### Characteristics

- Each service team manages their own event bus
- No additional buses required to facilitate cross account event delivery
- Aligned to service boundary

### Team

- Service teams manage all resources for sending and receiving events

### Considerations

- Additional overhead in managing distributed rules and resource policies
