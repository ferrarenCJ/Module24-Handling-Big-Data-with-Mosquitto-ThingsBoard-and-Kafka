# Videos
# Module 24 – Handling Big Data with Mosquitto, ThingsBoard, and Kafka

## Overview

This folder contains structured notes, transcript summaries, key concepts, architectures, implementation details, and project walkthroughs derived from the Module 24 video lessons.

These notes were created to serve as a long-term reference for:

- MQTT Messaging
- Mosquitto
- ThingsBoard
- Firebase
- Alarm Processing
- Kafka
- Node.js
- Producer / Consumer Architectures
- Event Streaming Systems

---

# Module 24 Learning Path

The module was organized into three major sections:

```text
Mosquitto
      ↓
ThingsBoard
      ↓
Kafka
```

Each section progressively expanded the streaming architecture from IoT messaging to enterprise-scale event streaming.

---

# Section 1 – Mosquitto and MQTT

## Topics Covered

- MQTT Protocol
- Publish / Subscribe Messaging
- Topics
- Brokers
- MQTT Clients
- Paho Library
- Mosquitto Docker Deployment

---

## Key Architecture

```text
Publisher
     ↓
MQTT Topic
     ↓
Mosquitto Broker
     ↓
Subscriber
```

---

## Videos and Lessons

### Mini-Lesson 24.1

```text
Mosquitto and MQTT Protocol
```

Topics:

- MQTT Fundamentals
- Brokers
- Topics
- Publish / Subscribe

---

### Mini-Lesson 24.2

```text
The Paho Library
```

Topics:

- Paho Client
- MQTT Connections
- Publishing
- Subscribing

---

### Videos 24.2 – 24.3

```text
Using Mosquitto to Stream Data
```

Topics:

- Mosquitto Docker Container
- Message Publishing
- Message Consumption

---

# Section 2 – ThingsBoard

## Topics Covered

- Device Management
- Assets
- Telemetry
- Rule Chains
- Firebase
- Alarms
- Dashboards
- Widgets

---

## Telemetry Architecture

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

## Videos and Lessons

### ThingsBoard and Required Project 24.1

Topics:

```text
Project Overview
Firebase Integration
Telemetry Pipelines
```

---

### Videos 24.4 – 24.5

```text
Getting Started with Firebase
```

Topics:

```text
Firebase Project Creation
Realtime Database
ThingsBoard Installation
```

---

### Mini-Lesson 24.3

```text
ThingsBoard Components
```

Topics:

```text
Devices
Assets
Rule Engine
Rule Chains
Root Rule Chain
```

---

### Video 24.6

```text
Setting Up a ThingsBoard Environment
```

Topics:

```text
Telemetry Generation
Thermostat Simulation
Rule Chains
```

---

### Mini-Lesson 24.4

```text
Setting Up a Root Rule Chain
```

Topics:

```text
Input Nodes
Message Type Switch
Save Timeseries
Rule Chain Integration
```

---

### Videos 24.7 – 24.9

```text
Streaming Data Using ThingsBoard
```

Topics:

```text
Widgets
Firebase Integration
Telemetry Visualization
```

---

### Video 24.10

```text
ThingsBoard Exercise Solution
```

Topics:

```text
Project 24.1 Part 1
Temperature Data
Humidity Data
Firebase Storage
```

---

### Mini-Lesson 24.5

```text
Setting Up Alarms in ThingsBoard
```

Topics:

```text
CreateAlarm
ClearAlarm
Threshold Monitoring
Alarm Rule Chains
```

---

### Videos 24.11 – 24.12

```text
Setting Up Alarms in ThingsBoard
```

Topics:

```text
Alarm Monitoring
AlarmToFirebase
TempToFirebase
Rule Chain Integration
```

---

# Section 3 – Kafka

## Topics Covered

- Event Streaming
- Kafka Topics
- Producers
- Consumers
- Brokers
- KafkaJS
- Node.js
- Web Servers

---

## Kafka Architecture

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

## Videos and Lessons

### Kafka and Required Project 24.2

Topics:

```text
Kafka Overview
Project Introduction
Producer / Consumer Design
```

---

### Videos 24.13 – 24.14

```text
Kafka Overview and Installation
```

Topics:

```text
Kafka Architecture
Confluent Platform
Docker Deployment
```

---

### Mini-Lesson 24.6

```text
Introduction to Node.js
```

Topics:

```text
Node.js
Express
Web Servers
```

---

### Videos 24.15 – 24.16

```text
Constructing a Web Server
```

Topics:

```text
Node.js Installation
Kafka Consumer Architecture
Streaming Applications
```

---

### Mini-Lesson 24.7

```text
Understanding Kafka Code Blocks
```

Topics:

```text
Producer Development
Consumer Development
Kafka Topics
Message Flow
```

---

# Projects Referenced

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

Outcome:

✅ Temperature Telemetry

✅ Humidity Telemetry

✅ Firebase Storage

---

## Project 24.1 Part 2

### Analyzing Live Streaming Data Using ThingsBoard

Architecture:

```text
Root Rule Chain
       ↓
CreateAndClearAlarms
       ↓
AlarmToFirebase
       ↓
Firebase
```

Outcome:

✅ Alarm Generation

✅ Alarm Monitoring

✅ Firebase Alarm Storage

---

## Project 24.2

### Constructing a Web Server Using Kafka

Architecture:

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

Outcome:

✅ Producer

✅ Consumer

✅ Web Server

✅ Real-Time Streaming

---

# Major Technical Lessons

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
Rule Chains
CreateAlarm
ClearAlarm
REST API Nodes
Firebase Integration
```

---

## Kafka

```text
Producer
Consumer
Topic
Broker
Partition
```

---

## Node.js

```text
Express
KafkaJS
Web Servers
```

---

# Troubleshooting Highlights

## Firebase SSL Trust Issue

Error:

```text
PKIX path building failed
```

Resolution:

```bash
keytool -importcert
```

Imported:

```text
Sempra Energy Utilities Root Authority SHA2
```

into the Java truststore.

---

## node-rdkafka Compatibility Issue

Issue:

```text
Visual Studio Build Tools Required
```

Resolution:

```text
KafkaJS
```

replaced:

```text
node-rdkafka
```

allowing the Kafka consumer to function without native compilation.

---

# Fleet Intelligence Platform Relevance

Module 24 technologies directly support modern fleet telemetry systems.

Example:

```text
Vehicle Device
      ↓
MQTT / Kafka
      ↓
Broker
      ↓
Processing Layer
      ↓
Storage
      ↓
Dashboards
      ↓
Alerts
```

Potential Solutions:

```text
Vehicle Tracking

Fuel Monitoring

Route Optimization

Driver Analytics

Maintenance Alerts

Geofencing
```

---

# Module 24 Outcome

The video notes collectively provide a complete reference for:

✅ MQTT

✅ Mosquitto

✅ ThingsBoard

✅ Firebase

✅ Rule Chains

✅ Alarm Workflows

✅ Kafka

✅ KafkaJS

✅ Node.js

✅ Docker

✅ Event Streaming

✅ Enterprise Troubleshooting

---

## Video Notes Status

```text
All Module 24 Video Notes Completed
```

---

**Author:** Clifford Ferraren  
**Program:** MIT Professional Education – Applied Data Engineering Program  
**Module:** Module 24 – Handling Big Data with Mosquitto, ThingsBoard, and Kafka