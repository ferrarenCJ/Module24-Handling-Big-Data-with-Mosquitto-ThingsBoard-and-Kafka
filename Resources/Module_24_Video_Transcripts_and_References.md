# Module 24: Video Transcripts and References

## Module 24
### Handling Big Data with Mosquitto, ThingsBoard, and Kafka

---

# Overview

This document serves as a centralized reference for all Module 24 transcripts, supporting resources, documentation, and references used throughout the module.

Module 24 focused on:

- Mosquitto
- MQTT
- ThingsBoard
- Firebase
- Kafka
- Node.js
- Event Streaming
- Telemetry Processing
- Alarm Workflows
- Producer / Consumer Architectures

The transcripts and references provide additional context, technical explanations, and implementation details beyond the video lessons.

---

# Module Resources

## Module 24 Transcript

Provides the complete transcript for all video content included in Module 24.

### Resource

```text
Module 24 Transcript
```

### Purpose

Used for:

- Reviewing lectures
- Searching topics
- Clarifying concepts
- Studying for knowledge checks
- Supporting project work

### Topics Covered

```text
Mosquitto
MQTT
ThingsBoard
Firebase
Kafka
Node.js
Producer / Consumer Architectures
```

---

# Module References

## Module 24 References

Provides the official list of references cited throughout the module.

### Purpose

Used for:

- Further learning
- Technical research
- Industry documentation
- Professional reference material

---

# Major Technologies Referenced

## MQTT

### Purpose

Lightweight messaging protocol designed for:

```text
IoT Devices
Sensors
Telemetry
Real-Time Messaging
```

Architecture:

```text
Publisher
     ↓
 Broker
     ↓
Subscriber
```

---

## Mosquitto

### Purpose

Open-source MQTT broker.

Responsibilities:

```text
Message Routing

Topic Management

Publish / Subscribe
```

---

## ThingsBoard

### Purpose

Open-source IoT platform used for:

```text
Telemetry Processing

Device Management

Dashboards

Rule Chains

Alarm Workflows
```

---

## Firebase

### Purpose

Google cloud platform used for:

```text
Realtime Databases

Telemetry Storage

Alarm Storage
```

---

## Kafka

### Purpose

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
Real-Time Analytics

Large Scale Streaming

Telemetry Systems

Event Processing
```

---

## Node.js

### Purpose

Server-side JavaScript runtime.

Used for:

```text
Kafka Consumers

Web Servers

Streaming Applications
```

Powered by:

```text
Google Chrome V8 Engine
```

---

# Module Projects Referenced

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

✅ Temperature Telemetry

✅ Humidity Telemetry

✅ Firebase Integration

---

## Project 24.1 Part 2

### Analyzing Live Streaming Data Using ThingsBoard

Architecture:

```text
Telemetry
      ↓
CreateAndClearAlarms
      ↓
AlarmToFirebase
      ↓
Firebase
```

Completed:

✅ Alarm Processing

✅ Alarm Monitoring

✅ Firebase Alarm Storage

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
Node.js Server
       ↓
Browser
```

Completed:

✅ Producer

✅ Consumer

✅ Kafka Topic

✅ Web Server

✅ Streaming Vehicle Coordinates

---

# Key Concepts Reinforced

## MQTT

```text
Publish
Subscribe
Broker
Topic
```

---

## ThingsBoard

```text
Devices

Assets

Rule Chains

Root Rule Chain

CreateAlarm

ClearAlarm
```

---

## Firebase

```text
REST API

Realtime Database

Telemetry Storage

Alarm Storage
```

---

## Kafka

```text
Producer

Consumer

Topic

Broker

Partition

Cluster
```

---

## Node.js

```text
Web Servers

Express

KafkaJS

Streaming Applications
```

---

# Additional Learning Recommendations

## Apache Kafka Documentation

```text
https://kafka.apache.org/documentation/
```

Used for:

```text
Topics

Producers

Consumers

Broker Architecture
```

---

## KafkaJS Documentation

```text
https://kafka.js.org/
```

Used for:

```text
Kafka Client Development

Consumer Implementations
```

---

## ThingsBoard Documentation

```text
https://thingsboard.io/docs/
```

Used for:

```text
Rule Chains

Alarm Nodes

REST API Nodes

IoT Architectures
```

---

## Node.js Documentation

```text
https://nodejs.org
```

Used for:

```text
JavaScript Runtime

Web Servers

Application Development
```

---

# Module 24 Learning Outcomes

Successfully achieved:

✅ Understand MQTT and Mosquitto

✅ Configure ThingsBoard Environments

✅ Create Rule Chains

✅ Implement Alarm Workflows

✅ Integrate Firebase

✅ Build Kafka Producers

✅ Build Kafka Consumers

✅ Create Streaming Web Servers

✅ Process Real-Time Telemetry

✅ Troubleshoot Enterprise Integration Issues

---

# Module Status

```text
Module 24 Completed
```

Projects Completed:

✅ Project 24.1 Part 1

✅ Project 24.1 Part 2

✅ Project 24.2

---

**Author:** Clifford Ferraren  
**Program:** MIT Professional Education – Applied Data Engineering Program  
**Module:** Module 24 – Handling Big Data with Mosquitto, ThingsBoard, and Kafka