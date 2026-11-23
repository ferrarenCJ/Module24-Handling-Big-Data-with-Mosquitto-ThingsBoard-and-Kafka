# Mini-Lesson 24.7: Understanding Code Blocks for Constructing a Web Server Using Kafka

---

# Overview

This lesson provides a detailed walkthrough of the code used to build a Kafka producer and consumer architecture using Node.js.

The goal is to understand the foundational code blocks required to:

- Create Kafka consumers
- Create Kafka producers
- Subscribe to topics
- Publish messages
- Build a web server
- Stream data through Kafka

Students use the:

```text
johnKafka
```

repository to explore a simplified implementation consisting of:

```text
One Producer
One Consumer
One Server
```

Before building large-scale streaming applications.

---

# IoT and Kafka

Modern IoT systems consist of:

```text
Devices
Sensors
Servers
Producers
Consumers
Applications
```

Architecture:

```text
Producer
    ↓
Kafka Topic
    ↓
Kafka Broker
    ↓
Consumer
    ↓
Web Server
```

Kafka simplifies the management of:

```text
Large Volumes of Data

Streaming Events

Device Communication
```

---

# Project Structure

Navigate to:

```text
johnKafka
```

↓

```text
helloTest
```

---

# Application Components

The application contains:

```text
server.js
myconsumer.js
myproducer.js
```

---

# Server

Starts using:

```cmd
node server.js
```

Accessible at:

```text
http://localhost:5000
```

---

# Purpose

The server:

- Accepts requests
- Runs the consumer
- Runs the producer
- Displays results

---

# Consumer

File:

```text
myconsumer.js
```

Purpose:

```text
Receive data
```

from Kafka.

---

# Consumer Definition

```javascript
const myconsumer =
function myconsumer(topic)
```

The consumer accepts:

```text
Kafka Topic
```

as an argument.

---

# Kafka Initialization

```javascript
const Kafka =
require('node-rdkafka');

const bootstrapServers =
'localhost:9092';

var response = "";
```

---

# Explanation

### node-rdkafka

Provides Kafka functionality within Node.js.

---

### bootstrapServers

Defines:

```text
Kafka Broker Address
```

Example:

```text
localhost:9092
```

---

### response

Stores messages returned by the consumer.

---

# createConsumer()

## Purpose

Create and connect a Kafka consumer.

---

## Code

```javascript
function createConsumer(onData) {

    const consumer =
        new Kafka.KafkaConsumer(
        {
            'bootstrap.servers':
            bootstrapServers,

            'group.id':
            'node-example-group-1'
        },
        {
            'auto.offset.reset':
            'earliest'
        });

    return new Promise(
        (resolve, reject) => {

            consumer
                .on(
                    'ready',
                    () =>
                    resolve(consumer)
                )
                .on(
                    'data',
                    onData
                );

            consumer.connect();
    });
}
```

---

# What Happens?

### Create Consumer

```javascript
new Kafka.KafkaConsumer()
```

---

### Register Events

```javascript
.on('ready')
```

Waits for connection.

---

### Register Data Handler

```javascript
.on('data')
```

Processes incoming messages.

---

### Connect

```javascript
consumer.connect()
```

Connects to Kafka.

---

# consumerExample()

## Purpose

Consume Kafka messages.

---

## Code Summary

```javascript
consumer.subscribe(
    [topic.topic]
);

consumer.consume();
```

---

# Workflow

```text
Kafka Topic
       ↓
Subscribe
       ↓
Consume
       ↓
Process Messages
```

---

# Logging

Example:

```javascript
console.log(
  `Consumed record`
)
```

Purpose:

```text
Monitoring

Debugging

Verification
```

---

# Subscription

```javascript
consumer.subscribe(
    [topic.topic]
);
```

Subscribes to a Kafka topic.

Example:

```text
vehicle-location
```

---

# Consume Messages

```javascript
consumer.consume();
```

Starts receiving records.

---

# Disconnect Handling

```javascript
process.on(
    'SIGINT',
    ...
)
```

Handles:

```text
Ctrl + C
```

cleanly.

---

# Error Handling

```javascript
consumerExample()
.catch(...)
```

Logs failures.

Example:

```text
Connection Error

Topic Error

Broker Error
```

---

# Export Consumer

```javascript
exports.myconsumer =
    myconsumer
```

Makes the consumer available to:

```text
server.js
```

---

# Producer

File:

```text
myProducer.js
```

Purpose:

```text
Send Data
```

to Kafka.

---

# Producer Workflow

```text
Data
  ↓
Producer
  ↓
Topic
  ↓
Broker
```

---

# Configuration

```javascript
const bootstrapServers =
    'localhost:9092';
```

Defines the Kafka broker.

---

# Topic Validation

Function:

```javascript
ensureTopicExists()
```

---

# Purpose

Verify the topic exists.

Example:

```text
vehicle-location
```

---

# Topic Creation

```javascript
adminClient.createTopic()
```

Creates:

```text
Topic
```

if necessary.

---

# Error Handling

Kafka Error:

```text
ERR_TOPIC_ALREADY_EXISTS
```

Code:

```javascript
36
```

---

# Meaning

Topic already exists.

No action needed.

---

# createProducer()

## Purpose

Create a Kafka producer.

---

## Code

```javascript
new Kafka.Producer(
{
    'bootstrap.servers':
    bootstrapServers,

    'dr_msg_cb':
    true
});
```

---

# Delivery Reports

```javascript
delivery-report
```

Tracks successful message delivery.

Example:

```text
Message Sent
```

---

# Error Events

```javascript
event.error
```

Handles failures.

Examples:

```text
Broker Unavailable

Connection Failure
```

---

# produceExample()

## Purpose

Publish data.

---

# Producer Logic

```javascript
for (
    let idx = 0;
    idx < 10;
    ++idx
)
```

Creates:

```text
10 Messages
```

---

# Message Example

```javascript
const key = 'john';

const value =
Buffer.from(
JSON.stringify({
    count: idx
}));
```

---

# Example Payload

```json
{
    "count": 0
}
```

```json
{
    "count": 1
}
```

```json
{
    "count": 2
}
```

---

# Publish Messages

```javascript
producer.produce(
    mytopic.topic,
    -1,
    value,
    key
);
```

---

# Producer Workflow

```text
Key + Value
      ↓
Produce
      ↓
Topic
      ↓
Broker
```

---

# Logging

Example:

```javascript
Successfully produced record
```

Purpose:

```text
Trace Message Delivery
```

---

# Flush Messages

```javascript
producer.flush()
```

Ensures:

```text
All Messages Delivered
```

before disconnecting.

---

# Disconnect

```javascript
producer.disconnect()
```

Closes the connection.

---

# Export Producer

```javascript
exports.myproducer =
    myproducer;
```

Allows:

```text
server.js
```

to access producer functions.

---

# Complete Architecture

```text
Producer
    ↓
Kafka Topic
    ↓
Kafka Broker
    ↓
Consumer
    ↓
Web Server
```

---

# Project 24.2 Connection

Required Project 24.2 uses these exact concepts.

Students will:

### Producer

Publish:

```json
{
    "latitude": 33.875,
    "longitude": -118.090
}
```

---

### Consumer

Consume:

```text
Vehicle Location Events
```

---

### Web Server

Display:

```text
Streaming GPS Data
```

---

# Example Vehicle Event

```json
{
    "vehicle_id": "SCG001",
    "latitude": 33.875,
    "longitude": -118.090
}
```

---

# Real-World Implementation

Thousands of devices:

```text
Sensors

Vehicles

Meters
```

can simultaneously:

```text
Publish
```

while applications:

```text
Consume
```

events through Kafka.

---

# Fleet Intelligence Platform Connections

The architecture maps directly to fleet telemetry systems.

Example:

```text
Vehicle GPS
      ↓
Kafka Producer
      ↓
Kafka Topic
      ↓
Kafka Broker
      ↓
Node.js Consumer
      ↓
Fleet Dashboard
```

---

# Example Fleet Payload

```json
{
    "vehicle_id": "SCG001",
    "latitude": 33.875,
    "longitude": -118.090,
    "speed": 58
}
```

---

# Fleet Use Cases

```text
Vehicle Tracking

Route Optimization

Fuel Monitoring

Geofencing

Driver Analytics
```

---

# Key Concepts

| Concept | Description |
|----------|-------------|
| Producer | Sends messages |
| Consumer | Receives messages |
| Topic | Communication channel |
| Broker | Kafka server |
| Node.js | JavaScript runtime |
| KafkaConsumer | Consumer class |
| Producer Class | Publishes messages |
| Delivery Report | Message confirmation |
| Topic Creation | Kafka topic provisioning |
| Bootstrap Server | Kafka broker address |

---

# Key Learning Outcomes

Successfully explained:

✅ Kafka Consumer Architecture

✅ Kafka Producer Architecture

✅ Kafka Topic Management

✅ Message Publishing

✅ Message Consumption

✅ Logging Strategy

✅ Error Handling

✅ Node.js Kafka Integration

✅ Event Streaming Fundamentals

---

# My Key Takeaways

- Consumers subscribe to Kafka topics and receive streaming data.
- Producers publish data using key-value pairs.
- Kafka topics organize communication channels.
- Logging is important for monitoring and debugging streaming systems.
- Topic validation prevents producer failures.
- Delivery reports verify successful message transmission.
- Exporting producer and consumer modules allows integration with a Node.js web server.
- These building blocks form the foundation of Required Project 24.2 and many real-world streaming applications.