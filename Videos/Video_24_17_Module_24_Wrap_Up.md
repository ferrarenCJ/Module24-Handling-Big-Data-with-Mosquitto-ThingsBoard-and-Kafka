# Module 24: Wrap-Up

## Module 24
### Handling Big Data with Mosquitto, ThingsBoard, and Kafka

---

# Overview

Module 24 introduced three technologies used for handling real-time streaming and large-scale data:

1. Mosquitto
2. ThingsBoard
3. Kafka

Together, these technologies demonstrated how modern streaming systems:

- Collect data
- Transport data
- Process data
- Monitor data
- Analyze data
- Visualize data

across IoT and enterprise environments.

---

# Section 1: Mosquitto and MQTT

The first section focused on:

```text
MQTT
```

and:

```text
Mosquitto
```

---

# Key Concepts Learned

## MQTT

Message Queuing Telemetry Transport

A lightweight publish/subscribe messaging protocol designed for:

- IoT devices
- Sensors
- Telemetry systems
- Streaming applications

---

## Publish / Subscribe Architecture

```text
Publisher
     ↓
 Mosquitto Broker
     ↓
 Subscriber
```

---

## Mosquitto Broker

Mosquitto acts as the central communication hub.

Responsibilities:

- Receive messages
- Manage topics
- Route data
- Deliver messages

---

# Activities Completed

Students learned how to:

✅ Deploy Mosquitto using Docker

✅ Connect MQTT clients

✅ Publish messages

✅ Subscribe to topics

✅ Stream telemetry data

✅ Analyze MQTT use cases

---

# Discussion 24.1

Use Cases for Mosquitto

Highlighted applications:

- Manufacturing
- Healthcare
- Smart homes
- Automotive
- Telemetry systems

---

# Section 2: ThingsBoard

The second section focused on:

```text
ThingsBoard
```

and real-time telemetry processing.

---

# Key Concepts Learned

## Devices

Generate telemetry data.

Examples:

- Temperature sensors
- Humidity sensors
- GPS trackers

---

## Assets

Logical containers used to organize devices.

Examples:

- Buildings
- Vehicles
- Facilities

---

## Rule Engine

Processes incoming messages.

Responsibilities:

- Routing
- Filtering
- Transformation
- Alarm processing

---

## Root Rule Chain

Primary processing workflow inside ThingsBoard.

---

## Widgets

Visualization components used to display telemetry.

Examples:

- Charts
- Gauges
- Tables
- KPIs

---

## Alarms

Monitor telemetry values and trigger actions when threshold conditions are met.

Examples:

```text
High Temperature

Low Pressure

Device Offline
```

---

# Firebase Integration

Students created:

```text
module24Project
```

and configured:

```text
Firebase Realtime Database
```

to receive telemetry data.

---

# Required Project 24.1 Part 1

## Streaming Live Data to ThingsBoard

Completed:

✅ MQTT telemetry generation

✅ Temperature data publishing

✅ Humidity data publishing

✅ ThingsBoard ingestion

✅ Firebase integration

✅ End-to-end telemetry pipeline

---

# Required Project 24.1 Part 2

## Analyzing Live Streaming Data Using ThingsBoard

Completed:

✅ Alarm Rule Chains

✅ Threshold monitoring

✅ Alarm generation

✅ Firebase alarm integration

✅ Alarm data processing

---

# Major Technical Challenge

## SSL Certificate Trust Issue

While integrating:

```text
ThingsBoard
      ↓
Firebase
```

the environment encountered:

```text
PKIX path building failed
```

and:

```text
SSLHandshakeException
```

---

# Root Cause

Corporate SSL inspection replaced the Firebase certificate chain with:

```text
Sempra Energy Utilities Root Authority SHA2
```

which was not trusted by Java inside the ThingsBoard Docker container.

---

# Resolution

Exported:

```text
Sempra Energy Utilities Root Authority SHA2
```

and imported it into the Java truststore:

```bash
keytool -importcert ...
```

Result:

✅ Telemetry transmitted to Firebase

✅ Alarm data transmitted to Firebase

---

# Section 3: Kafka

The final section focused on:

```text
Apache Kafka
```

---

# Key Concepts Learned

## Producer

Publishes events.

Examples:

```text
Python Applications

IoT Devices

GPS Systems
```

---

## Consumer

Receives events.

Examples:

```text
Dashboards

Node.js Applications

Analytics Platforms
```

---

## Topic

Communication channel used to organize Kafka events.

Example:

```text
vehicle-coordinates
```

---

## Broker

Stores and distributes messages.

---

## ZooKeeper

Coordinates Kafka services.

---

# Kafka Deployment

Students deployed:

```text
Confluent Platform
```

using Docker.

Components included:

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

# Node.js

Students learned how to:

✅ Install Node.js

✅ Create web servers

✅ Use Express

✅ Build Kafka consumers

✅ Display data through a browser

---

# Producer / Consumer Pattern

```text
Producer
    ↓
Kafka Topic
    ↓
Broker
    ↓
Consumer
```

---

# Required Project 24.2

## Constructing a Web Server Using Kafka

Students created:

### Kafka Producer

Generated:

```json
{
    "longitude": 127,
    "latitude": 50
}
```

---

### Kafka Topic

```text
vehicle-coordinates
```

---

### Kafka Consumer

Consumed:

```text
Vehicle Coordinate Data
```

---

### Node.js Web Server

Served telemetry data through:

```text
http://localhost:5000
```

---

### Browser Interface

```text
Consume Vehicle Coordinates
```

---

# Major Technical Challenge

## node-rdkafka Compatibility

The course material relied on:

```text
node-rdkafka
```

which required:

```text
Visual Studio Build Tools

Desktop Development with C++
```

and was incompatible with:

```text
Node.js v22
```

---

# Resolution

Replaced:

```text
node-rdkafka
```

with:

```text
KafkaJS
```

Result:

✅ Successful data consumption

✅ Functional Node.js consumer

✅ No Visual Studio dependency

---

# End-to-End Streaming Architectures Completed

---

## MQTT / ThingsBoard Pipeline

```text
MQTT Publisher
       ↓
Mosquitto
       ↓
ThingsBoard
       ↓
Firebase
```

---

## Kafka Pipeline

```text
Python Producer
       ↓
Kafka Topic
       ↓
Kafka Broker
       ↓
Node.js Consumer
       ↓
Web Server
```

---

# Fleet Intelligence Platform Connections

Module 24 directly relates to modern fleet telemetry architectures.

Potential design:

```text
Vehicle Device
       ↓
MQTT / Kafka
       ↓
Broker
       ↓
Telemetry Processing
       ↓
Alerts
       ↓
Dashboards
```

---

# Example Fleet Event

```json
{
    "vehicle_id": "SCG001",
    "latitude": 33.875,
    "longitude": -118.090,
    "speed": 58,
    "fuel_level": 72
}
```

---

# Fleet Use Cases

```text
Vehicle Tracking

Fuel Monitoring

Route Optimization

Driver Analytics

Maintenance Alerts

Geofencing
```

---

# Module 24 Learning Outcomes

Successfully achieved:

✅ Identify key concepts related to Mosquitto, ThingsBoard, and Kafka

✅ Discuss use cases for Mosquitto, ThingsBoard, and Kafka

✅ Stream live data to ThingsBoard

✅ Analyze live streaming data using ThingsBoard

✅ Construct a web server using Kafka

---

# Key Skills Developed

✅ MQTT Messaging

✅ Broker Architecture

✅ Docker Deployment

✅ Telemetry Processing

✅ Rule Chains

✅ Alarm Configuration

✅ Firebase Integration

✅ Kafka Deployment

✅ Topic Management

✅ Producer Development

✅ Consumer Development

✅ Node.js Web Servers

✅ Event Streaming

✅ SSL Troubleshooting

---

# Module 24 Projects Completed

## Project 24.1 Part 1

Streaming Live Data to ThingsBoard

✅ Complete

---

## Project 24.1 Part 2

Analyzing Live Streaming Data Using ThingsBoard

✅ Complete

---

## Project 24.2

Constructing a Web Server Using Kafka

✅ Complete

---

# My Key Takeaways

- MQTT and Mosquitto provide lightweight messaging solutions for IoT systems.
- ThingsBoard provides telemetry management, visualization, rule processing, and alarm generation.
- Firebase can serve as a cloud destination for telemetry and alarm data.
- Kafka provides enterprise-grade event streaming capabilities at scale.
- Producers generate events while consumers process events.
- Node.js enables real-time web applications that consume Kafka data streams.
- Modern streaming architectures combine messaging brokers, stream processors, storage systems, and visualization tools into scalable event-driven ecosystems.
- The skills learned in Module 24 directly apply to IoT, fleet telemetry, smart utility systems, industrial monitoring, and large-scale data engineering platforms.