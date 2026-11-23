# Video Notes
# Module 24 – Handling Big Data with Mosquitto, ThingsBoard, and Kafka

## Overview

This folder contains study notes and transcript summaries created while completing Module 24.

The material covers three major streaming technologies:

- Mosquitto
- ThingsBoard
- Kafka

The notes were organized to provide a future reference covering:

- Concepts
- Architectures
- Commands
- Configurations
- Rule Chains
- Telemetry Pipelines
- Kafka Producers and Consumers
- Project Implementations

---

# Module Structure

## Section 1
### Mosquitto and MQTT

Topics Covered:

- MQTT Protocol
- Publish / Subscribe Messaging
- Brokers
- Topics
- Clients
- IoT Streaming

Key Concepts:

```text
Publisher
    ↓
Mosquitto Broker
    ↓
Subscriber
```

Videos:

```text
Mini-Lesson 24.1
Mosquitto and MQTT Protocol

Mini-Lesson 24.2
The Paho Library

Videos 24.2–24.3
Using Mosquitto to Stream Data
```

---

# Section 2
### ThingsBoard

Topics Covered:

- Device Management
- Assets
- Rule Engine
- Rule Chains
- Root Rule Chain
- Widgets
- Firebase Integration
- Alarm Processing

Key Architecture:

```text
MQTT Publisher
      ↓
Mosquitto
      ↓
ThingsBoard
      ↓
Firebase
```

Videos:

```text
ThingsBoard and Project 24.1

Getting Started with Firebase

Mini-Lesson 24.3
ThingsBoard Components

Video 24.6
Setting Up a ThingsBoard Environment

Mini-Lesson 24.4
Root Rule Chains

Videos 24.7–24.9
Streaming Data Using ThingsBoard

Video 24.10
ThingsBoard Exercise Solution

Mini-Lesson 24.5
Setting Up Alarms

Videos 24.11–24.12
Alarm Monitoring
```

---

# Section 3
### Kafka

Topics Covered:

- Event Streaming
- Topics
- Producers
- Consumers
- Brokers
- ZooKeeper
- KafkaJS
- Node.js
- Web Servers

Key Architecture:

```text
Producer
    ↓
Topic
    ↓
Broker
    ↓
Consumer
```

Videos:

```text
Kafka and Required Project 24.2

Videos 24.13–24.14
Kafka Overview and Deployment

Mini-Lesson 24.6
Introduction to Node.js

Videos 24.15–24.16
Constructing a Web Server

Mini-Lesson 24.7
Kafka Code Blocks
```

---

# Video Notes Included

## MQTT / Mosquitto

```text
Video_24_02_Mosquitto_and_MQTT_Protocol.md

Video_24_03_The_Paho_Library.md

Video_24_02_24_03_Using_Mosquitto_to_Stream_Data.md
```

---

## ThingsBoard

```text
Video_24_04_ThingsBoard_and_Required_Project_24_01.md

Video_24_04_24_05_Getting_Started_with_Firebase.md

Video_24_06_Mini_Lesson_24_03_ThingsBoard_Components.md

Video_24_06_Setting_Up_a_ThingsBoard_Environment.md

Video_24_07_Mini_Lesson_24_04_Setting_Up_a_Root_Rule_Chain.md

Video_24_07_24_09_Streaming_Data_Using_ThingsBoard.md

Video_24_10_ThingsBoard_Exercise_Solution.md

Video_24_11_Mini_Lesson_24_05_Setting_Up_Alarms_in_ThingsBoard.md

Video_24_11_24_12_Setting_Up_Alarms_in_ThingsBoard_to_Monitor_Data.md
```

---

## Kafka

```text
Video_24_13_Kafka_and_Required_Project_24_02.md

Video_24_13_24_14_Kafka.md

Video_24_15_Mini_Lesson_24_06_Introduction_to_NodeJS.md

Video_24_15_24_16_Constructing_a_Web_Server.md

Video_24_17_Mini_Lesson_24_07_Understanding_Code_Blocks_for_Constructing_a_Web_Server_Using_Kafka.md
```

---

# Practical Projects Referenced

## Project 24.1 Part 1

Streaming Live Data to ThingsBoard

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

---

## Project 24.1 Part 2

Analyzing Live Streaming Data

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

---

## Project 24.2

Constructing a Web Server Using Kafka

Architecture:

```text
Python Producer
      ↓
vehicle-coordinates
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

# Key Technical Lessons Learned

## MQTT

```text
Publish
Subscribe
Broker
Topic
Client
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
REST API Nodes
```

---

## Firebase

```text
Realtime Database
REST APIs
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
Streaming
```

---

## Node.js

```text
KafkaJS
Express
Web Servers
Consumers
```

---

# Important Troubleshooting Topics

## Firebase SSL Trust Issue

Error:

```text
PKIX path building failed

SSLHandshakeException
```

Root Cause:

```text
Sempra Energy Utilities Root Authority SHA2
```

Resolution:

```bash
keytool -importcert
```

into the ThingsBoard Java truststore.

---

## Node-RDKafka Compatibility Issue

Error:

```text
Visual Studio Build Tools Required
```

Resolution:

```text
KafkaJS
```

used instead of:

```text
node-rdkafka
```

---

# Fleet Intelligence Platform Connections

The technologies covered throughout Module 24 align closely with fleet telemetry systems.

Example:

```text
Vehicle GPS Device
        ↓
MQTT / Kafka
        ↓
Broker
        ↓
Processing
        ↓
Storage
        ↓
Dashboard
        ↓
Alerts
```

Potential Use Cases:

```text
Vehicle Tracking

Route Optimization

Fuel Monitoring

Maintenance Alerts

Driver Analytics

Geofencing
```

---

# Module Outcome

This collection of notes provides a complete reference covering:

✅ MQTT

✅ Mosquitto

✅ ThingsBoard

✅ Firebase

✅ Rule Chains

✅ Alarm Workflows

✅ Kafka

✅ Node.js

✅ KafkaJS

✅ Event Streaming

✅ Real-Time Telemetry Processing

✅ End-to-End Streaming Architectures

---

**Author:** Clifford Ferraren  
**Program:** MIT Professional Education – Applied Data Engineering Program  
**Module:** Module 24 – Handling Big Data with Mosquitto, ThingsBoard, and Kafka