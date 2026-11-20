# Module 24: Handling Big Data with Mosquitto, ThingsBoard, and Kafka
## Video 24.1 - Introduction and Information

---

# Module Overview

Module 24 introduces three technologies used to handle large-scale streaming and IoT data:

1. Mosquitto
2. ThingsBoard
3. Kafka

These technologies support real-time data ingestion, messaging, monitoring, processing, and visualization of streaming data.

---

# Learning Objectives

By the end of this module, I should be able to:

- Explain key concepts of Mosquitto, ThingsBoard, and Kafka
- Understand MQTT publish/subscribe messaging
- Stream live data using ThingsBoard
- Analyze live streaming data using alarms and dashboards
- Build a web server using Kafka and Node.js
- Identify real-world use cases for modern streaming architectures

---

# Section 1: Mosquitto and MQTT

## Key Concepts

### MQTT

MQTT (Message Queuing Telemetry Transport) is a lightweight messaging protocol commonly used for IoT and real-time streaming applications.

Characteristics:

- Lightweight
- Low bandwidth usage
- Event-driven
- Publish/Subscribe architecture

### Broker

A broker acts as the central message hub.

Responsibilities:

- Receives messages from publishers
- Routes messages to subscribers
- Manages topic subscriptions

### Publisher

Produces and sends messages to a broker.

Examples:

- Temperature sensor
- Humidity sensor
- GPS tracker
- Vehicle telemetry system

### Subscriber

Receives messages from the broker.

Examples:

- Monitoring dashboard
- Database
- Analytics platform
- Alerting system

### Mosquitto

Mosquitto is an open-source MQTT broker that implements the MQTT protocol.

Primary use cases:

- IoT messaging
- Sensor networks
- Telemetry collection
- Real-time monitoring

---

## Skills Covered

- Deploy Mosquitto using Docker
- Publish MQTT messages
- Subscribe to MQTT topics
- Understand MQTT message flow
- Analyze Mosquitto use cases

---

# Section 2: ThingsBoard

## What is ThingsBoard?

ThingsBoard is an open-source IoT platform used for:

- Device management
- Data collection
- Data processing
- Data visualization
- Alert management

---

## Supporting Technologies

### Firebase

Google Firebase will be used as a backend storage platform.

Capabilities:

- Realtime Database
- Event storage
- Cloud data synchronization

---

## ThingsBoard Components

### Root Rule Chain

Processes incoming messages and routes data through a workflow.

### Widgets

Dashboard components used to display:

- Live telemetry
- Statistics
- Charts
- Device status

### Alarm Rule Chains

Rule-based workflows that trigger when thresholds are crossed.

Examples:

- Temperature > Threshold
- Humidity > Threshold
- Device Offline

---

## Skills Covered

- Configure ThingsBoard
- Create Firebase projects
- Create Root Rule Chains
- Build dashboards and widgets
- Configure alarms
- Stream data to Firebase

---

# Section 3: Kafka

## What is Kafka?

Apache Kafka is a distributed event-streaming platform designed for large-scale streaming applications.

Kafka supports:

- Data ingestion
- Event streaming
- Data pipelines
- Real-time analytics

---

## Kafka Components

### Producer

Publishes messages to Kafka topics.

Example:

Vehicle GPS application publishing:

- Latitude
- Longitude
- Timestamp

---

### Topic

Logical channel where messages are stored.

Example:

vehicle-location

---

### Consumer

Reads messages from Kafka topics.

Examples:

- Applications
- Dashboards
- Analytics platforms
- Web servers

---

### Broker

Kafka server responsible for:

- Receiving events
- Storing events
- Delivering events to consumers

---

### ZooKeeper

Service used for cluster coordination and management.

---

## Additional Technologies

### Docker

Used to deploy Kafka infrastructure.

### Confluent Kafka Image

Provides:

- Kafka Broker
- ZooKeeper
- Supporting Kafka services

### Node.js

Used to build a web server that consumes Kafka messages.

---

## Skills Covered

- Deploy Kafka with Docker
- Create producers
- Create consumers
- Stream real-time data
- Build a web server in Node.js
- Display Kafka events in real time

---

# Required Project 24.1

## Part 1: Streaming Live Data to ThingsBoard

### Objective

Build an end-to-end IoT streaming pipeline.

### Workflow

MQTT Device
→ Mosquitto Broker
→ ThingsBoard
→ Firebase Realtime Database

### Tasks

1. Configure Mosquitto
2. Generate temperature data
3. Generate humidity data
4. Publish data via MQTT
5. Consume data in ThingsBoard
6. Send data to Firebase

### Estimated Time

2.5 Hours

---

## Architecture

Temperature Sensor
          ↓
Humidity Sensor
          ↓
     MQTT Publisher
          ↓
       Mosquitto
          ↓
      ThingsBoard
          ↓
       Firebase

---

# Required Project 24.1 Part 2

## Analyzing Live Streaming Data Using ThingsBoard

### Objective

Create an alarm processing framework for real-time telemetry.

### Workflow

Incoming Data
→ Root Rule Chain
→ Alarm Rule Chain
→ Firebase

### Tasks

1. Create alarm workflows
2. Define alarm thresholds
3. Connect alarms to Firebase
4. Test alarm generation
5. Verify alarm storage

### Estimated Time

2 Hours

---

# Required Project 24.2

## Constructing a Web Server Using Kafka

### Objective

Create a streaming application that publishes GPS data to Kafka and displays it through a web server.

### Workflow

Python Producer
→ Kafka Topic
→ Kafka Broker
→ Node.js Consumer
→ Web Server

### Data Stream

Vehicle Location Data

- Longitude
- Latitude
- Timestamp

### Technologies

- Python
- Kafka
- Confluent Platform
- Docker
- Node.js

### Estimated Time

2 Hours

---

# Module Deliverables

## Discussions

### Discussion 24.1

Use Cases for Mosquitto

### Discussion 24.2

Use Cases for ThingsBoard

### Discussion 24.3

Use Cases for Kafka

---

## Projects

### Project 24.1 Part 1

Streaming Live Data to ThingsBoard

### Project 24.1 Part 2

Analyzing Live Streaming Data Using ThingsBoard

### Project 24.2

Constructing a Web Server Using Kafka

---

# Key Terms

| Term | Definition |
|--------|------------|
| MQTT | Lightweight publish/subscribe messaging protocol |
| Broker | Message routing service |
| Publisher | Message producer |
| Subscriber | Message consumer |
| Mosquitto | Open-source MQTT broker |
| ThingsBoard | Open-source IoT platform |
| Firebase | Google cloud backend platform |
| Rule Chain | Workflow for processing data |
| Alarm Rule Chain | Event-driven alert workflow |
| Widget | Dashboard visualization component |
| Kafka | Distributed event-streaming platform |
| Producer | Application that sends messages |
| Consumer | Application that receives messages |
| Topic | Kafka communication channel |
| ZooKeeper | Kafka cluster management service |
| Node.js | JavaScript runtime for server applications |

---

# Fleet Intelligence Platform Connections

This module directly aligns with the Fleet Intelligence Platform architecture.

Potential mappings:

| Module Technology | Fleet Platform Use |
|------------------|-------------------|
| MQTT | Vehicle telemetry ingestion |
| Mosquitto | IoT message broker |
| ThingsBoard | Fleet dashboards |
| Firebase | Realtime event storage |
| Kafka | Enterprise event backbone |
| Node.js | Fleet APIs and streaming services |
| GPS Streaming | Vehicle location tracking |
| Alarms | Fuel theft and maintenance alerts |

---

# My Key Takeaways

- MQTT is designed for lightweight device communications.
- Mosquitto implements MQTT messaging through a broker architecture.
- ThingsBoard provides dashboards, rules, alarms, and IoT data management.
- Firebase can store streamed telemetry and alarms.
- Kafka is a scalable event-streaming platform used for high-volume data pipelines.
- Producers publish events while consumers process them.
- Node.js can consume Kafka streams and expose them through web applications.
- The technologies in this module closely resemble modern IoT and telemetry architectures used in transportation, fleet management, utilities, and industrial monitoring.