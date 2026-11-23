# Kafka Producer / Consumer Reference
# Module 24 Quick Reference

---

# Kafka Architecture

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

# Module 24 Architecture

```text
PublishVehicleCoordinates.py
            ↓
      Kafka Producer
            ↓
 vehicle-coordinates
            ↓
        Broker
            ↓
      Kafka Consumer
            ↓
        Node.js
            ↓
       Browser
```

---

# Kafka Components

## Producer

Publishes messages.

Example:

```json
{
    "longitude": 127,
    "latitude": 50
}
```

---

## Topic

Communication channel.

Example:

```text
vehicle-coordinates
```

---

## Broker

Stores and distributes messages.

---

## Consumer

Reads and processes messages.

---

## ZooKeeper

Coordinates Kafka services.

---

# Confluent Docker Services

```text
zookeeper
broker
schema-registry
rest-proxy
connect
ksqldb-server
ksqldb-cli
ksql-datagen
control-center
```

---

# Start Kafka Environment

```cmd
docker compose up -d
```

---

# Verify Containers

```cmd
docker ps
```

---

# Confluent Control Center

```text
http://localhost:9021
```

---

# Create Topic

```text
vehicle-coordinates
```

Partitions:

```text
1
```

---

# Kafka Python Producer

## Install

```cmd
pip install kafka-python
```

---

# Producer Imports

```python
import kafka
import json
import random
from time import sleep
```

---

# Topic

```python
topic_name = "vehicle-coordinates"
```

---

# Sample Payload

```python
sensor_data = {
    "longitude": 0,
    "latitude": 0
}
```

---

# Random Coordinates

```python
longitude = random.randint(-180, 180)

latitude = random.randint(-90, 90)
```

---

# Assign Values

```python
sensor_data["longitude"] = longitude

sensor_data["latitude"] = latitude
```

---

# Publish Message

```python
producer.send(
    topic_name,
    value=sensor_data
)
```

---

# Example Output

```text
longitude: 46 latitude: -20

longitude: 55 latitude: 63

longitude: 127 latitude: 50
```

---

# Node.js Setup

## Verify Installation

```cmd
node --version
```

Example:

```text
v22.23.5
```

---

# Install Dependencies

```cmd
npm install
```

---

# KafkaJS Installation

```cmd
npm install kafkajs
```

---

# Why KafkaJS?

Replaced:

```text
node-rdkafka
```

because:

```text
node-gyp
Visual Studio Build Tools
Desktop Development with C++
```

were unavailable.

---

# KafkaJS Import

```javascript
const { Kafka } = require('kafkajs');
```

---

# KafkaJS Consumer

```javascript
const kafka = new Kafka({
    clientId: 'vehicle-consumer',
    brokers: ['localhost:9092']
});
```

---

# Create Consumer

```javascript
const consumer = kafka.consumer({
    groupId: 'vehicle-group'
});
```

---

# Connect

```javascript
await consumer.connect();
```

---

# Subscribe

```javascript
await consumer.subscribe({
    topic: topic.topic,
    fromBeginning: true
});
```

---

# Consume Messages

```javascript
await consumer.run({
    eachMessage: async ({
        topic,
        partition,
        message
    }) => {

        const value =
            message.value.toString();

        console.log(value);
    }
});
```

---

# Express Server

## Import Express

```javascript
const express = require('express');
```

---

# Create App

```javascript
const app = express();
```

---

# Home Route

```javascript
app.get("/", (req,res)=>{
```

---

# Consumer Route

```javascript
app.get("/consumer", (req,res)=>{
```

---

# Kafka Topic

```javascript
let topic =
    "vehicle-coordinates";
```

---

# Start Server

```javascript
app.listen(
    5000,
    ()=>console.log(
        "Listening on 5000"
    )
);
```

---

# Access Web Application

```text
http://localhost:5000
```

---

# Expected Page

```text
Confluence Kafka REST

Consume Vehicle Coordinates
```

---

# Verify Consumer

Expected output:

```text
Consumed value
{"longitude":46,"latitude":-20}

Consumed value
{"longitude":55,"latitude":63}

Consumed value
{"longitude":127,"latitude":50}
```

---

# Common Commands

## Start Producer

```cmd
python PublishVehicleCoordinates.py
```

---

## Start Web Server

```cmd
node server.js
```

---

## Check Docker Containers

```cmd
docker ps
```

---

## View Broker Logs

```cmd
docker logs broker
```

---

## Stop Containers

```cmd
docker compose down
```

---

# Common Issues

## Topic Does Not Exist

Create topic:

```text
vehicle-coordinates
```

in Confluent Control Center.

---

## node-rdkafka Install Failure

Error:

```text
Visual Studio Build Tools required
```

Solution:

```cmd
npm install kafkajs
```

---

## SSL Errors

Typical:

```text
SELF_SIGNED_CERT_IN_CHAIN
```

Solution:

```cmd
npm config set strict-ssl false
```

---

## Kafka Broker Not Running

Verify:

```cmd
docker ps
```

and ensure:

```text
broker
```

is running.

---

# Producer vs Consumer

| Producer | Consumer |
|-----------|-----------|
| Sends data | Reads data |
| Python | Node.js |
| GPS Simulation | Display Coordinates |
| Write to Topic | Read from Topic |

---

# Example Fleet Event

```json
{
    "vehicle_id": "SCG001",
    "longitude": -118.090,
    "latitude": 33.875,
    "speed": 58
}
```

---

# Kafka Key Takeaways

✅ Kafka Topics store streaming events

✅ Producers publish data

✅ Consumers read data

✅ Kafka brokers manage message distribution

✅ KafkaJS provides a modern Node.js Kafka client

✅ Confluent Control Center simplifies Kafka management

✅ Producer/Consumer architectures are foundational to real-time data engineering systems