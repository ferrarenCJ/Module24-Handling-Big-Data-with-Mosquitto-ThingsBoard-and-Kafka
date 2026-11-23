# Resources
# Module 24 – Handling Big Data with Mosquitto, ThingsBoard, and Kafka

## Overview

This folder contains supporting files, reference materials, troubleshooting notes, configuration files, and external resources used while completing Module 24.

The resources collected here were used to support:

- MQTT and Mosquitto deployments
- ThingsBoard development
- Firebase integrations
- Kafka deployments
- Kafka Producer / Consumer development
- Node.js applications
- SSL troubleshooting
- Docker environments

---

# Resource Categories

## MQTT & Mosquitto Resources

Resources related to:

```text
MQTT Protocol
Mosquitto Broker
Paho MQTT
Docker Deployment
```

Useful References:

```text
https://mqtt.org

https://mosquitto.org
```

Topics:

- MQTT Topics
- Publish / Subscribe
- Brokers
- IoT Messaging

---

## ThingsBoard Resources

Resources related to:

```text
ThingsBoard
Rule Chains
Alarms
Firebase
```

Official Documentation:

```text
https://thingsboard.io/docs/
```

Useful Sections:

```text
Rule Engine

Rule Chains

Action Nodes

Filter Nodes

Alarm Management
```

---

## Firebase Resources

Resources used for:

```text
Realtime Database
REST APIs
Telemetry Storage
Alarm Storage
```

Official Documentation:

```text
https://firebase.google.com/docs
```

Key Topics:

```text
Realtime Database

REST APIs

Database Rules

JSON Structures
```

---

## Kafka Resources

Resources related to:

```text
Kafka
Topics
Producers
Consumers
Confluent Platform
```

Official Documentation:

```text
https://kafka.apache.org/documentation/
```

Additional Resources:

```text
https://confluent.io

https://developer.confluent.io
```

---

## KafkaJS Resources

Used as a replacement for:

```text
node-rdkafka
```

Documentation:

```text
https://kafka.js.org/
```

Key Topics:

```text
Consumers

Producers

Topics

Broker Connections
```

---

## Node.js Resources

Resources related to:

```text
Node.js
Express
Kafka Consumers
```

Official Documentation:

```text
https://nodejs.org
```

Express:

```text
https://expressjs.com
```

---

# Corporate SSL Resources

## Purpose

Resolve SSL trust issues encountered during:

```text
ThingsBoard
     ↓
Firebase
```

integration.

---

# Issue Encountered

Error:

```text
PKIX path building failed

SSLHandshakeException

unable to find valid certification path
```

---

# Root Cause

Corporate SSL inspection introduced:

```text
Sempra Energy Utilities Root Authority SHA2
```

which was not trusted by Java inside the ThingsBoard Docker container.

---

# Files

Example:

```text
SempraRoot.cer
```

Purpose:

```text
Java Truststore Import
```

---

# SSL Resolution Procedure

## Copy Certificate

```cmd
docker cp SempraRoot.cer thingsboard-mytb-1:/tmp/
```

---

## Import Certificate

```bash
keytool -importcert \
-alias sempra-root \
-file /tmp/SempraRoot.cer \
-keystore /usr/lib/jvm/java-17-openjdk-amd64/lib/security/cacerts \
-storepass changeit \
-noprompt
```

---

## Restart ThingsBoard

```cmd
docker restart thingsboard-mytb-1
```

Result:

```text
Firebase Connectivity Restored
```

---

# Kafka Compatibility Resources

## Problem

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

# Solution

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

Benefits:

✅ Pure JavaScript

✅ No Native Compilation

✅ No Visual Studio Dependency

✅ Modern Kafka Support

---

# Helpful Commands

## Docker

List containers:

```cmd
docker ps
```

---

View logs:

```cmd
docker logs <container>
```

---

Restart container:

```cmd
docker restart <container>
```

---

# MQTT

Install Paho:

```cmd
pip install "paho-mqtt<2.0.0"
```

---

# Kafka

Install Producer Library:

```cmd
pip install kafka-python
```

---

# Node.js

Install dependencies:

```cmd
npm install
```

Install KafkaJS:

```cmd
npm install kafkajs
```

---

# Firebase

Manual write test:

```cmd
curl -k -X PUT ^
-H "Content-Type: application/json" ^
-d "{\"alarmTriggered\":true}" ^
"https://<project>.firebaseio.com/alarm.json"
```

---

# Learning Resources Used

## Apache Kafka

```text
https://kafka.apache.org/documentation/
```

Used for:

```text
Topics

Producers

Consumers

Kafka Architecture
```

---

## KafkaJS

```text
https://kafka.js.org/
```

Used for:

```text
Kafka Consumer Development

Node.js Integration
```

---

## ThingsBoard

```text
https://thingsboard.io/docs/
```

Used for:

```text
Rule Chains

Alarm Nodes

REST API Nodes
```

---

## Node.js

```text
https://nodejs.org
```

Used for:

```text
Server Development

Express Applications
```

---

# Resource Purpose

This directory serves as a reference library for:

```text
Streaming Data

IoT Architectures

Telemetry Pipelines

Event Streaming

Docker Deployments

Enterprise Troubleshooting
```

and should be expanded as new technologies and projects are completed.

---

# Module 24 Topics Supported

✅ MQTT

✅ Mosquitto

✅ ThingsBoard

✅ Firebase

✅ Rule Chains

✅ Alarm Processing

✅ Kafka

✅ KafkaJS

✅ Node.js

✅ Docker

✅ SSL Troubleshooting

✅ Event Streaming

---

**Author:** Clifford Ferraren  
**Program:** MIT Professional Education – Applied Data Engineering Program  
**Module:** Module 24 – Handling Big Data with Mosquitto, ThingsBoard, and Kafka