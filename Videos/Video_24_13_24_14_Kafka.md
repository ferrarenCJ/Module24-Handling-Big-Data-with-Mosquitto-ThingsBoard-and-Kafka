# Kafka
## Videos 24.13 and 24.14

---

# Overview

This section introduces Apache Kafka, one of the most widely used technologies for handling large-scale real-time streaming data.

In these videos, students learn:

- Kafka fundamentals
- Kafka architecture
- Kafka producers
- Kafka consumers
- Docker deployment
- Confluent Kafka platform
- Node.js integration
- Web server preparation for Project 24.2

Kafka extends the streaming concepts learned earlier with MQTT, Mosquitto, ThingsBoard, and Firebase by providing a scalable enterprise-grade event streaming platform.

---

# Video 24.13
## Kafka Overview

### Duration

4:32

---

# What is Kafka?

Apache Kafka is an open-source distributed event-streaming platform designed to handle large quantities of real-time streaming data.

Kafka enables organizations to:

- Publish data
- Store data
- Stream data
- Process events
- Analyze events

at very large scale.

---

# Why Kafka?

Kafka can process:

- Millions of events per second
- Large numbers of producers
- Large numbers of consumers
- Distributed workloads

while maintaining:

- High availability
- Scalability
- Fault tolerance

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

# Kafka Components

## Producer

A producer sends messages to Kafka.

Examples:

```text
GPS Device

Sensor

Python Application

Web Application
```

---

### Example Producer Message

```json
{
    "latitude": 33.875,
    "longitude": -118.090
}
```

---

## Topic

A topic is a logical communication channel used to organize messages.

Example:

```text
vehicle-location
```

Messages are published to topics and consumed from topics.

---

## Broker

The broker receives and stores messages.

Responsibilities:

- Accept events
- Manage topics
- Store records
- Serve consumers

---

## Consumer

A consumer reads messages from a topic.

Examples:

```text
Dashboard

Analytics Engine

Web Application

Node.js Server
```

---

# Kafka Message Flow

```text
Vehicle Device
       ↓
Producer
       ↓
Kafka Topic
       ↓
Kafka Broker
       ↓
Consumer
       ↓
Application
```

---

# Kafka vs MQTT

| MQTT | Kafka |
|--------|--------|
| Lightweight IoT Protocol | Enterprise Event Streaming Platform |
| Device-Oriented | Platform-Oriented |
| Publish/Subscribe | Distributed Event Log |
| Small Devices | High-Volume Data Processing |
| Mosquitto Broker | Kafka Broker |

---

# Common Kafka Use Cases

## Transportation

```text
Vehicle Tracking

Route Analytics

Fleet Monitoring
```

---

## Finance

```text
Transaction Processing

Fraud Detection

Trading Systems
```

---

## Manufacturing

```text
Equipment Monitoring

Automation

Predictive Maintenance
```

---

## Utilities

```text
Smart Meter Telemetry

Pressure Monitoring

Leak Detection
```

---

## Web Applications

```text
User Activity Tracking

Log Aggregation

Clickstream Analytics
```

---

# Kafka Strengths

Kafka excels when:

```text
Large Data Volumes
```

must be processed continuously.

Examples:

```text
Millions of GPS Events

Billions of Sensor Readings

Continuous Log Streams
```

---

# Video 24.14
## Installing Kafka in a Docker Container

### Duration

5:56

---

# Objective

Deploy a complete Kafka environment using Docker.

---

# Kafka Platform Used

The course uses:

```text
Confluent Platform
```

Docker image.

Confluent provides:

- Kafka Broker
- ZooKeeper
- Supporting Kafka services

---

# Why Docker?

Benefits:

- Easy deployment
- Consistency
- Isolation
- Portability

---

# Kafka Docker Architecture

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

# Kafka Installation Files

Course materials provide:

```text
johnKafka GitHub Repository
```

Students download the provided ZIP file and deploy Kafka using Docker Compose.

---

# Required Software

Before running Kafka:

Install:

```text
Node.js
```

---

# Required Node.js Libraries

## Windows

```cmd
npm install express

npm install node-rdkafka
```

---

## Mac

```cmd
sudo xcode-select --reset

npm install express

npm install node-rdkafka
```

---

# What is Express?

Express is a lightweight Node.js web framework.

Used for:

- Web applications
- APIs
- Real-time services

---

# What is node-rdkafka?

`node-rdkafka` is a Kafka client library for Node.js.

Used to:

- Consume Kafka messages
- Produce Kafka messages
- Integrate Kafka with web applications

---

# Why Node.js?

Node.js is used in Project 24.2 to create a web server that acts as a Kafka consumer.

Workflow:

```text
Kafka Topic
      ↓
Node.js Consumer
      ↓
Web Server
      ↓
Client Browser
```

---

# Kafka Deployment Workflow

## Step 1

Download project files.

---

## Step 2

Start Docker environment.

```cmd
docker-compose up
```

---

## Step 3

Verify Kafka broker is running.

---

## Step 4

Verify ZooKeeper is running.

---

## Step 5

Create producers and consumers.

---

## Step 6

Build web server.

---

# Connection to Required Project 24.2

Project 24.2 requires students to build a complete Kafka streaming solution.

---

## Producer

Python application.

Publishes:

```json
{
    "latitude": 33.875,
    "longitude": -118.090
}
```

---

## Topic

```text
vehicle-location
```

---

## Broker

Kafka

---

## Consumer

Node.js

---

## Output

Web Server

---

# Final Project Architecture

```text
Vehicle GPS Generator
          ↓
Python Producer
          ↓
Kafka Topic
          ↓
Kafka Broker
          ↓
Node.js Consumer
          ↓
Web Server
```

---

# Example Vehicle Event

```json
{
    "vehicle_id": "TRUCK001",
    "latitude": 33.875,
    "longitude": -118.090
}
```

---

# Fleet Intelligence Platform Connections

Kafka aligns closely with future fleet telemetry architectures.

Potential implementation:

```text
Vehicle GPS
      ↓
Kafka Producer
      ↓
Kafka Broker
      ↓
Kafka Consumer
      ↓
Fleet Dashboard
```

---

# Potential Fleet Events

```json
{
    "vehicle_id": "SCG001",
    "speed": 58,
    "fuel_level": 72,
    "latitude": 33.875,
    "longitude": -118.090
}
```

---

# Potential Analytics

```text
Route Optimization

Speed Monitoring

Fuel Usage

Maintenance Alerts

Driver Behavior
```

---

# Key Concepts

| Concept | Description |
|----------|-------------|
| Kafka | Distributed event-streaming platform |
| Producer | Application publishing events |
| Consumer | Application reading events |
| Topic | Kafka communication channel |
| Broker | Kafka server |
| ZooKeeper | Kafka coordination service |
| Confluent Platform | Kafka distribution |
| Node.js | JavaScript runtime |
| Express | Node.js web framework |
| node-rdkafka | Kafka client library for Node.js |

---

# Key Learning Outcomes

Successfully introduced:

✅ Kafka Architecture

✅ Topics

✅ Producers

✅ Consumers

✅ Dockerized Kafka

✅ ZooKeeper

✅ Confluent Platform

✅ Node.js Integration

✅ Express Framework

✅ Kafka Web Server Concepts

---

# My Key Takeaways

- Kafka is designed for enterprise-scale streaming data processing.
- Producers publish events while consumers process them.
- Topics organize streaming events.
- Kafka brokers store and distribute events.
- Docker simplifies Kafka deployment through the Confluent Platform.
- Node.js and node-rdkafka provide Kafka consumer capabilities for web applications.
- Vehicle telemetry provides a practical introduction to real-time event streaming.
- Kafka complements technologies such as MQTT and ThingsBoard and is commonly used in modern data engineering architectures.