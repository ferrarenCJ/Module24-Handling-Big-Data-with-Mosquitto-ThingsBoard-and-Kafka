# Mini-Lesson 24.1: Mosquitto and MQTT Protocol

---

# Overview

This lesson introduces:

- Eclipse Mosquitto
- MQTT (Message Queuing Telemetry Transport)
- Publish/Subscribe messaging
- IoT communication architecture
- MQTT Brokers, Topics, Publishers, and Subscribers
- Installing Mosquitto with Docker

MQTT is one of the most widely used communication protocols for Internet of Things (IoT) systems because it efficiently handles large volumes of continuous streaming data.

---

# What is Mosquitto?

Eclipse Mosquitto is an open-source MQTT broker.

Its primary responsibility is to receive messages from publishers and route those messages to subscribers.

Mosquitto acts as the central communication hub for MQTT-based systems.

```text
Publisher
    ↓
Mosquitto Broker
    ↓
Subscriber
```

---

# Publish/Subscribe Messaging Model

MQTT uses a Publish/Subscribe communication model.

Unlike traditional client-server communication, publishers and subscribers do not communicate directly.

Instead, they communicate through a broker.

## Publisher

A publisher sends data to a broker.

Examples:

- Temperature sensor
- Vehicle GPS tracker
- Smart thermostat
- Industrial sensor

---

## Subscriber

A subscriber receives data from the broker.

Examples:

- Dashboard
- Mobile application
- Analytics system
- Alerting service

---

## Broker

The broker acts as a message router.

Responsibilities:

- Receive messages
- Manage topics
- Track subscriptions
- Deliver messages to subscribers

Example:

```text
Temperature Sensor
       ↓
   Broker
    ↓ ↓ ↓
Dashboard
Database
Alert System
```

---

# What is a Protocol?

A protocol is a standardized set of rules that govern communication between systems.

Protocols ensure that systems exchange information safely, consistently, and efficiently.

Without protocols, devices would not know:

- How to send data
- How data should be formatted
- How responses should be handled

---

# Previously Learned Protocols

## HTTP

Hypertext Transfer Protocol (HTTP)

Used for communication between:

```text
Web Browser ↔ Web Server
```

Examples:

- Website requests
- REST APIs
- Web applications

HTTP follows a request-response pattern:

```text
Request
   ↓
Server
   ↓
Response
```

---

## TCP/IP

Transmission Control Protocol / Internet Protocol

Provides reliable communication between clients and servers.

Responsibilities:

- Addressing
- Routing
- Packet delivery
- Reliable communication

Most internet traffic relies on TCP/IP.

---

## REST APIs

REST APIs use HTTP for communication.

Example:

```text
Client
   ↓
HTTP Request
   ↓
Server
   ↓
HTTP Response
```

Common methods:

- GET
- POST
- PUT
- DELETE

---

# Why HTTP is Not Ideal for IoT

IoT systems generate continuous streams of data.

Examples:

- Vehicle telemetry
- GPS coordinates
- Smart home data
- Manufacturing sensors
- Utility monitoring systems

These systems continuously generate data without waiting for requests.

HTTP is inefficient because it requires:

1. A request
2. A response

for every interaction.

---

# What is IoT?

IoT (Internet of Things) refers to a network of physical devices connected to the internet.

Examples:

- Smart vehicles
- Smart watches
- Smart thermostats
- Cameras
- Industrial sensors
- Manufacturing equipment

These devices continuously collect and stream data.

---

# MQTT Protocol

MQTT stands for:

**Message Queuing Telemetry Transport**

It was specifically designed for:

- Lightweight communication
- Low bandwidth environments
- IoT devices
- Real-time telemetry

---

# MQTT Communication Model

MQTT uses a Publisher-Subscriber architecture.

```text
Publisher
    ↓
 Topic
    ↓
 Broker
    ↓
Subscriber
```

A publisher sends data to a topic.

The broker then distributes that data to every subscriber of the topic.

---

# Topics

Topics are communication channels used within MQTT.

Examples:

```text
temperature
humidity
gps
vehicles
fuel
alerts
```

Topics allow subscribers to receive only the messages they need.

---

## Example

Vehicle publishes GPS data:

```text
Topic:
vehicle/gps
```

Subscribers:

```text
Fleet Dashboard
Analytics System
Monitoring Service
```

All subscribed systems immediately receive the message.

---

# MQTT Clients

Every publisher and subscriber is considered an MQTT client.

Clients can:

- Publish data
- Subscribe to topics
- Publish and subscribe simultaneously

Examples:

```text
Sensor
Dashboard
Database Connector
Mobile App
Cloud Service
```

---

# MQTT Message Flow

## Step 1

Publisher sends data.

```text
Temperature Sensor
```

---

## Step 2

Message reaches broker.

```text
Mosquitto Broker
```

---

## Step 3

Broker determines which clients subscribed to the topic.

```text
temperature
```

---

## Step 4

Broker forwards message.

```text
Temperature Sensor
        ↓
    Mosquitto
      ↓ ↓ ↓
 Dashboard
 Firebase
 Analytics
```

---

# MQTT Architecture

MQTT architecture is broker-centric.

```text
       Client
          ↑
Client ← Broker → Client
          ↓
       Client
```

Key observation:

Clients never communicate directly.

All communication passes through the broker.

This architecture improves:

- Scalability
- Flexibility
- Reliability
- Decoupling

---

# Mosquitto Architecture

Mosquitto sits at the center of an MQTT deployment.

```text
IoT Devices
      ↓
Mosquitto Broker
      ↓
Applications
Dashboards
Databases
Alert Systems
```

Mosquitto supports:

- Thousands of devices
- Real-time communication
- Lightweight messaging
- Cross-platform deployments

---

# Real-World Mosquitto Use Cases

Examples include:

## Automotive

Vehicle telemetry

Data:

- GPS coordinates
- Speed
- Fuel consumption
- Diagnostics

---

## Smart Homes

Devices:

- Thermostats
- Cameras
- Sensors
- Alarms

---

## Industrial Systems

Streaming:

- Machine health
- Production metrics
- Sensor readings
- Equipment status

---

## Utilities

Examples relevant to gas and electric utilities:

- Pressure sensors
- Flow sensors
- Cathodic protection monitoring
- Smart meters
- Leak detection systems

---

# Installing Mosquitto with Docker

The module provides:

```text
DockerMosquittoInstall.zip
```

Installation process:

## Step 1

Download and unzip:

```text
DockerMosquittoInstall.zip
```

---

## Step 2

Open Command Prompt.

Navigate to the project folder.

```cmd
cd DockerMosquittoInstall
```

---

## Step 3

Start Mosquitto.

```cmd
docker-compose up
```

---

## Step 4

Verify in Docker Desktop.

Expected running container:

```text
Mosquitto
```

---

# What Happens Next?

Once Mosquitto is running:

### Publishers

Can send messages.

```text
publish()
```

### Subscribers

Can receive messages.

```text
subscribe()
```

### Broker

Routes messages between them.

---

# Project 24.1 Connection

## Streaming Live Data to ThingsBoard

In Project 24.1 Part 1:

You will publish:

- Temperature data
- Humidity data

using MQTT and Mosquitto.

Workflow:

```text
Temperature/Humidity Generator
                ↓
           MQTT Client
                ↓
       Mosquitto Broker
                ↓
          ThingsBoard
                ↓
           Firebase
```

---

# Why Data Engineers Need MQTT

Modern systems increasingly rely on event-driven architectures.

Data engineers must understand:

- Real-time ingestion
- Event streaming
- IoT messaging
- Broker architectures
- Publish/Subscribe models

MQTT is commonly used when:

- Data is continuously generated
- Low latency is required
- Devices are resource constrained
- Millions of events must be handled efficiently

---

# Key Terms

| Term | Definition |
|--------|------------|
| MQTT | Message Queuing Telemetry Transport |
| Mosquitto | Open-source MQTT broker |
| Broker | Message routing service |
| Publisher | Client that sends messages |
| Subscriber | Client that receives messages |
| Topic | Channel used to organize messages |
| Client | Any publisher or subscriber |
| IoT | Internet of Things |
| Publish | Send a message |
| Subscribe | Receive messages from a topic |
| Docker Container | Isolated runtime environment |

---

# Fleet Intelligence Platform Connections

This lesson directly maps to fleet telemetry architecture.

| MQTT Concept | Fleet Platform Equivalent |
|--------------|--------------------------|
| Publisher | Vehicle GPS device |
| Topic | Vehicle telemetry channel |
| Broker | Mosquitto/Kafka middleware |
| Subscriber | Fleet dashboard |
| Subscriber | Alerting engine |
| Subscriber | Analytics platform |
| MQTT Stream | Real-time vehicle tracking |

Potential future design:

```text
Vehicle Device
      ↓
 MQTT Broker
      ↓
 Kafka
      ↓
 Fleet Platform
      ↓
 Dashboards & Alerts
```

---

# My Key Takeaways

- MQTT is designed specifically for IoT and telemetry workloads.
- Mosquitto is an MQTT broker that routes messages between publishers and subscribers.
- Topics organize communication channels.
- Publishers send data while subscribers receive data.
- Brokers decouple producers from consumers.
- MQTT is more suitable than HTTP for continuous streaming sensor data.
- Docker makes it easy to deploy Mosquitto.
- MQTT architectures are widely used in fleet management, utilities, industrial monitoring, and smart-device ecosystems.