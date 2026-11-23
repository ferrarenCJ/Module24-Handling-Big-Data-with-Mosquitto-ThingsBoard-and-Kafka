# Kafka and Required Project 24.2

---

# Overview

The final section of Module 24 focuses on Apache Kafka, one of the most widely used platforms for handling large-scale real-time streaming data.

In this section, students learn how to:

- Install Kafka using Docker
- Understand Kafka architecture
- Create Kafka producers
- Create Kafka consumers
- Use Node.js
- Build a web server
- Stream live data through Kafka
- Complete Required Project 24.2

This section builds upon the streaming concepts introduced earlier with MQTT, Mosquitto, ThingsBoard, and Firebase.

---

# What is Kafka?

Apache Kafka is an open-source distributed event-streaming platform used for:

- Real-time data ingestion
- Stream processing
- Event-driven architectures
- Data integration
- Analytics pipelines

Kafka is designed to handle:

- High throughput
- Low latency
- Fault tolerance
- Scalability

---

# Why Kafka?

Organizations use Kafka because it can process millions of events per second and distribute those events to multiple consumers simultaneously.

Examples:

- Vehicle telemetry
- Financial transactions
- Website activity
- IoT telemetry
- Sensor streams
- Application logs

---

# Kafka Architecture

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

# Key Components

## Producer

A producer publishes data to Kafka.

Examples:

```text
GPS Device

Vehicle Tracking System

IoT Sensor

Application
```

---

## Topic

A topic is a logical communication channel.

Example:

```text
vehicle-location
```

Messages are written to and read from topics.

---

## Broker

The broker receives and stores messages.

Responsibilities:

- Accept messages
- Manage topics
- Serve consumers

---

## Consumer

Consumers subscribe to topics and read messages.

Examples:

```text
Analytics Application

Dashboard

Web Server

Alert System
```

---

## ZooKeeper

ZooKeeper is used to coordinate Kafka components.

Responsibilities:

- Service discovery
- Cluster management
- Broker coordination

---

# Docker Deployment

The course uses a Docker image provided by:

```text
Confluent
```

The image includes:

- Kafka Broker
- ZooKeeper
- Supporting services

---

# Kafka Container Architecture

```text
Docker
    ↓
Confluent Platform
    ↓
Kafka Broker
    ↓
ZooKeeper
```

---

# Node.js Introduction

After Kafka installation, students install:

```text
Node.js
```

Node.js is used to create a web server that consumes Kafka messages.

---

# Why Node.js?

Node.js is well-suited for:

- Real-time applications
- Streaming data
- Lightweight web services
- Event-driven architectures

---

# Producer and Consumer Concepts

Kafka relies on two primary application types:

---

## Producer

Publishes events.

Example:

```json
{
    "latitude": 33.875,
    "longitude": -118.090
}
```

---

## Consumer

Reads events.

Example:

```text
Display Vehicle Location
```

---

# Streaming Workflow

```text
Vehicle GPS Data
        ↓
   Producer
        ↓
Kafka Topic
        ↓
Kafka Broker
        ↓
   Consumer
        ↓
Web Server
```

---

# Required Project 24.2

## Constructing a Web Server Using Kafka

---

# Objective

Build a Kafka-powered streaming application capable of:

- Publishing vehicle location data
- Processing live streaming events
- Creating a consumer
- Displaying data through a web server

---

# Technologies Used

| Technology | Purpose |
|------------|----------|
| Python | Producer |
| Kafka | Event Streaming Platform |
| Docker | Kafka Deployment |
| Confluent Platform | Kafka Distribution |
| ZooKeeper | Cluster Coordination |
| Node.js | Web Server |
| Kafka Consumer | Event Processing |

---

# Project Workflow

## Step 1

Install Kafka.

```text
Docker
```

↓

```text
Confluent Platform
```

---

## Step 2

Create a producer.

Producer publishes:

```json
{
    "latitude": 33.875,
    "longitude": -118.090
}
```

---

## Step 3

Publish to Kafka topic.

Topic:

```text
vehicle-location
```

---

## Step 4

Create consumer.

Consumer subscribes:

```text
vehicle-location
```

---

## Step 5

Create Node.js web server.

---

## Step 6

Display incoming data.

---

# Vehicle Location Example

Producer sends:

```json
{
    "vehicle_id": "TRUCK001",
    "latitude": 33.875,
    "longitude": -118.090
}
```

---

Consumer receives:

```json
{
    "vehicle_id": "TRUCK001",
    "latitude": 33.875,
    "longitude": -118.090
}
```

---

Web server displays:

```text
Vehicle Position Updated
```

---

# Relationship to Previous Module Content

Module Progression:

```text
MQTT
    ↓
Mosquitto
    ↓
ThingsBoard
    ↓
Firebase
    ↓
Kafka
```

Each technology builds upon the previous one.

---

# MQTT vs Kafka

| MQTT | Kafka |
|--------|--------|
| Lightweight IoT Protocol | Distributed Streaming Platform |
| Device-Oriented | Enterprise Streaming |
| Publish/Subscribe Broker | Distributed Event Log |
| Sensor Telemetry | High-Volume Event Processing |

---

# Real-World Kafka Use Cases

## Transportation

```text
Vehicle Tracking

Fleet Management

GPS Streaming
```

---

## Financial Services

```text
Transaction Processing

Fraud Detection
```

---

## Manufacturing

```text
Machine Telemetry

Predictive Maintenance
```

---

## Utilities

```text
Smart Meter Data

Pressure Monitoring

Leak Detection
```

---

## Web Applications

```text
Activity Tracking

User Events

Analytics Pipelines
```

---

# Fleet Intelligence Platform Connections

This section directly aligns with a future fleet telemetry architecture.

Potential architecture:

```text
Vehicle GPS Device
          ↓
Kafka Producer
          ↓
Kafka Broker
          ↓
Kafka Topic
          ↓
Node.js Consumer
          ↓
Fleet Dashboard
```

---

# Example Fleet Event

```json
{
    "vehicle_id": "SCG001",
    "latitude": 33.875,
    "longitude": -118.090,
    "speed": 58,
    "fuel_level": 72
}
```

---

# Potential Future Features

```text
Vehicle Tracking

Driver Analytics

Fuel Monitoring

Geofencing

Maintenance Alerts
```

---

# Key Concepts

| Concept | Description |
|----------|-------------|
| Kafka | Distributed event-streaming platform |
| Producer | Publishes events |
| Consumer | Reads events |
| Topic | Kafka communication channel |
| Broker | Kafka server |
| ZooKeeper | Cluster management service |
| Node.js | JavaScript runtime |
| Web Server | Event visualization endpoint |
| Event Streaming | Continuous event processing |

---

# Key Learning Outcomes

Successfully introduced:

✅ Kafka Architecture

✅ Topic-Based Messaging

✅ Producers

✅ Consumers

✅ Dockerized Kafka

✅ Node.js Integration

✅ Web Server Construction

✅ Vehicle Telemetry Streaming

✅ Event-Driven Processing

---

# My Key Takeaways

- Kafka is designed for enterprise-scale streaming data workloads.
- Producers publish events to topics while consumers process those events.
- Kafka provides scalable and fault-tolerant event streaming.
- Docker simplifies Kafka deployment through the Confluent Platform images.
- Node.js can be used to build web servers that consume Kafka streams.
- Vehicle location streaming provides a practical use case for learning Kafka.
- Kafka architectures align closely with real-world fleet management, telemetry, analytics, and IoT platforms.
- Required Project 24.2 combines Kafka, Python, Node.js, and Docker into a complete streaming solution.