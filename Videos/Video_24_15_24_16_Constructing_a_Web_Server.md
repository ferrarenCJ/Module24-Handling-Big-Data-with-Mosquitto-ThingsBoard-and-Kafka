# Constructing a Web Server
## Videos 24.15 and 24.16

---

# Overview

This section introduces the use of Node.js and Kafka to build a web server capable of consuming and displaying live streaming data.

In these videos, students learn how to:

- Install Node.js
- Configure Node.js libraries
- Build a web server
- Connect a web server to Kafka
- Consume Kafka messages
- Stream data through a Kafka broker
- Prepare for Required Project 24.2

The final architecture combines:

- Kafka
- Docker
- Node.js
- Python
- Web Applications

to produce and consume streaming vehicle location data.

---

# Video 24.15
## Installing Node.js

### Duration

1:53

---

# Purpose

Before constructing a Kafka consumer application, Node.js must be installed.

Node.js provides:

- JavaScript runtime environment
- Server-side execution
- API support
- Real-time communication capabilities

---

# Why Node.js?

Node.js allows JavaScript code to execute outside of a browser.

Benefits include:

- Fast execution
- Event-driven architecture
- Lightweight runtime
- Large package ecosystem

---

# How Node.js Fits into Kafka

In Project 24.2:

```text
Kafka Topic
      ↓
Node.js Consumer
      ↓
Web Server
      ↓
Browser
```

Node.js becomes the consumer layer between Kafka and the user interface.

---

# Verify Existing Installation

Open Command Prompt:

```cmd
node --version
```

Example:

```text
v24.5.0
```

If a version number appears:

✅ Node.js is already installed.

---

# Install Node.js

If Node.js is not installed:

Navigate to:

```text
https://nodejs.org
```

Install the appropriate version:

```text
Windows
macOS
Linux
```

Recommended:

```text
LTS Version
```

---

# Verify Installation

```cmd
node --version

npm --version
```

Examples:

```text
v24.5.0

11.6.0
```

---

# What is NPM?

NPM stands for:

```text
Node Package Manager
```

NPM installs JavaScript libraries and dependencies.

Example:

```cmd
npm install express
```

---

# Video 24.16
## Constructing a Web Server to Produce and Consume Data from Kafka

### Duration

7:35

---

# Objective

Build a Node.js web server that communicates with Kafka.

Students learn how to:

- Install Kafka libraries
- Consume Kafka events
- Create a web server
- Display streaming data

---

# Kafka + Node.js Architecture

```text
Kafka Producer
       ↓
   Kafka Topic
       ↓
   Kafka Broker
       ↓
 Node.js Consumer
       ↓
    Web Server
       ↓
     Browser
```

---

# Preparation

Download:

```text
johnKafka GitHub Repository
```

provided by the course.

---

# Install Required Libraries

Navigate to:

```text
helloTest
```

project folder.

Install:

## Express

```cmd
npm install express
```

---

## Dependency Fixes

```cmd
npm audit fix
```

---

# What is Express?

Express is a lightweight Node.js web framework.

Used for:

- APIs
- Web applications
- HTTP servers
- Real-time applications

---

# Why Express?

Without Express:

```text
Manual HTTP Handling
```

With Express:

```text
Simple Route Definitions
```

Example:

```javascript
app.get('/', ...)
```

---

# node-rdkafka

Earlier in Module 24 students installed:

```cmd
npm install node-rdkafka
```

Purpose:

```text
Kafka Consumer
Kafka Producer
Node.js Integration
```

---

# Kafka Consumer Functionality

The Node.js server consumes:

```text
Vehicle Location Events
```

from Kafka topics.

---

# Example Event

```json
{
    "latitude": 33.875,
    "longitude": -118.090
}
```

---

# Kafka Workflow

## Producer

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

Stores and distributes messages.

---

## Consumer

Node.js receives messages.

---

## Browser

Displays information.

---

# Web Server Responsibilities

The server:

### Connects to Kafka

```text
Consumer
```

---

### Receives Events

```text
GPS Locations
```

---

### Processes Events

```text
JSON Messages
```

---

### Responds to Clients

```text
Browser Requests
```

---

# End-to-End Example

```text
Vehicle GPS Simulator
          ↓
     Producer
          ↓
Kafka Topic
          ↓
Kafka Broker
          ↓
Node.js Consumer
          ↓
Express Server
          ↓
Browser
```

---

# Project 24.2 Workflow

Students will build:

## Kafka Producer

Python application.

Produces:

```json
{
    "latitude": 33.875,
    "longitude": -118.090
}
```

---

## Kafka Topic

```text
vehicle-location
```

---

## Kafka Consumer

Node.js application.

---

## Web Server

Node.js + Express.

---

## Browser Client

Receives data.

---

# Streaming Location Example

Incoming event:

```json
{
    "vehicle_id": "TRUCK001",
    "latitude": 33.875,
    "longitude": -118.090
}
```

Consumer reads event.

Browser displays:

```text
Vehicle Location Updated
```

---

# Real-Time Benefits

Advantages include:

### Low Latency

Messages delivered quickly.

---

### Continuous Updates

Streaming data.

---

### Scalability

Supports many consumers.

---

### Decoupled Architecture

Producers and consumers remain independent.

---

# Relationship to Previous Topics

Earlier in Module 24:

```text
MQTT
   ↓
Mosquitto
   ↓
ThingsBoard
   ↓
Firebase
```

Current section:

```text
Kafka
   ↓
Broker
   ↓
Consumer
   ↓
Web Server
```

Both support streaming architectures but target different use cases.

---

# Real-World Kafka Applications

## Transportation

```text
Vehicle Tracking

Fleet Telemetry

Route Optimization
```

---

## Finance

```text
Fraud Detection

Transaction Monitoring
```

---

## Manufacturing

```text
Machine Events

Sensor Data
```

---

## Utilities

```text
Pressure Monitoring

Leak Detection

Smart Meter Data
```

---

## Web Analytics

```text
User Activity Streams
```

---

# Fleet Intelligence Platform Connections

This architecture closely resembles future fleet telemetry systems.

Example:

```text
Vehicle GPS Device
         ↓
 Kafka Producer
         ↓
 Kafka Topic
         ↓
 Kafka Consumer
         ↓
 Node.js Dashboard Server
         ↓
 Fleet Operations Dashboard
```

---

# Sample Fleet Payload

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

# Fleet Dashboard Capabilities

```text
Vehicle Locations

Fuel Monitoring

Driver Analytics

Maintenance Alerts

Geofence Events
```

---

# Key Concepts

| Concept | Description |
|----------|-------------|
| Node.js | JavaScript runtime |
| Express | Node.js web framework |
| Kafka | Event-streaming platform |
| Producer | Publishes events |
| Consumer | Reads events |
| Topic | Kafka communication channel |
| Broker | Kafka server |
| node-rdkafka | Kafka library for Node.js |
| Web Server | Serves data to browsers |

---

# Key Learning Outcomes

Successfully introduced:

✅ Node.js Installation

✅ Express Installation

✅ Kafka Consumer Concepts

✅ Node.js Web Servers

✅ Stream Processing

✅ Browser Communication

✅ Kafka Integration

✅ Producer / Consumer Patterns

✅ Event-Driven Architectures

---

# My Key Takeaways

- Node.js provides a lightweight platform for building Kafka consumer applications.
- Express simplifies the creation of web servers.
- Kafka can distribute streaming events to Node.js consumers in real time.
- Web servers allow Kafka events to be presented through browser-based interfaces.
- Producers generate streaming events while consumers process those events.
- Vehicle location streaming serves as a practical introduction to real-time event processing.
- The technologies introduced in these videos form the foundation for Required Project 24.2.
- Kafka and Node.js provide an architecture highly relevant to modern fleet, IoT, telemetry, and analytics platforms.