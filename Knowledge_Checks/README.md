# Knowledge Checks
# Module 24 – Handling Big Data with Mosquitto, ThingsBoard, and Kafka

## Overview

This folder contains the completed knowledge check reviews for Module 24.

The knowledge checks reinforced the key concepts, architectures, terminology, and practical applications related to:

- Mosquitto
- MQTT
- ThingsBoard
- Firebase
- Kafka
- Node.js
- Event Streaming
- Producer / Consumer Architectures

Each knowledge check has been summarized with explanations, correct answers, and supporting notes for future reference.

---

# Knowledge Checks Included

## Self-Study Knowledge Check 24.1
### Mosquitto

**File**

```text
SKC_24_01_Mosquitto.md
```

---

### Topics Covered

- MQTT Protocol
- Mosquitto Broker
- Publish / Subscribe Architecture
- Paho MQTT Library
- MQTT Topics
- MQTT Clients

---

### Key Concepts

#### MQTT

```text
Message Queuing Telemetry Transport
```

Purpose:

```text
IoT Messaging
Telemetry
Streaming Data
```

---

#### Publish / Subscribe

```text
Publisher
    ↓
Mosquitto Broker
    ↓
Subscriber
```

---

#### Paho

Python MQTT Client Library

Installation:

```cmd
pip install "paho-mqtt<2.0.0"
```

---

### Score

```text
6 / 6 Correct
```

---

# Self-Study Knowledge Check 24.2
### ThingsBoard

**File**

```text
SKC_24_02_ThingsBoard.md
```

---

### Topics Covered

- ThingsBoard Components
- Devices
- Assets
- Rule Engine
- Rule Chains
- Root Rule Chain
- Alarms

---

### Key Concepts

#### Device

```text
Telemetry Source
```

Examples:

```text
Temperature Sensor

Humidity Sensor

GPS Tracker
```

---

#### Asset

```text
Container for Devices
```

Examples:

```text
Building

Facility

Vehicle
```

---

#### Rule Chain

```text
Logical Collection
of Processing Nodes
```

---

#### Root Rule Chain

Primary telemetry workflow.

---

#### Alarm

Threshold-based notification system.

Example:

```text
Temperature > 20°C
```

---

### Score

```text
8 / 8 Correct
```

---

# Self-Study Knowledge Check 24.3
### Kafka

**File**

```text
SKC_24_03_Kafka.md
```

---

### Topics Covered

- Kafka Architecture
- Topics
- Producers
- Consumers
- Event Streaming
- Node.js

---

### Key Concepts

#### Kafka

```text
Distributed Publish / Subscribe
Messaging System
```

Purpose:

```text
Process Big Data Streams
at Scale
```

---

#### Producer

Writes records to Kafka.

Example:

```json
{
    "latitude": 33.875,
    "longitude": -118.090
}
```

---

#### Consumer

Reads records from Kafka.

Example:

```text
Node.js Application
```

---

#### Topic

Communication channel.

Example:

```text
vehicle-coordinates
```

---

#### Broker

Stores and distributes messages.

---

#### Node.js

Uses:

```text
Google Chrome V8 Engine
```

---

### Score

```text
6 / 6 Correct
```

---

# Technology Summary

## Mosquitto

Purpose:

```text
MQTT Broker
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

## ThingsBoard

Purpose:

```text
IoT Platform
```

Capabilities:

```text
Telemetry Processing

Visualization

Rule Chains

Alarm Processing
```

---

## Firebase

Purpose:

```text
Realtime Cloud Storage
```

Used For:

```text
Telemetry Data

Alarm Data
```

---

## Kafka

Purpose:

```text
Enterprise Event Streaming
```

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

---

## Node.js

Purpose:

```text
Web Applications

Kafka Consumers

Web Servers
```

---

# Module 24 Learning Outcomes

Knowledge checks reinforced the ability to:

✅ Understand MQTT and Mosquitto architectures

✅ Configure ThingsBoard telemetry processing

✅ Understand Rule Chains and Alarms

✅ Identify Kafka components

✅ Build Producer / Consumer mental models

✅ Understand event-streaming architectures

✅ Connect telemetry systems with cloud storage platforms

---

# Fleet Intelligence Platform Connections

The concepts reviewed directly support future fleet telemetry solutions.

Example:

```text
Vehicle GPS
       ↓
Producer
       ↓
Topic
       ↓
Broker
       ↓
Consumer
       ↓
Fleet Dashboard
```

Potential telemetry:

```json
{
    "vehicle_id": "SCG001",
    "latitude": 33.875,
    "longitude": -118.090,
    "speed": 58,
    "fuel_level": 72
}
```

Potential alarms:

```text
Overspeed

Low Fuel

Vehicle Offline

Geofence Violation
```

---

# Knowledge Check Status

```text
SKC 24.1 - Mosquitto    ✅ Complete

SKC 24.2 - ThingsBoard  ✅ Complete

SKC 24.3 - Kafka        ✅ Complete
```

---

# Overall Performance

| Knowledge Check | Result |
|-----------------|---------|
| Mosquitto | ✅ 100% |
| ThingsBoard | ✅ 100% |
| Kafka | ✅ 100% |

---

**Author:** Clifford Ferraren  
**Program:** MIT Professional Education – Applied Data Engineering Program  
**Module:** Module 24 – Handling Big Data with Mosquitto, ThingsBoard, and Kafka