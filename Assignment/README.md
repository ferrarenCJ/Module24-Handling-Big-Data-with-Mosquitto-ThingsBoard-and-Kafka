# Module 24 Assignments
# Handling Big Data with Mosquitto, ThingsBoard, and Kafka

## MIT Professional Education
### Applied Data Engineering Program

---

# Module Overview

Module 24 focused on building real-time streaming architectures using:

- Mosquitto
- MQTT
- ThingsBoard
- Firebase
- Kafka
- Node.js
- Docker

The module consisted of three major projects that progressively expanded the architecture from simple MQTT messaging to enterprise-scale event streaming.

---

# Assignment Summary

## Required Project 24.1 (Part 1)
### Streaming Live Data to ThingsBoard

**Objective**

Create an end-to-end IoT telemetry pipeline capable of generating, transmitting, processing, visualizing, and storing real-time temperature and humidity data.

---

### Technologies Used

- Python
- Paho MQTT
- Mosquitto
- MQTT
- Docker
- ThingsBoard
- Firebase Realtime Database

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

### Deliverables Completed

✅ Mosquitto Docker Deployment

✅ MQTT Publisher

✅ Temperature Telemetry

✅ Humidity Telemetry

✅ ThingsBoard Integration

✅ Firebase Integration

✅ Real-Time Telemetry Visualization

---

# Required Project 24.1 (Part 2)
### Analyzing Live Streaming Data Using ThingsBoard

---

## Objective

Extend the telemetry architecture from Part 1 by implementing alarm monitoring and automated event processing.

---

### Technologies Used

- ThingsBoard Rule Engine
- Alarm Rule Chains
- Firebase Realtime Database
- MQTT
- Mosquitto

---

### Architecture

```text
MQTT Publisher
      ↓
Mosquitto
      ↓
ThingsBoard
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

### Deliverables Completed

✅ CreateAndClearAlarms Rule Chain

✅ AlarmToFirebase Rule Chain

✅ TempToFirebase Rule Chain

✅ Alarm Generation

✅ Alarm Monitoring

✅ Firebase Alarm Integration

✅ Real-Time Alarm Processing

---

## Major Issue Resolved

### Corporate SSL Trust Store Problem

During Firebase integration:

```text
ThingsBoard
      ↓
Firebase
```

failed with:

```text
PKIX path building failed

SSLHandshakeException

unable to find valid certification path
```

---

### Root Cause

The corporate SSL inspection environment replaced Firebase certificates with:

```text
Sempra Energy Utilities Root Authority SHA2
```

which was not trusted by Java inside the ThingsBoard Docker container.

---

### Resolution

Exported:

```text
Sempra Energy Utilities Root Authority SHA2
```

and imported it into the Java truststore:

```bash
keytool -importcert \
-alias sempra-root \
-file /tmp/SempraRoot.cer \
-keystore /usr/lib/jvm/java-17-openjdk-amd64/lib/security/cacerts \
-storepass changeit \
-noprompt
```

Result:

✅ Firebase telemetry writes restored

✅ Alarm data successfully written to Firebase

---

# Required Project 24.2
### Constructing a Web Server Using Kafka

---

## Objective

Build a Kafka-based producer-consumer architecture capable of streaming vehicle location data through a Kafka broker and displaying consumed messages through a Node.js web application.

---

### Technologies Used

- Kafka
- Confluent Platform
- Docker
- Python
- KafkaJS
- Node.js
- Express

---

### Architecture

```text
PublishVehicleCoordinates.py
            ↓
      Kafka Producer
            ↓
vehicle-coordinates Topic
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

### Deliverables Completed

✅ Confluent Kafka Deployment

✅ Kafka Topic Creation

✅ Vehicle Coordinate Producer

✅ Kafka Consumer

✅ Node.js Web Server

✅ Browser Integration

✅ Real-Time Message Consumption

---

## Major Compatibility Issue Resolved

### node-rdkafka Installation Failure

Course materials expected:

```text
node-rdkafka
```

but installation failed because:

```text
Visual Studio Build Tools
Desktop Development with C++
node-gyp
```

were unavailable.

---

### Resolution

Replaced:

```text
node-rdkafka
```

with:

```text
KafkaJS
```

Installation:

```cmd
npm install kafkajs
```

Result:

✅ Kafka Consumer Operational

✅ Node.js Web Server Functional

✅ No Visual Studio Dependency

✅ Kafka Messages Successfully Consumed

---

# Skills Demonstrated

Throughout Module 24 the following skills were successfully demonstrated:

---

## MQTT & Mosquitto

✅ Publish / Subscribe Architecture

✅ Telemetry Generation

✅ Broker Configuration

✅ MQTT Clients

---

## ThingsBoard

✅ Device Management

✅ Rule Chains

✅ Widgets

✅ Telemetry Processing

✅ Alarm Processing

✅ Firebase Integration

---

## Firebase

✅ Realtime Database

✅ REST API Integration

✅ Alarm Storage

✅ Telemetry Storage

---

## Kafka

✅ Kafka Topics

✅ Producers

✅ Consumers

✅ Brokers

✅ KafkaJS

✅ Node.js Integration

---

## Docker

✅ Multi-Container Deployments

✅ Kafka Clusters

✅ Mosquitto Infrastructure

✅ ThingsBoard Infrastructure

---

## Troubleshooting

✅ SSL Certificate Chains

✅ Java Truststores

✅ Corporate TLS Inspection

✅ Node.js Dependency Issues

✅ Kafka Client Compatibility

---

# Fleet Intelligence Platform Connections

Module 24 directly aligns with real-world fleet telemetry systems.

Example architecture:

```text
Vehicle GPS Devices
          ↓
 MQTT / Kafka
          ↓
 Brokers
          ↓
 Processing Engines
          ↓
 Dashboards
          ↓
 Alerts
```

Potential future applications:

```text
Vehicle Tracking

Route Optimization

Fuel Monitoring

Driver Behavior Analytics

Geofencing

Maintenance Alerts

Predictive Analytics
```

---

# Projects Completed

| Project | Status |
|----------|--------|
| Required Project 24.1 Part 1 | ✅ Complete |
| Required Project 24.1 Part 2 | ✅ Complete |
| Required Project 24.2 | ✅ Complete |

---

# Module 24 Status

```text
ALL REQUIRED ASSIGNMENTS COMPLETED
```

---

**Author:** Clifford Ferraren  
**Program:** MIT Professional Education – Applied Data Engineering Program  
**Module:** Module 24 – Handling Big Data with Mosquitto, ThingsBoard, and Kafka