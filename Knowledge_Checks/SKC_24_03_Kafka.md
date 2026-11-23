# Self-Study Knowledge Check 24.3: Kafka

---

# Activity Information

| Item | Details |
|------------|---------|
| Module | Module 24: Handling Big Data with Mosquitto, ThingsBoard, and Kafka |
| Activity | Self-Study Knowledge Check 24.3 |
| Topic | Kafka |
| Questions | 6 |
| Points | 0 |
| Time Limit | None |
| Attempts | Unlimited |
| Estimated Time | 20 Minutes |
| Due Date | November 26, 2026 |

> This is a self-study activity and does not count toward program completion.

---

# Learning Outcome

- Identify key concepts related to Mosquitto, ThingsBoard, and Kafka.

---

# Knowledge Check Summary

This assessment covered:

- Kafka fundamentals
- Kafka topics
- Kafka producers
- Kafka consumers
- Kafka architecture
- Node.js fundamentals
- Streaming data at scale

---

# Question 1

## What is Kafka?

### Correct Answer

✅ Kafka is a distributed publish/subscribe messaging system used for processing big data at scale.

### Explanation

Apache Kafka is a distributed event-streaming platform designed to:

- Process large volumes of streaming data
- Connect producers and consumers
- Support real-time analytics
- Enable scalable data ingestion

### Example

```text
Producer
    ↓
 Topic
    ↓
 Broker
    ↓
Consumer
```

### Key Takeaway

Kafka is designed for large-scale event streaming and data processing.

---

# Question 2

## How is Kafka different from traditional message queuing projects, such as MQTT?

### Correct Answer

✅ Traditional message queuing projects cannot handle large volumes of messages, whereas Kafka can.

### Explanation

Kafka is specifically designed for:

- High throughput
- Large-scale event processing
- Massive streaming workloads
- Distributed architectures

While MQTT supports streaming and IoT messaging, Kafka excels at handling very large numbers of messages and consumers at scale.

### Key Takeaway

Kafka's primary advantage is its ability to process very large volumes of streaming data.

---

# Question 3

## What are producers in Kafka?

### Correct Answer

✅ Kafka producers are applications that write data to the Kafka brokers messaging queue.

### Explanation

Producers publish events to Kafka topics.

Example:

```json
{
    "latitude": 33.875,
    "longitude": -118.090
}
```

Workflow:

```text
Producer
    ↓
Kafka Topic
    ↓
Kafka Broker
```

### Key Takeaway

Producers send messages into Kafka.

---

# Question 4

## What are consumers in Kafka?

### Correct Answer

✅ Kafka consumers are applications that read data from the Kafka brokers messaging queue.

### Explanation

Consumers subscribe to topics and read events stored by Kafka.

Example:

```text
Kafka Broker
      ↓
Consumer
      ↓
Application
```

In Project 24.2:

```text
Node.js Web Server
```

acts as a Kafka consumer.

### Key Takeaway

Consumers receive and process Kafka messages.

---

# Question 5

## What are Kafka topics?

### Correct Answer

✅ Kafka topics are categories of messaging queues that are being made available for consumption.

### Explanation

Topics organize messages within Kafka.

Example:

```text
vehicle-location
```

Producer:

```text
Publishes to Topic
```

Consumer:

```text
Subscribes to Topic
```

Workflow:

```text
Producer
      ↓
Topic
      ↓
Consumer
```

### Key Takeaway

Topics are logical channels for organizing Kafka data streams.

---

# Question 6

## Which JavaScript engine does Node.js use?

### Correct Answer

✅ Node.js uses the Chrome V8 JavaScript engine.

### Explanation

The V8 engine:

- Compiles JavaScript into machine code
- Executes JavaScript efficiently
- Powers Node.js applications

Node.js leverages the same engine used by:

```text
Google Chrome
```

### Key Takeaway

Node.js runs on Google's V8 JavaScript engine.

---

# Kafka Concepts Reinforced

## Producer

Publishes messages.

Example:

```json
{
    "count": 1
}
```

---

## Consumer

Reads messages.

Example:

```text
Node.js Application
```

---

## Topic

Communication channel.

Example:

```text
vehicle-location
```

---

## Broker

Stores and distributes messages.

---

## Event Streaming

Continuous flow of records.

Example:

```text
GPS Coordinates

Telemetry Data

Sensor Readings
```

---

# Kafka Architecture Review

```text
Producer
    ↓
Topic
    ↓
Broker
    ↓
Consumer
```

---

# Node.js Review

Node.js is:

```text
JavaScript Runtime
```

powered by:

```text
Chrome V8 Engine
```

Used for:

- APIs
- Web Servers
- Streaming Applications
- Kafka Consumers

---

# Relationship to Project 24.2

Project 24.2 uses:

### Producer

Python application publishing:

```json
{
    "latitude": 33.875,
    "longitude": -118.090
}
```

---

### Topic

```text
vehicle-location
```

---

### Consumer

Node.js application.

---

### Output

Web Server displaying streaming data.

---

# Fleet Intelligence Platform Connections

Kafka concepts map closely to enterprise telemetry systems.

### Producer

```text
Vehicle GPS Device
```

---

### Topic

```text
vehicle-location
```

---

### Consumer

```text
Fleet Dashboard
```

---

### Example Event

```json
{
    "vehicle_id": "SCG001",
    "latitude": 33.875,
    "longitude": -118.090,
    "speed": 58
}
```

---

# Real-World Kafka Applications

## Transportation

```text
Fleet Tracking

GPS Monitoring
```

---

## Finance

```text
Transaction Processing

Fraud Detection
```

---

## Manufacturing

```text
Machine Telemetry

Predictive Maintenance
```

---

## Utilities

```text
Smart Meter Data

Pressure Monitoring
```

---

# Final Review Notes

✅ Kafka is a distributed publish/subscribe messaging system

✅ Kafka processes large volumes of streaming data

✅ Producers write messages to Kafka

✅ Consumers read messages from Kafka

✅ Topics organize Kafka data streams

✅ Node.js consumers commonly process Kafka messages

✅ Node.js uses the Chrome V8 JavaScript engine

✅ Kafka forms the foundation of many modern real-time streaming architectures

---

# Score

| Questions | Correct |
|------------|---------|
| 6 | 6 |
| Accuracy | 100% |

All Kafka concepts were answered correctly.