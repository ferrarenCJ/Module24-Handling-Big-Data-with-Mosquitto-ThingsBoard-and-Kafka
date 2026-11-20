# Using Mosquitto to Stream Data
## Videos 24.2 and 24.3

---

# Overview

These videos demonstrate how to:

1. Deploy Eclipse Mosquitto using Docker
2. Configure an MQTT broker
3. Publish data to MQTT topics
4. Subscribe to MQTT topics
5. Stream real-time IoT data using the MQTT protocol

Together, these videos provide the foundation for Project 24.1, where live telemetry data will be streamed into ThingsBoard and Firebase.

---

# Video 24.2
## Setting Up a Docker Container for Mosquitto

### Duration

05:31

---

# Purpose

Mosquitto is an MQTT broker that manages communication between publishers and subscribers.

Rather than installing Mosquitto directly on the operating system, the course deploys Mosquitto inside a Docker container.

Benefits:

- Easy setup
- Portable environment
- Isolated deployment
- Consistent configuration
- Simplified upgrades

---

# Architecture

```text
Publisher
     ↓
Mosquitto Broker
     ↓
Subscriber
```

Mosquitto runs inside Docker and acts as the central communication hub.

---

# Installing Mosquitto

The course provides:

```text
DockerMosquittoInstall.zip
```

Installation process:

### Step 1

Download and extract:

```text
DockerMosquittoInstall.zip
```

---

### Step 2

Open Command Prompt.

Navigate to the extracted folder.

```cmd
cd DockerMosquittoInstall
```

---

### Step 3

Start the container.

```cmd
docker-compose up
```

or with modern Docker:

```cmd
docker compose up
```

---

# Expected Result

Docker downloads and starts:

```text
eclipse-mosquitto
```

---

# Verify Container

Open Docker Desktop.

Confirm:

```text
mosquitto
```

shows:

```text
Running
```

---

# Verify Using Command Line

```cmd
docker ps
```

Expected:

```text
CONTAINER ID
IMAGE
eclipse-mosquitto
STATUS Up
```

---

# Check Mosquitto Logs

```cmd
docker logs mosquitto
```

Expected:

```text
mosquitto version x.x running
Opening ipv4 listen socket on port 1883
```

---

# Mosquitto Runtime Environment

Default MQTT port:

```text
1883
```

Common usage:

```text
Publisher → Port 1883 → Mosquitto → Subscribers
```

---

# Why Use Docker?

Advantages include:

- No local broker installation
- Easy container restart
- Reproducible environment
- Works consistently across systems

---

# Video 24.3
## Using Mosquitto to Publish and Subscribe to Data Stream Topics

### Duration

10:50

---

# Objective

Learn how MQTT clients communicate through Mosquitto using:

- Topics
- Publishers
- Subscribers
- Messages

---

# MQTT Publish / Subscribe Model

MQTT uses asynchronous communication.

```text
Publisher
    ↓
 Topic
    ↓
 Broker
    ↓
Subscriber
```

---

# Publisher

A publisher produces data and sends it to a topic.

Examples:

- Temperature sensor
- Humidity sensor
- GPS tracker
- Vehicle telemetry device

Example:

```text
Temperature = 80°F
```

Publisher sends:

```json
{
  "temperature": 80
}
```

---

# Subscriber

A subscriber listens to a topic.

Example subscribers:

- Dashboard
- Analytics platform
- Alert system
- Database

---

# Topics

Topics organize communication channels.

Examples:

```text
sensors/temperature

sensors/humidity

vehicles/gps

alerts
```

Subscribers only receive messages for topics they subscribe to.

---

# Message Flow

Example:

```text
Temperature Sensor
        ↓
 Topic:
sensors/temperature
        ↓
Mosquitto Broker
        ↓
Dashboard
        ↓
Database
        ↓
Alert Service
```

---

# Publishing Data

Using Paho:

```python
client.publish(
    "sensors/temperature",
    payload
)
```

Result:

```text
Topic:
sensors/temperature

Payload:
{"temperature":72}
```

is sent to Mosquitto.

---

# Subscribing to Data

Using Paho:

```python
client.subscribe(
    "sensors/temperature"
)
```

The subscriber now receives all future messages sent to:

```text
sensors/temperature
```

---

# Real-Time Streaming

One of MQTT's strengths is continuous streaming.

Example:

```text
08:00 Temperature 70
08:01 Temperature 71
08:02 Temperature 73
08:03 Temperature 72
```

Every update is immediately delivered to subscribers.

---

# Event-Driven Architecture

MQTT systems are event-driven.

New data arrives →

```text
Publish Event
       ↓
Broker
       ↓
Subscriber
       ↓
Processing
```

No polling is required.

---

# Broker Responsibilities

Mosquitto:

### Receives Messages

```text
Publish()
```

---

### Maintains Topics

```text
sensors/*
vehicles/*
alerts/*
```

---

### Tracks Subscribers

Determines who should receive messages.

---

### Delivers Messages

Routes data appropriately.

---

# Example Data Stream

Publisher:

```json
{
  "temperature": 65
}
```

Broker:

```text
Mosquitto
```

Subscriber output:

```text
sensors/temperature
{"temperature":65}
```

---

# Monitoring Containers

The course notes that container status can be monitored through browser-based interfaces.

Examples include:

```text
localhost:8080
```

for Dockerized services that expose web interfaces.

Always verify:

- Container health
- Running status
- Port mappings
- Logs

---

# Mosquitto Workflow

```text
Python Publisher
        ↓
 MQTT Topic
        ↓
 Mosquitto Broker
        ↓
Python Subscriber
        ↓
Console Output
```

---

# Connection to Project 24.1

Project 24.1 extends this architecture.

Current lesson:

```text
Publisher
    ↓
Broker
    ↓
Subscriber
```

Project workflow:

```text
Temperature Producer
Humidity Producer
          ↓
     Mosquitto
          ↓
     ThingsBoard
          ↓
      Firebase
```

---

# Real-World Applications

## Smart Home

Devices:

- Thermostats
- Cameras
- Motion sensors

---

## Automotive

Streaming:

- GPS
- Speed
- Diagnostics
- Fuel telemetry

---

## Industrial IoT

Streaming:

- Machine health
- Pressure readings
- Production metrics

---

## Utilities

Examples relevant to gas utilities:

- Smart meters
- Pressure sensors
- Leak detection systems
- Cathodic protection monitoring

---

# Fleet Intelligence Platform Connections

This module maps directly to a future fleet telemetry solution.

Example architecture:

```text
Vehicle Device
      ↓
 MQTT Publisher
      ↓
 Mosquitto Broker
      ↓
 Kafka
      ↓
 Analytics Platform
      ↓
 Dashboard
```

Potential vehicle telemetry payload:

```json
{
  "vehicle_id": "SCG001",
  "latitude": 33.8751,
  "longitude": -118.0885,
  "speed": 58,
  "fuel_level": 72
}
```

---

# Key Commands

## Start Container

```cmd
docker compose up -d
```

---

## List Running Containers

```cmd
docker ps
```

---

## View Logs

```cmd
docker logs mosquitto
```

---

## Stop Container

```cmd
docker compose down
```

---

# Key Terms

| Term | Definition |
|--------|------------|
| MQTT | Message Queuing Telemetry Transport |
| Mosquitto | MQTT broker implementation |
| Publisher | Produces messages |
| Subscriber | Consumes messages |
| Topic | Message channel |
| Broker | Message routing service |
| Docker | Container platform |
| Container | Isolated runtime environment |
| Stream | Continuous flow of data |
| Telemetry | Remote measurement data |

---

# My Key Takeaways

- Mosquitto is deployed using Docker for portability and simplicity.
- The broker is central to all MQTT communication.
- Publishers send messages to topics.
- Subscribers receive messages from topics.
- Topics organize data streams.
- MQTT is highly effective for streaming IoT data.
- Mosquitto supports scalable event-driven architectures.
- These lessons provide the foundation for Project 24.1, where data will flow from MQTT into ThingsBoard and Firebase.
- The same publish/subscribe pattern is used in modern telemetry, fleet management, industrial IoT, and utility-monitoring systems.