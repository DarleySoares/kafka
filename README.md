# Kafka Projects

## Kafka

According to Apache enterprise, Apache Kafka is an open-source distributed event streaming plataform used by 
thousands of companies for high-performance data pipelines, streaming analytics, data integration, and mission-critical
applications. 
The principal characteristics of plataform are deliver messages using cluster of machines with latencies as low as 2ms, 
elastically expand to deliver trillions of messages by day, permanent storage and high availability.

The Kafka ecosystem works with 3 main concepts: events, producers and consumers.

An event records, it`s also called record or message, is "something happened" in your system, conceptually, an event has a key: value, timestamp and optional metadata
headers, for example:

> Event key: "USDBRL"
>
> Event value: "{'code':'USD', 'codein':'BRL', 'high':'5.432', 'low':'5.380', 'ask':'5.428', 'bid': '5.458'}"
>
> Event timestamp: "2022-01-25 12:45:55.000Z"

The producers are those client applications that publish (write) events to Kafka, this events are organized and durably stored in topics, a topic is similar to a folder in 
fileystem, and the events are the files in that folder. The topics are always multi-producer
and multi-subscriber. The consumers are those that subscribe to read and process these events.


## ZooKeeper

The Apache ZooKeeper is a centralized service for maintaining configuration information,
naming, providing distributed synchronization, and providing group services. All of these
kinds of services are used in some form or another by distributed applications. 

In Kafka, the ZooKeeper is used to determine which broker is the leader of a given partition and topic and perform leader elections. If a node by some reason is shutting
down, it's the controller's responsibility to tell all the replicas to act as partition
leaders in order to fulfill the duties of the partition leaders on the node that is about
to fail. It's also used to keeps a list of all functioning brokers in the cluster; maintains
the configuration of all topics, including the list of existing topics, number of partitions for each topic, location of the replicas and etc.; maintains the ACLs for all topicas and acesses how much data each client is allowed to read and write.


## Projects

* [Structured Streaming](./structured%20streaming/README.md)
