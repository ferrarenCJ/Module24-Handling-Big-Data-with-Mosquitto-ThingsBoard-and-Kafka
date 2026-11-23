# Module 24: Solution Files

## Module 24
### Handling Big Data with Mosquitto, ThingsBoard, and Kafka

---

# Overview

This document summarizes the official solution files provided for Module 24 projects.

These solutions demonstrate complete implementations of:

- MQTT Telemetry Streaming
- ThingsBoard Integration
- Firebase Storage
- Alarm Processing
- Kafka Event Streaming
- Node.js Web Applications
- Producer / Consumer Architectures

The solution files can be used to:

- Compare implementations
- Troubleshoot assignments
- Validate outputs
- Review project architectures
- Study real-world streaming data workflows

---

# Solution Files

## Project 24.1 (Part 1)
### Streaming Live Data to ThingsBoard

---

### Project Objective

Create a complete streaming telemetry pipeline capable of:

- Producing MQTT telemetry
- Publishing telemetry to Mosquitto
- Processing telemetry in ThingsBoard
- Storing telemetry in Firebase

---

### Architecture

```text
TBPublish.py
      ↓
MQTT Publisher
      ↓
Mosquitto Broker
      ↓
ThingsBoard
      ↓
Firebase
```

---

### Key Deliverables

✅ Mosquitto Configuration

✅ MQTT Publishing

✅ Temperature Telemetry

✅ Humidity Telemetry

✅ ThingsBoard Integration

✅ Firebase Integration

---

### Technologies Used

```text
Python
Paho MQTT
Mosquitto
ThingsBoard
Firebase
Docker
```

---

# Project 24.1 (Part 2)
### Analyzing Live Streaming Data Using ThingsBoard

---

### Project Objective

Implement alarm monitoring and rule-chain processing using ThingsBoard.

---

### Architecture

```text
MQTT Telemetry
       ↓
Root Rule Chain
       ↓
CreateAndClearAlarms
       ↓
AlarmToFirebase
       ↓
Firebase
```

---

### Key Deliverables

✅ Alarm Rule Chain

✅ TempToFirebase Rule Chain

✅ AlarmToFirebase Rule Chain

✅ Alarm Creation

✅ Alarm Clearing

✅ Firebase Alarm Storage

---

### Example Alarm

```text
General Alarm

Severity: Critical

Originator:
DHT11 Demo Device
```

---

### Technologies Used

```text
ThingsBoard
Rule Chains
Firebase
MQTT
Mosquitto
Docker
```

---

# Project 24.2
### Constructing a Web Server Using Kafka

---

### Project Objective

Build a complete Kafka producer-consumer architecture and display consumed data through a Node.js web server.

---

### Architecture

```text
PublishVehicleCoordinates.py
            ↓
      Kafka Producer
            ↓
vehicle-coordinates Topic
            ↓
        Kafka Broker
            ↓
      Kafka Consumer
            ↓
       Node.js Server
            ↓
          Browser
```

---

### Key Deliverables

✅ Kafka Cluster Deployment

✅ Topic Creation

✅ Python Producer

✅ Node.js Consumer

✅ Web Server

✅ Message Consumption

---

### Example Kafka Event

```json
{
    "longitude": 127,
    "latitude": 50
}
```

---

### Example Consumer Output

```text
Consumed value {"longitude":127,"latitude":50}

Consumed value {"longitude":46,"latitude":-20}

Consumed value {"longitude":55,"latitude":63}
```

---

### Technologies Used

```text
Kafka
Confluent Platform
Python
Node.js
Express
KafkaJS
Docker
```

---

# Major Lessons Learned

---

## MQTT and Mosquitto

Learned:

```text
Publish / Subscribe

Topics

Brokers

Paho MQTT
```

---

## ThingsBoard

Learned:

```text
Devices

Assets

Rule Chains

Widgets

Alarms

Firebase Integration
```

---

## Kafka

Learned:

```text
Producers

Consumers

Topics

Brokers

Clusters

Partitions
```

---

## Node.js

Learned:

```text
Web Servers

Express

Kafka Consumers
```

---

# Important Troubleshooting Outcomes

---

## Firebase SSL Trust Issue

Error:

```text
PKIX path building failed

SSLHandshakeException
```

---

### Cause

Corporate TLS inspection replaced Firebase certificates using:

```text
Sempra Energy Utilities Root Authority SHA2
```

---

### Resolution

Imported certificate into the Java truststore:

```bash
keytool -importcert \
-alias sempra-root \
-file /tmp/SempraRoot.cer \
-keystore /usr/lib/jvm/java-17-openjdk-amd64/lib/security/cacerts \
-storepass changeit \
-noprompt
```

Result:

✅ Firebase integration restored

---

## Kafka Consumer Compatibility Issue

Issue:

```text
node-rdkafka
```

required:

```text
Visual Studio Build Tools
Desktop Development with C++
```

---

### Resolution

Installed:

```cmd
npm install kafkajs
```

and migrated the consumer implementation to:

```javascript
const { Kafka } = require('kafkajs');
```

Result:

✅ Kafka consumer functional

✅ No Visual Studio dependency

---

# Module 24 Project Progression

## Project 24.1 Part 1

```text
Telemetry Streaming
```

---

## Project 24.1 Part 2

```text
Alarm Processing
```

---

## Project 24.2

```text
Event Streaming
Producer / Consumer Architecture
```

---

# Fleet Intelligence Platform Connections

The solutions completed throughout Module 24 map directly to future fleet telemetry architectures.

Example:

```text
Vehicle GPS Device
         ↓
 MQTT / Kafka
         ↓
 Broker
         ↓
 Processing Engine
         ↓
 Storage
         ↓
 Dashboards
         ↓
 Alerts
```

---

# Example Fleet Telemetry

```json
{
    "vehicle_id": "SCG001",
    "longitude": -118.090,
    "latitude": 33.875,
    "speed": 58,
    "fuel_level": 72
}
```

---

# Potential Future Applications

```text
Vehicle Tracking

Route Optimization

Fuel Monitoring

Driver Analytics

Geofencing

Maintenance Alerts

Predictive Maintenance
```

---

# Projects Completed

| Project | Status |
|----------|--------|
| Project 24.1 Part 1 | ✅ Complete |
| Project 24.1 Part 2 | ✅ Complete |
| Project 24.2 | ✅ Complete |

---

# Module Status

```text
All Module 24 Projects Completed Successfully
```

---

**Author:** Clifford Ferraren  
**Program:** MIT Professional Education – Applied Data Engineering Program  
**Module:** Module 24 – Handling Big Data with Mosquitto, ThingsBoard, and Kafka