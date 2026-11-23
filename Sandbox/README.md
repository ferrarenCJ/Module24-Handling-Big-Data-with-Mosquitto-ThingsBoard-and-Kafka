# Sandbox
# Module 24 – Handling Big Data with Mosquitto, ThingsBoard, and Kafka

## Overview

The Sandbox folder contains experimental code, testing scripts, troubleshooting work, temporary files, and proof-of-concept implementations created while completing Module 24.

The purpose of the Sandbox is to:

- Test code before moving it into assignments
- Validate configurations
- Troubleshoot connectivity issues
- Experiment with producers and consumers
- Verify Firebase integrations
- Validate Kafka topics
- Perform SSL troubleshooting
- Store temporary test scripts

---

# Purpose of a Sandbox

A sandbox environment provides a safe workspace where code can be executed without affecting:

```text
Production Code

Assignment Deliverables

Final Project Artifacts
```

The Sandbox should be considered:

```text
Temporary
Experimental
Disposable
```

while assignment folders should contain finalized solutions.

---

# Technologies Tested

## MQTT

Examples:

```text
MQTT Topics

Publisher Tests

Subscriber Tests
```

---

## Mosquitto

Examples:

```text
Broker Connectivity

Docker Validation

Message Routing
```

---

## ThingsBoard

Examples:

```text
Rule Chain Testing

Alarm Testing

REST API Nodes

Firebase Connectivity
```

---

## Firebase

Examples:

```text
REST API Validation

Manual Data Writes

JSON Structure Testing
```

---

## Kafka

Examples:

```text
Producer Validation

Topic Testing

Consumer Debugging

KafkaJS Experiments
```

---

## Node.js

Examples:

```text
Server Testing

Consumer Testing

Express Routing

Package Validation
```

---

# Common Sandbox Activities

## Generate Test Telemetry

Example:

```json
{
    "temperature": 76,
    "humidity": 88
}
```

---

## Generate Test GPS Coordinates

Example:

```json
{
    "longitude": -118,
    "latitude": 34
}
```

---

## Verify Firebase Writes

Example:

```cmd
curl -k -X PUT ^
-H "Content-Type: application/json" ^
-d "{\"alarmTriggered\":true}" ^
"https://module24project-xxxxx.firebaseio.com/alarm.json"
```

---

## Verify Kafka Producer

```cmd
python PublishVehicleCoordinates.py
```

---

## Verify Kafka Consumer

```cmd
node server.js
```

---

# SSL Troubleshooting

One of the most important troubleshooting exercises completed during Module 24 involved resolving Firebase SSL trust issues.

Error:

```text
PKIX path building failed

SSLHandshakeException
```

---

## Root Cause

Corporate TLS inspection certificate:

```text
Sempra Energy Utilities Root Authority SHA2
```

was not trusted by Java running inside Docker.

---

## Resolution

```bash
keytool -importcert
```

used to import the certificate into the Java truststore.

This process should be preserved for future Firebase integration work.

---

# Kafka Troubleshooting

## Problem

```text
node-rdkafka
```

required:

```text
Visual Studio Build Tools

Desktop Development with C++
```

which were unavailable.

---

## Resolution

Installed:

```cmd
npm install kafkajs
```

and migrated consumer code to:

```javascript
const { Kafka } = require('kafkajs');
```

---

# Suggested Sandbox Contents

Examples:

```text
temp.py

firebase_test.py

mqtt_test.py

kafka_test.py

consumer_test.js

producer_test.js

ssl_test.md
```

---

# Best Practices

✅ Test changes in Sandbox first

✅ Keep assignment deliverables separate

✅ Document troubleshooting steps

✅ Save reusable scripts

✅ Remove obsolete experiments periodically

---

# Module 24 Relationship

The Sandbox supported:

```text
Project 24.1 Part 1

Project 24.1 Part 2

Project 24.2
```

by providing an isolated environment for experimentation and troubleshooting before changes were applied to project deliverables.

---

# Status

```text
Sandbox Ready for Future Experiments
```

---

**Author:** Clifford Ferraren  
**Program:** MIT Professional Education – Applied Data Engineering Program  
**Module:** Module 24 – Handling Big Data with Mosquitto, ThingsBoard, and Kafka