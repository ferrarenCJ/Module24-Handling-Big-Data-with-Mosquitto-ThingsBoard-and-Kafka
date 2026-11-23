# Module 24 Glossary
# Handling Big Data with Mosquitto, ThingsBoard, and Kafka

---

# A

## Action Nodes

In ThingsBoard, Action Nodes execute actions based on incoming messages.

Examples:

- Create Alarm
- Clear Alarm
- Save Timeseries
- REST API Call

---

## Alarm

In ThingsBoard, alarms are used to monitor telemetry and notify users when data reaches a defined threshold.

Example:

```text
Temperature > 20°C
```

Result:

```text
General Alarm
```

---

## Asset

An abstract entity in ThingsBoard used to organize and group devices.

Examples:

```text
Building A
Vehicle A
Facility A
```

Assets act as logical containers for devices.

---

# B

## Broker

A broker is a server responsible for receiving, storing, and routing messages between producers and consumers.

Examples:

```text
Mosquitto
Kafka Broker
```

Architecture:

```text
Producer
    ↓
 Broker
    ↓
Consumer
```

---

# C

## Callback Functions

Functions executed automatically when a specific event occurs.

Example in Paho MQTT:

```python
on_connect()

on_message()
```

Used to process incoming MQTT messages.

---

## Cluster

In Kafka, a cluster is the collection of Kafka brokers working together.

Benefits:

- High availability
- Fault tolerance
- Scalability

---

## Consumer

In Kafka, a consumer reads messages from Kafka topics through a Kafka broker.

Examples:

```text
Node.js Consumer
Analytics Service
Dashboard Application
```

Architecture:

```text
Producer
    ↓
Broker
    ↓
Consumer
```

---

# D

## Data Partitions

The smallest Kafka storage unit.

Kafka topics are divided into partitions to:

- Improve scalability
- Improve performance
- Distribute workload

---

## Device

In ThingsBoard, a device is an abstract component that records and transmits telemetry.

Examples:

```text
Temperature Sensor
Humidity Sensor
GPS Tracker
Smart Meter
```

Devices belong to assets.

---

# F

## Filter Nodes

ThingsBoard nodes used to evaluate, filter, and route messages.

Examples:

```text
Message Type Switch
TempThreshold
MaxTemp
```

---

# K

## Kafka

Apache Kafka is a distributed publish/subscribe messaging system used for processing big data at scale.

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

Uses:

```text
Streaming Analytics
Event Processing
IoT Telemetry
Financial Systems
Fleet Tracking
```

---

# L

## Link Label

Connection labels used between ThingsBoard Rule Nodes.

Examples:

```text
Success

Failure

True

False

Created

RPC Request from Device
```

---

## Live Streaming

The continuous generation and transmission of data in real time.

Examples:

```text
GPS Data

Temperature Data

Humidity Data

Vehicle Telemetry
```

---

## Logs

Status messages written by applications during execution.

Examples:

```text
Connected to Broker

Message Published

Message Consumed

Alarm Created
```

Used for:

- Debugging
- Monitoring
- Troubleshooting

---

# M

## Messaging Queue

A communication mechanism where producers and consumers are decoupled.

Messages are:

```text
Produced
Stored
Consumed
```

at different times.

Examples:

```text
Kafka Topics
RabbitMQ Queues
```

---

## Mosquitto

An open-source MQTT broker used for routing messages between MQTT clients.

Responsibilities:

```text
Publish
Subscribe
Route Messages
Manage Topics
```

---

## MQTT Broker

The central communication component in MQTT.

Responsibilities:

```text
Receive Messages
Manage Topics
Deliver Messages
```

Examples:

```text
Mosquitto
HiveMQ
EMQX
```

---

# N

## Node.js

An open-source JavaScript runtime environment that executes JavaScript outside of a browser.

Used for:

```text
Web Servers
APIs
Kafka Consumers
Streaming Applications
```

Powered by:

```text
Google Chrome V8 Engine
```

---

# P

## Paho Library

Python MQTT client library.

Installation:

```cmd
pip install "paho-mqtt<2.0.0"
```

Provides:

```text
MQTT Client
Publishing
Subscribing
Broker Connectivity
```

---

## Producer

In Kafka, a producer is responsible for sending data to Kafka topics.

Example:

```json
{
  "longitude": -118,
  "latitude": 34
}
```

Produced by:

```text
Python Application
IoT Device
GPS Device
```

---

## Protocol

A set of rules that govern communication between systems.

Examples:

```text
HTTP
HTTPS
MQTT
TCP/IP
```

---

## Publish / Subscribe Model

Messaging pattern where:

```text
Publisher
```

sends data and:

```text
Subscriber
```

receives data through a broker.

Architecture:

```text
Publisher
      ↓
Broker
      ↓
Subscriber
```

Used by:

```text
MQTT
Mosquitto
```

---

## Pumping Data

The process of transmitting data from one platform to another.

Examples:

```text
ThingsBoard → Firebase

Kafka → Consumer

Producer → Broker
```

---

# R

## Root Rule Chain

The primary Rule Chain in ThingsBoard.

Responsibilities:

```text
Receive Telemetry
Route Messages
Trigger Actions
Forward Data
```

---

## Rule Chain

A logical group of Rule Nodes and their relationships.

Examples:

```text
Root Rule Chain
CreateAndClearAlarms
AlarmToFirebase
TempToFirebase
```

---

## Rule Engine

ThingsBoard's event-processing framework.

Capabilities:

```text
Filtering
Routing
Transformation
Alarm Processing
```

---

## Rule Node

Individual processing components used inside a Rule Chain.

Examples:

```text
Input
Save Timeseries
TempThreshold
CreateAlarm
REST API Call
```

---

## Rule Node Relation

Connections between Rule Nodes.

Examples:

```text
Success
Failure
True
False
Created
```

---

# S

## Sensors

Hardware components that collect measurements and produce telemetry.

Examples:

```text
Temperature Sensors
Humidity Sensors
Pressure Sensors
GPS Devices
```

---

# T

## Telemetry

Data generated and transmitted by devices.

Examples:

```json
{
  "temperature": 76,
  "humidity": 93
}
```

```json
{
  "longitude": -118,
  "latitude": 34
}
```

---

## Topic (Kafka)

A Kafka communication channel used to organize data streams.

Example:

```text
vehicle-coordinates
```

Used by:

- Producers
- Consumers
- Brokers

---

## Topic (MQTT)

MQTT communication channel used by publishers and subscribers.

Examples:

```text
temperature

humidity

vehicle/location
```

Managed by the MQTT broker.

---

## ThingsBoard

Open-source IoT platform for:

```text
Device Management
Telemetry Processing
Dashboards
Rule Chains
Alarm Processing
```

Capabilities:

✅ Collect Data

✅ Visualize Data

✅ Process Data

✅ Trigger Alarms

---

# W

## Widget

A ThingsBoard visualization component.

Examples:

```text
Time Series Chart

Gauge

Map

Table

KPI Card
```

Used to display telemetry and alarm data.

---

# Z

## ZooKeeper

Apache ZooKeeper is a centralized coordination service used by Kafka.

Responsibilities:

```text
Broker Coordination
Configuration Management
Cluster Synchronization
Service Discovery
```

Used in:

```text
Kafka Clusters
```

---

# Module 24 Technologies Summary

| Technology | Purpose |
|------------|----------|
| MQTT | Lightweight IoT Messaging |
| Mosquitto | MQTT Broker |
| Paho | MQTT Client Library |
| ThingsBoard | IoT Platform |
| Firebase | Cloud Realtime Database |
| Kafka | Event Streaming Platform |
| KafkaJS | JavaScript Kafka Client |
| Node.js | Web Server Runtime |
| ZooKeeper | Kafka Coordination Service |

---

# Key Architectures

## MQTT

```text
Publisher
     ↓
MQTT Topic
     ↓
Mosquitto
     ↓
Subscriber
```

---

## ThingsBoard

```text
MQTT
   ↓
ThingsBoard
   ↓
Firebase
```

---

## Kafka

```text
Producer
    ↓
Topic
    ↓
Broker
    ↓
Consumer
```