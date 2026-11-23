# Module 24
# Handling Big Data with Mosquitto, ThingsBoard, and Kafka

## MIT Professional Education
### Applied Data Engineering Program

---

# Module Overview

Module 24 focused on designing, building, monitoring, and consuming real-time streaming data pipelines using three major technologies:

- Mosquitto
- ThingsBoard
- Kafka

The module progressed through three increasingly sophisticated streaming architectures:

```text
MQTT + Mosquitto
        ↓
ThingsBoard + Firebase
        ↓
Kafka + Node.js
```

Students learned how to:

- Generate telemetry data
- Build streaming pipelines
- Process real-time events
- Monitor data using alarms
- Store telemetry in the cloud
- Construct Kafka producer/consumer systems
- Build a web server for streaming applications

---

# Repository Structure

```text
Module_24_Handling_Big_Data
│
├── Assignment
├── Cheat_Sheets
├── Coding_Activities
├── Discussions
├── Knowledge_Checks
├── Resources
├── Sandbox
├── Videos
└── README.md
```

---

# Section 1
# Mosquitto and MQTT

## Technologies

- MQTT
- Mosquitto
- Paho MQTT
- Docker

---

## Concepts Learned

### MQTT

Message Queuing Telemetry Transport

Purpose:

```text
Lightweight IoT Messaging
```

Architecture:

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

### Mosquitto

Open-source MQTT broker.

Responsibilities:

```text
Message Routing
Topic Management
Publish / Subscribe
Telemetry Distribution
```

---

### Paho MQTT

Python MQTT client library.

Installation:

```cmd
pip install "paho-mqtt<2.0.0"
```

---

## Skills Developed

✅ MQTT Publishers

✅ MQTT Subscribers

✅ Topic Subscriptions

✅ Mosquitto Docker Deployment

✅ Telemetry Streaming

---

# Section 2
# ThingsBoard and Firebase

## Technologies

- ThingsBoard
- Firebase
- MQTT
- Mosquitto
- Docker

---

## Concepts Learned

### Devices

Telemetry producing entities.

Examples:

```text
Temperature Sensor

Humidity Sensor

GPS Device
```

---

### Assets

Containers for devices.

Examples:

```text
Building

Facility

Vehicle
```

---

### Rule Engine

Responsible for:

```text
Processing
Filtering
Routing
Transformation
```

---

### Rule Chains

Logical workflows used to process telemetry.

Example:

```text
Input
      ↓
Filter
      ↓
Storage
      ↓
Alerting
```

---

### Root Rule Chain

Primary processing workflow inside ThingsBoard.

---

### Widgets

Used to visualize telemetry.

Examples:

```text
Timeseries Charts

Gauges

Tables

Maps
```

---

### Alarms

Used to monitor telemetry and trigger actions.

Example:

```text
Temperature > Threshold
```

---

## Firebase

Used as a cloud-hosted:

```text
Realtime Database
```

for:

```text
Telemetry Storage
Alarm Storage
```

---

# Required Project 24.1 (Part 1)

## Streaming Live Data to ThingsBoard

### Objective

Create a complete telemetry pipeline.

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

### Deliverables

✅ Temperature Telemetry

✅ Humidity Telemetry

✅ Firebase Integration

✅ ThingsBoard Visualization

---

# Required Project 24.1 (Part 2)

## Analyzing Live Streaming Data Using ThingsBoard

### Objective

Build alarm-processing workflows.

---

### Architecture

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

---

### Deliverables

✅ Alarm Rule Chains

✅ Real-Time Alarm Processing

✅ Firebase Alarm Storage

✅ Telemetry Monitoring

---

# Major Technical Challenge

## Firebase SSL Trust Issue

### Error

```text
PKIX path building failed

SSLHandshakeException
```

---

### Root Cause

Corporate SSL inspection replaced Firebase certificates with:

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

then imported into Java truststore:

```bash
keytool -importcert \
-alias sempra-root \
-file /tmp/SempraRoot.cer \
-keystore /usr/lib/jvm/java-17-openjdk-amd64/lib/security/cacerts \
-storepass changeit \
-noprompt
```

Result:

✅ Firebase Connectivity Restored

✅ Alarm Data Generated

✅ Telemetry Data Stored

---

# Section 3
# Kafka and Node.js

## Technologies

- Kafka
- Confluent Platform
- KafkaJS
- Node.js
- Express
- Docker

---

## Concepts Learned

### Producer

Publishes events.

Example:

```json
{
    "longitude": 127,
    "latitude": 50
}
```

---

### Topic

Communication channel.

Example:

```text
vehicle-coordinates
```

---

### Broker

Stores and distributes Kafka messages.

---

### Consumer

Reads Kafka messages.

---

### Kafka Architecture

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

### Node.js

Used to build:

```text
Web Applications
Kafka Consumers
Web Servers
```

---

# Required Project 24.2

## Constructing a Web Server Using Kafka

### Objective

Build a producer/consumer architecture using Kafka.

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

### Deliverables

✅ Kafka Cluster Deployment

✅ Topic Creation

✅ Python Producer

✅ Kafka Consumer

✅ Node.js Server

✅ Web Application

✅ Real-Time Streaming

---

# Major Technical Challenge

## node-rdkafka Compatibility Issue

The course material relied upon:

```text
node-rdkafka
```

which required:

```text
Visual Studio Build Tools

Desktop Development with C++

node-gyp
```

and failed under:

```text
Node.js v22.23.5
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

✅ Kafka Consumer Functional

✅ No Native Compilation Required

✅ No Visual Studio Dependency

---

# Coding Activities

## Mosquitto

```text
Publisher
Subscriber
```

---

## ThingsBoard

```text
Project_24_1_Part_1

Project_24_1_Part_2
```

---

## Kafka

```text
Producer

Consumer

Web_Server
```

---

# Knowledge Checks

Completed:

```text
SKC 24.1 – Mosquitto

SKC 24.2 – ThingsBoard

SKC 24.3 – Kafka
```

Result:

```text
100% Completion
```

---

# Discussions

Completed:

```text
Discussion 24.1
Use Cases for Mosquitto

Discussion 24.2
Use Cases for ThingsBoard

Discussion 24.3
Use Cases for Kafka

Self-Study Discussion 24.1
Handling Big Data
```

---

# Cheat Sheets

Created:

```text
Module 24 Cheat Sheet

Kafka Producer Consumer Reference
```

Topics Covered:

```text
MQTT

ThingsBoard

Firebase

Kafka

Node.js

Docker

SSL Troubleshooting
```

---

# Key Skills Developed

✅ MQTT Messaging

✅ Publish / Subscribe Architectures

✅ Docker Deployments

✅ Telemetry Processing

✅ Rule Chains

✅ Alarm Workflows

✅ Firebase Integration

✅ Kafka Streaming

✅ Producers

✅ Consumers

✅ Node.js Web Servers

✅ KafkaJS

✅ Event Streaming

✅ SSL Troubleshooting

✅ Enterprise System Integration

---

# Fleet Intelligence Platform Connections

The technologies covered throughout Module 24 directly support future fleet telemetry architectures.

Example:

```text
Vehicle GPS Device
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

Potential Applications:

```text
Vehicle Tracking

Fuel Monitoring

Route Optimization

Driver Analytics

Geofencing

Maintenance Alerts

Predictive Maintenance
```

---

# Module Deliverables Completed

| Deliverable | Status |
|-------------|---------|
| Project 24.1 Part 1 | ✅ Complete |
| Project 24.1 Part 2 | ✅ Complete |
| Project 24.2 | ✅ Complete |
| All Discussions | ✅ Complete |
| All Knowledge Checks | ✅ Complete |
| All Video Notes | ✅ Complete |
| Cheat Sheets | ✅ Complete |

---

# Module Status

```text
MODULE 24 COMPLETE
```

---

**Author:** Clifford Ferraren  
**Program:** MIT Professional Education – Applied Data Engineering Program  
**Course:** Applied Data Engineering Program  
**Module:** Module 24 – Handling Big Data with Mosquitto, ThingsBoard, and Kafka# Module 24
# Handling Big Data with Mosquitto, ThingsBoard, and Kafka

## MIT Professional Education
### Applied Data Engineering Program

---

# Module Overview

Module 24 focused on designing, building, monitoring, and consuming real-time streaming data pipelines using three major technologies:

- Mosquitto
- ThingsBoard
- Kafka

The module progressed through three increasingly sophisticated streaming architectures:

```text
MQTT + Mosquitto
        ↓
ThingsBoard + Firebase
        ↓
Kafka + Node.js
```

Students learned how to:

- Generate telemetry data
- Build streaming pipelines
- Process real-time events
- Monitor data using alarms
- Store telemetry in the cloud
- Construct Kafka producer/consumer systems
- Build a web server for streaming applications

---

# Repository Structure

```text
Module_24_Handling_Big_Data
│
├── Assignment
├── Cheat_Sheets
├── Coding_Activities
├── Discussions
├── Knowledge_Checks
├── Resources
├── Sandbox
├── Videos
└── README.md
```

---

# Section 1
# Mosquitto and MQTT

## Technologies

- MQTT
- Mosquitto
- Paho MQTT
- Docker

---

## Concepts Learned

### MQTT

Message Queuing Telemetry Transport

Purpose:

```text
Lightweight IoT Messaging
```

Architecture:

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

### Mosquitto

Open-source MQTT broker.

Responsibilities:

```text
Message Routing
Topic Management
Publish / Subscribe
Telemetry Distribution
```

---

### Paho MQTT

Python MQTT client library.

Installation:

```cmd
pip install "paho-mqtt<2.0.0"
```

---

## Skills Developed

✅ MQTT Publishers

✅ MQTT Subscribers

✅ Topic Subscriptions

✅ Mosquitto Docker Deployment

✅ Telemetry Streaming

---

# Section 2
# ThingsBoard and Firebase

## Technologies

- ThingsBoard
- Firebase
- MQTT
- Mosquitto
- Docker

---

## Concepts Learned

### Devices

Telemetry producing entities.

Examples:

```text
Temperature Sensor

Humidity Sensor

GPS Device
```

---

### Assets

Containers for devices.

Examples:

```text
Building

Facility

Vehicle
```

---

### Rule Engine

Responsible for:

```text
Processing
Filtering
Routing
Transformation
```

---

### Rule Chains

Logical workflows used to process telemetry.

Example:

```text
Input
      ↓
Filter
      ↓
Storage
      ↓
Alerting
```

---

### Root Rule Chain

Primary processing workflow inside ThingsBoard.

---

### Widgets

Used to visualize telemetry.

Examples:

```text
Timeseries Charts

Gauges

Tables

Maps
```

---

### Alarms

Used to monitor telemetry and trigger actions.

Example:

```text
Temperature > Threshold
```

---

## Firebase

Used as a cloud-hosted:

```text
Realtime Database
```

for:

```text
Telemetry Storage
Alarm Storage
```

---

# Required Project 24.1 (Part 1)

## Streaming Live Data to ThingsBoard

### Objective

Create a complete telemetry pipeline.

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

### Deliverables

✅ Temperature Telemetry

✅ Humidity Telemetry

✅ Firebase Integration

✅ ThingsBoard Visualization

---

# Required Project 24.1 (Part 2)

## Analyzing Live Streaming Data Using ThingsBoard

### Objective

Build alarm-processing workflows.

---

### Architecture

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

---

### Deliverables

✅ Alarm Rule Chains

✅ Real-Time Alarm Processing

✅ Firebase Alarm Storage

✅ Telemetry Monitoring

---

# Major Technical Challenge

## Firebase SSL Trust Issue

### Error

```text
PKIX path building failed

SSLHandshakeException
```

---

### Root Cause

Corporate SSL inspection replaced Firebase certificates with:

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

then imported into Java truststore:

```bash
keytool -importcert \
-alias sempra-root \
-file /tmp/SempraRoot.cer \
-keystore /usr/lib/jvm/java-17-openjdk-amd64/lib/security/cacerts \
-storepass changeit \
-noprompt
```

Result:

✅ Firebase Connectivity Restored

✅ Alarm Data Generated

✅ Telemetry Data Stored

---

# Section 3
# Kafka and Node.js

## Technologies

- Kafka
- Confluent Platform
- KafkaJS
- Node.js
- Express
- Docker

---

## Concepts Learned

### Producer

Publishes events.

Example:

```json
{
    "longitude": 127,
    "latitude": 50
}
```

---

### Topic

Communication channel.

Example:

```text
vehicle-coordinates
```

---

### Broker

Stores and distributes Kafka messages.

---

### Consumer

Reads Kafka messages.

---

### Kafka Architecture

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

### Node.js

Used to build:

```text
Web Applications
Kafka Consumers
Web Servers
```

---

# Required Project 24.2

## Constructing a Web Server Using Kafka

### Objective

Build a producer/consumer architecture using Kafka.

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

### Deliverables

✅ Kafka Cluster Deployment

✅ Topic Creation

✅ Python Producer

✅ Kafka Consumer

✅ Node.js Server

✅ Web Application

✅ Real-Time Streaming

---

# Major Technical Challenge

## node-rdkafka Compatibility Issue

The course material relied upon:

```text
node-rdkafka
```

which required:

```text
Visual Studio Build Tools

Desktop Development with C++

node-gyp
```

and failed under:

```text
Node.js v22.23.5
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

✅ Kafka Consumer Functional

✅ No Native Compilation Required

✅ No Visual Studio Dependency

---

# Coding Activities

## Mosquitto

```text
Publisher
Subscriber
```

---

## ThingsBoard

```text
Project_24_1_Part_1

Project_24_1_Part_2
```

---

## Kafka

```text
Producer

Consumer

Web_Server
```

---

# Knowledge Checks

Completed:

```text
SKC 24.1 – Mosquitto

SKC 24.2 – ThingsBoard

SKC 24.3 – Kafka
```

Result:

```text
100% Completion
```

---

# Discussions

Completed:

```text
Discussion 24.1
Use Cases for Mosquitto

Discussion 24.2
Use Cases for ThingsBoard

Discussion 24.3
Use Cases for Kafka

Self-Study Discussion 24.1
Handling Big Data
```

---

# Cheat Sheets

Created:

```text
Module 24 Cheat Sheet

Kafka Producer Consumer Reference
```

Topics Covered:

```text
MQTT

ThingsBoard

Firebase

Kafka

Node.js

Docker

SSL Troubleshooting
```

---

# Key Skills Developed

✅ MQTT Messaging

✅ Publish / Subscribe Architectures

✅ Docker Deployments

✅ Telemetry Processing

✅ Rule Chains

✅ Alarm Workflows

✅ Firebase Integration

✅ Kafka Streaming

✅ Producers

✅ Consumers

✅ Node.js Web Servers

✅ KafkaJS

✅ Event Streaming

✅ SSL Troubleshooting

✅ Enterprise System Integration

---

# Fleet Intelligence Platform Connections

The technologies covered throughout Module 24 directly support future fleet telemetry architectures.

Example:

```text
Vehicle GPS Device
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

Potential Applications:

```text
Vehicle Tracking

Fuel Monitoring

Route Optimization

Driver Analytics

Geofencing

Maintenance Alerts

Predictive Maintenance
```

---

# Module Deliverables Completed

| Deliverable | Status |
|-------------|---------|
| Project 24.1 Part 1 | ✅ Complete |
| Project 24.1 Part 2 | ✅ Complete |
| Project 24.2 | ✅ Complete |
| All Discussions | ✅ Complete |
| All Knowledge Checks | ✅ Complete |
| All Video Notes | ✅ Complete |
| Cheat Sheets | ✅ Complete |

---

# Module Status

```text
MODULE 24 COMPLETE
```

---

**Author:** Clifford Ferraren  
**Program:** MIT Professional Education – Applied Data Engineering Program  
**Course:** Applied Data Engineering Program  
**Module:** Module 24 – Handling Big Data with Mosquitto, ThingsBoard, and Kafka