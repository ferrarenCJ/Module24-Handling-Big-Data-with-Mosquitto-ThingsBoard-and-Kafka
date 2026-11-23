# Required Project 24.2
# Constructing a Web Server Using Kafka

## Module 24
### Handling Big Data with Mosquitto, ThingsBoard, and Kafka

---

# Objective

The objective of this project was to build a complete Kafka-based streaming solution capable of:

- Creating a Kafka cluster
- Creating Kafka topics
- Publishing vehicle location telemetry
- Consuming Kafka messages
- Building a Node.js web server
- Displaying streaming data through a browser

This project demonstrates an end-to-end producer-consumer architecture using Kafka.

---

# Final Architecture

```text
PublishVehicleCoordinates.py
            │
            ▼
      Kafka Producer
            │
            ▼
vehicle-coordinates Topic
            │
            ▼
       Kafka Broker
            │
            ▼
      Kafka Consumer
         (Node.js)
            │
            ▼
       Web Server
            │
            ▼
       Browser UI
```

---

# Technologies Used

| Technology | Purpose |
|------------|----------|
| Python | Kafka Producer |
| Kafka | Event Streaming Platform |
| Docker | Container Platform |
| Confluent Platform | Kafka Environment |
| Node.js | Web Server Runtime |
| Express | Node.js Web Framework |
| KafkaJS | Kafka Consumer Library |
| ZooKeeper | Kafka Coordination Service |

---

# Kafka Environment

Kafka was deployed using the provided Confluent Docker Compose environment.

## Containers

The following Kafka services were successfully deployed:

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

# Confluent Control Center

URL:

```text
http://localhost:9021
```

Cluster Status:

```text
Healthy
```

Services:

```text
Kafka Broker
Kafka Connect
ksqlDB
ZooKeeper
```

---

# Kafka Topic

Created topic:

```text
vehicle-coordinates
```

Configuration:

```text
Partitions: 1
Replication Factor: Default
```

Purpose:

```text
Store simulated vehicle GPS coordinates
```

---

# Python Producer

File:

```text
PublishVehicleCoordinates.py
```

Purpose:

```text
Generate random vehicle locations
Publish coordinates to Kafka
```

---

# Producer Configuration

Topic:

```python
topic_name = "vehicle-coordinates"
```

---

# Coordinate Generation

Longitude:

```python
longitude = random.randint(-180, 180)
```

Latitude:

```python
latitude = random.randint(-90, 90)
```

---

# Example Payload

```json
{
    "longitude": 127,
    "latitude": 50
}
```

---

# Producer Send

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

longitude: 174 latitude: 56
```

---

# Node.js Consumer

Directory:

```text
NodeJSConsumer
```

Files:

```text
server.js
myconsumer.js
package.json
```

---

# Original Course Issue

The course materials use:

```javascript
node-rdkafka
```

and:

```javascript
const Kafka = require('node-rdkafka');
```

---

# Compatibility Problem

The latest environment contained:

```text
Node.js v22.23.5
```

Installation of:

```text
node-rdkafka
```

failed due to:

```text
node-gyp
```

and:

```text
Microsoft Visual Studio Build Tools
```

requirements.

Example error:

```text
Could not find any Visual Studio installation to use
```

---

# Solution

Replaced:

```javascript
node-rdkafka
```

with:

```javascript
kafkajs
```

---

# KafkaJS Installation

Installed:

```cmd
npm install kafkajs
```

Package:

```json
"kafkajs": "^2.2.4"
```

---

# Updated Consumer

Consumer implementation now uses:

```javascript
const { Kafka } = require('kafkajs');
```

---

# Kafka Consumer Flow

```text
Kafka Broker
        ↓
KafkaJS Consumer
        ↓
Vehicle Coordinates Topic
        ↓
Console Output
```

---

# Example Consumer Output

```text
Consumed value {"longitude":-169,"latitude":-55}

Consumed value {"longitude":9,"latitude":59}

Consumed value {"longitude":175,"latitude":-36}

Consumed value {"longitude":-44,"latitude":6}
```

---

# Web Server

File:

```text
server.js
```

Server Port:

```text
5000
```

---

# Home Page

URL:

```text
http://localhost:5000
```

Title:

```text
Confluence Kafka REST
```

Button:

```text
Consume Vehicle Coordinates
```

---

# Consumer Route

```javascript
app.get("/consumer", (req,res)=>{
    let topic = "vehicle-coordinates"
    response = consumer.myconsumer({
        topic: topic
    })

    res.send(
        "Success- Consumed: " + topic
    );
})
```

---

# Successful Message Consumption

Browser:

```text
Success- Consumed: vehicle-coordinates
```

Console:

```text
Consumed value {"longitude":-169,"latitude":-55}

Consumed value {"longitude":9,"latitude":59}

Consumed value {"longitude":175,"latitude":-36}
```

---

# Docker Resource Configuration

WSL2 configuration:

```ini
[wsl2]
memory=8GB
processors=4
localhostForwarding=true
```

Purpose:

```text
Support Kafka and Confluent workloads.
```

---

# Producer / Consumer Architecture

Producer:

```text
PublishVehicleCoordinates.py
```

Publishes:

```json
{
    "longitude": 127,
    "latitude": 50
}
```

---

Consumer:

```text
NodeJSConsumer
```

Consumes:

```json
{
    "longitude": 127,
    "latitude": 50
}
```

---

# Kafka Benefits Observed

Kafka provides:

✅ High throughput

✅ Message persistence

✅ Producer / Consumer decoupling

✅ Topic-based communication

✅ Scalability

✅ Fault tolerance

---

# Fleet Intelligence Platform Connections

This project closely aligns with a future fleet telemetry architecture.

Example:

```text
Vehicle GPS Device
        ↓
Kafka Producer
        ↓
Kafka Topic
        ↓
Kafka Broker
        ↓
Kafka Consumer
        ↓
Fleet Dashboard
```

---

# Example Fleet Payload

```json
{
    "vehicle_id": "SCG001",
    "longitude": -118.090,
    "latitude": 33.875,
    "speed": 58
}
```

---

# Potential Fleet Applications

```text
Vehicle Tracking

Route Optimization

Fuel Monitoring

Maintenance Alerts

Driver Analytics

Geofence Monitoring
```

---

# Key Learning Outcomes

Successfully demonstrated:

✅ Kafka Cluster Deployment

✅ Kafka Topic Creation

✅ Python Producer Development

✅ Vehicle Coordinate Simulation

✅ Kafka Consumer Development

✅ Node.js Web Server Creation

✅ KafkaJS Integration

✅ Browser Interaction

✅ Producer / Consumer Architecture

✅ End-to-End Event Streaming

---

# Deliverables Completed

| Step | Status |
|--------|--------|
| Project Extraction | ✅ |
| Docker Resources Configuration | ✅ |
| Kafka Cluster Deployment | ✅ |
| Confluent Control Center | ✅ |
| Default Topics Verification | ✅ |
| Vehicle Coordinates Topic | ✅ |
| Kafka Python Installation | ✅ |
| Producer Template | ✅ |
| Producer Code Modification | ✅ |
| Coordinate Data Production | ✅ |
| Node.js Verification | ✅ |
| Server.js Modification | ✅ |
| KafkaJS Installation | ✅ |
| Node.js Server Startup | ✅ |
| Kafka Web Interface | ✅ |
| Kafka Message Consumption | ✅ |

---

# Project Status

```text
Required Project 24.2
COMPLETED SUCCESSFULLY
```

---

## Notes

The original course material relied on:

```text
node-rdkafka
```

which required:

```text
Visual Studio Build Tools
Desktop Development with C++
```

Because these tools were unavailable in the environment, the Kafka consumer was successfully implemented using:

```text
KafkaJS
```

which provided equivalent Kafka consumer functionality without requiring native compilation.

---

**Author:** Clifford Ferraren  
**Program:** MIT Professional Education - Applied Data Engineering Program  
**Module:** Module 24 - Handling Big Data with Mosquitto, ThingsBoard, and Kafka