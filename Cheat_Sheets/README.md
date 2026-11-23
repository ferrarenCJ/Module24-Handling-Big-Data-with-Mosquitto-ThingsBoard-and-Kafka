# Streaming Big Data Cheat Sheets
# Module 24: Mosquitto, ThingsBoard, and Kafka

## MIT Professional Education
### Applied Data Engineering Program

---

# Overview

This folder contains quick-reference guides and implementation notes developed while completing Module 24.

The objective of these cheat sheets is to provide a practical reference for:

- MQTT Messaging
- Mosquitto Broker Configuration
- ThingsBoard Rule Chains
- Firebase Integration
- Alarm Workflows
- Kafka Streaming
- Kafka Producers and Consumers
- Node.js Web Servers
- Docker Deployment
- SSL Troubleshooting

These notes summarize the concepts, commands, code snippets, troubleshooting techniques, and architectures used throughout the module.

---

# Cheat Sheets Included

## 1. Module 24 Mosquitto, ThingsBoard, and Kafka Cheat Sheet

```text
Module_24_Mosquitto_ThingsBoard_Kafka_Cheat_Sheet.md
```

### Topics Covered

- MQTT
- Mosquitto
- Paho MQTT
- ThingsBoard
- Firebase
- Rule Chains
- Alarm Processing
- Kafka
- KafkaJS
- Node.js
- Docker
- SSL Troubleshooting

### Purpose

Provides a complete end-to-end summary of all technologies introduced in Module 24.

---

## 2. Kafka Producer / Consumer Reference

```text
Kafka_Producer_Consumer_Reference.md
```

### Topics Covered

- Kafka Architecture
- Topics
- Producers
- Consumers
- KafkaJS
- Node.js
- Confluent Platform
- Web Servers
- Vehicle Coordinate Streaming

### Purpose

Provides implementation-focused Kafka examples and commands used during Project 24.2.

---

# Technologies Covered

## MQTT

Message Queuing Telemetry Transport

```text
Publisher
     ↓
 Broker
     ↓
Subscriber
```

Used for:

- IoT devices
- Sensors
- Telemetry systems

---

## Mosquitto

Open-source MQTT broker.

Responsibilities:

```text
Receive Messages
Manage Topics
Route Messages
Deliver Data
```

---

## ThingsBoard

Open-source IoT platform.

Capabilities:

```text
Device Management
Asset Management
Telemetry Processing
Visualization
Rule Chains
Alarm Processing
```

---

## Firebase

Google Realtime Database.

Used for:

```text
Telemetry Storage
Alarm Storage
Realtime Updates
Cloud Integration
```

---

## Kafka

Distributed event-streaming platform.

Architecture:

```text
Producer
    ↓
Topic
    ↓
Broker
    ↓
Consumer
```

Used for:

```text
Event Streaming
Analytics
Real-Time Processing
Large-Scale Messaging
```

---

## Node.js

Server-side JavaScript runtime.

Used for:

```text
Web Servers
Kafka Consumers
Streaming Applications
```

---

# Major Projects Completed

## Project 24.1 Part 1

### Streaming Live Data to ThingsBoard

Architecture:

```text
TBPublish.py
      ↓
MQTT
      ↓
Mosquitto
      ↓
ThingsBoard
      ↓
Firebase
```

Completed:

✅ MQTT Publisher

✅ ThingsBoard Integration

✅ Firebase Integration

✅ Temperature Telemetry

✅ Humidity Telemetry

---

## Project 24.1 Part 2

### Analyzing Live Streaming Data Using ThingsBoard

Architecture:

```text
Telemetry
      ↓
Root Rule Chain
      ↓
CreateAndClearAlarms
      ↓
AlarmToFirebase
      ↓
Firebase
```

Completed:

✅ Alarm Rule Chains

✅ Alarm Processing

✅ Firebase Alarm Integration

✅ Real-Time Monitoring

---

## Project 24.2

### Constructing a Web Server Using Kafka

Architecture:

```text
Python Producer
      ↓
Kafka Topic
      ↓
Kafka Broker
      ↓
Kafka Consumer
      ↓
Node.js Web Server
      ↓
Browser
```

Completed:

✅ Kafka Cluster

✅ Confluent Control Center

✅ Producer

✅ Consumer

✅ KafkaJS

✅ Web Application

---

# Important Troubleshooting Notes

## Firebase SSL Issue

### Error

```text
PKIX path building failed

SSLHandshakeException
```

---

### Cause

Corporate SSL inspection replaced Firebase certificates with:

```text
Sempra Energy Utilities Root Authority SHA2
```

---

### Resolution

Export:

```text
Sempra Energy Utilities Root Authority SHA2
```

Import into Java truststore:

```bash
keytool -importcert \
-alias sempra-root \
-file /tmp/SempraRoot.cer \
-keystore cacerts
```

Restart:

```bash
ThingsBoard
```

Result:

✅ Firebase Integration Restored

---

## KafkaJS vs node-rdkafka

The course materials utilized:

```text
node-rdkafka
```

However, modern environments may encounter:

```text
node-gyp
Visual Studio Build Tools
Desktop Development with C++
```

requirements.

---

### Alternate Solution

Install:

```cmd
npm install kafkajs
```

Benefits:

✅ Pure JavaScript

✅ No Build Tools

✅ No Native Compilation

✅ Modern Kafka Support

---

# Fleet Intelligence Platform Connections

The technologies covered in this module align closely with a future fleet telemetry platform.

Example:

```text
Vehicle GPS Device
          ↓
 MQTT / Kafka
          ↓
Broker
          ↓
Telemetry Processing
          ↓
Firebase / Storage
          ↓
Dashboards
          ↓
Alerts
```

---

# Example Fleet Event

```json
{
    "vehicle_id": "SCG001",
    "longitude": -118.090,
    "latitude": 33.875,
    "speed": 58,
    "fuel_level": 72
}
```

Potential applications:

```text
Vehicle Tracking
Fuel Monitoring
Geofencing
Maintenance Alerts
Driver Analytics
Route Optimization
```

---

# Module 24 Key Takeaways

✅ MQTT enables lightweight IoT communication.

✅ Mosquitto provides MQTT broker functionality.

✅ ThingsBoard manages telemetry, rule chains, and alarms.

✅ Firebase provides realtime cloud storage.

✅ Kafka enables enterprise-scale event streaming.

✅ Producers publish events.

✅ Consumers consume events.

✅ Node.js enables real-time web applications.

✅ Docker simplifies deployment.

✅ SSL troubleshooting is a critical real-world integration skill.

---

# Module Status

```text
Module 24 Successfully Completed
```

Projects Completed:

✅ Project 24.1 Part 1

✅ Project 24.1 Part 2

✅ Project 24.2

---

**Author:** Clifford Ferraren  
**Program:** MIT Professional Education – Applied Data Engineering Program  
**Module:** Module 24 – Handling Big Data with Mosquitto, ThingsBoard, and Kafka