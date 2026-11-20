# ThingsBoard and Required Project 24.1

---

# Overview

In this section, the focus shifts from MQTT messaging with Mosquitto to building a complete IoT data streaming solution using:

- Mosquitto
- MQTT
- ThingsBoard
- Firebase
- Docker

The goal is to create an end-to-end pipeline that collects data from IoT devices, processes the data in ThingsBoard, and stores the results in Firebase.

---

# What is ThingsBoard?

ThingsBoard is an open-source IoT platform used for:

- Device management
- Data collection
- Data processing
- Data visualization
- Rule-based workflows
- Alarm generation
- Real-time dashboards

ThingsBoard sits between IoT devices and downstream systems, providing monitoring, analytics, and automation capabilities.

---

# Topics Covered in This Section

## Environment Setup

Learn how to:

- Create a Firebase project
- Configure a Firebase Realtime Database
- Deploy ThingsBoard using Docker
- Connect IoT devices to ThingsBoard

---

## ThingsBoard Components

Learn how to work with:

### Devices

Represent real-world IoT devices.

Examples:

- Temperature sensors
- Humidity sensors
- Smart meters
- Vehicle GPS trackers

---

### Widgets

Visual components used for dashboards.

Examples:

- Charts
- Gauges
- Tables
- Maps
- KPI indicators

---

### Rule Chains

Workflow engines that process incoming telemetry data.

Examples:

```text
Incoming Data
      ↓
 Rule Chain
      ↓
 Transformation
      ↓
 Storage
      ↓
 Notification
```

---

### Root Rule Chain

The primary processing workflow inside ThingsBoard.

Responsibilities:

- Receive telemetry
- Process messages
- Route events
- Trigger alarms
- Send data to external systems

---

# Data Flow Architecture

The architecture developed during this section will resemble:

```text
IoT Device
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

# Required Project 24.1 Overview

Project 24.1 is divided into two parts.

---

# Part 1: Streaming Live Data to ThingsBoard

## Objective

Build an end-to-end streaming pipeline.

---

## Technologies

- MQTT
- Mosquitto
- ThingsBoard
- Firebase

---

## Tasks

### Step 1

Set up Mosquitto.

Purpose:

```text
MQTT Broker
```

---

### Step 2

Generate telemetry data.

Example data:

```json
{
  "temperature": 75
}
```

and

```json
{
  "humidity": 45
}
```

---

### Step 3

Publish data using MQTT.

```text
Sensor
     ↓
Publisher
     ↓
Mosquitto
```

---

### Step 4

Verify data arrives in ThingsBoard.

```text
Mosquitto
     ↓
ThingsBoard
```

---

### Step 5

Create Firebase project.

Configure:

```text
Realtime Database
```

---

### Step 6

Send telemetry data to Firebase.

```text
ThingsBoard
     ↓
Firebase
```

---

## Final Architecture

```text
Temperature Sensor
Humidity Sensor
          ↓
     MQTT Publisher
          ↓
   Mosquitto Broker
          ↓
     ThingsBoard
          ↓
 Firebase Realtime DB
```

---

# Part 1 Deliverables

Successfully demonstrate:

✅ Mosquitto Running

✅ MQTT Publishing

✅ ThingsBoard Receiving Data

✅ Firebase Receiving Data

✅ Temperature Telemetry

✅ Humidity Telemetry

---

# Part 2: Analyzing Live Streaming Data Using ThingsBoard

## Objective

Create a real-time monitoring and alerting solution.

---

# Alarm Rule Chains

An Alarm Rule Chain evaluates live telemetry and triggers actions when thresholds are exceeded.

Example:

```text
Temperature > 90°F
```

Generate:

```text
High Temperature Alert
```

---

# Tasks

### Step 1

Create an Alarm Rule Chain.

---

### Step 2

Define threshold conditions.

Examples:

```text
Temperature > 90

Humidity > 90
```

---

### Step 3

Connect alarm workflow to Firebase.

```text
Alarm
    ↓
Firebase
```

---

### Step 4

Connect the Root Rule Chain.

```text
Root Rule Chain
          ↓
Alarm Rule Chain
```

---

### Step 5

Test alarm generation.

Verify:

```text
Alert Triggered
```

appears in Firebase.

---

# Part 2 Architecture

```text
Telemetry Data
        ↓
Root Rule Chain
        ↓
Alarm Rule Chain
        ↓
Firebase
```

---

# End-to-End Architecture

After completing both parts:

```text
Temperature Sensor
Humidity Sensor
         ↓
    MQTT Client
         ↓
 Mosquitto Broker
         ↓
   ThingsBoard
         ↓
 Root Rule Chain
         ↓
 Alarm Rule Chain
         ↓
 Firebase
```

---

# Why This Project Matters

This project introduces many concepts found in production IoT and streaming environments.

Examples include:

- Event-driven architectures
- Telemetry processing
- Real-time monitoring
- IoT analytics
- Alerting systems
- Cloud integrations

---

# Real-World Applications

## Utilities

Examples:

- Smart gas meters
- Pressure monitoring
- Leak detection systems

---

## Fleet Management

Examples:

- Vehicle GPS tracking
- Driver monitoring
- Fuel consumption alerts
- Maintenance alerts

---

## Manufacturing

Examples:

- Equipment telemetry
- Predictive maintenance
- Operational monitoring

---

## Smart Buildings

Examples:

- HVAC monitoring
- Occupancy sensors
- Environmental controls

---

# Fleet Intelligence Platform Connections

This module closely resembles the architecture of a modern fleet telemetry platform.

Potential future design:

```text
Vehicle GPS Device
          ↓
 MQTT Publisher
          ↓
 Mosquitto Broker
          ↓
 ThingsBoard
          ↓
 Kafka/Event Hub
          ↓
 Fleet Dashboard
          ↓
 Alert Engine
```

Sample telemetry:

```json
{
  "vehicle_id": "SCG001",
  "latitude": 33.875,
  "longitude": -118.090,
  "speed": 62,
  "fuel_level": 73
}
```

Possible alarms:

```text
Fuel Theft Alert

Vehicle Offline

Speed Threshold Exceeded

Maintenance Due
```

---

# Key Concepts

| Concept | Description |
|----------|-------------|
| ThingsBoard | Open-source IoT platform |
| Device | IoT asset sending data |
| Widget | Dashboard visualization |
| Rule Chain | Processing workflow |
| Root Rule Chain | Primary processing chain |
| Alarm Rule Chain | Alert processing workflow |
| Telemetry | Live sensor data |
| Firebase | Cloud-based realtime database |
| MQTT | IoT publish/subscribe protocol |
| Mosquitto | MQTT broker |

---

# My Key Takeaways

- ThingsBoard extends MQTT systems by adding visualization, workflows, and alerting capabilities.
- Firebase acts as the destination for processed telemetry and alarm data.
- The Root Rule Chain processes incoming telemetry.
- Alarm Rule Chains enable threshold-based monitoring and notifications.
- Project 24.1 creates a complete IoT streaming architecture from data generation through storage and alerting.
- The technologies and architecture closely resemble real-world IoT, utility, and fleet-monitoring systems.