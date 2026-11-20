# Getting Started with Firebase
## Videos 24.4 and 24.5

---

# Overview

This section introduces two critical components of the Module 24 architecture:

1. Firebase Realtime Database
2. ThingsBoard

Together with Mosquitto and MQTT, these technologies form an end-to-end IoT streaming platform capable of collecting, processing, visualizing, and storing telemetry data.

By the end of these videos, the architecture will begin to resemble:

```text
IoT Device
      ↓
 MQTT
      ↓
Mosquitto Broker
      ↓
 ThingsBoard
      ↓
 Firebase Realtime Database
```

---

# Video 24.4
## Creating a Project in Firebase

### Duration

03:52

---

# What is Firebase?

Firebase is a cloud application development platform created by Google.

It provides:

- Authentication
- Realtime databases
- Cloud storage
- Hosting
- Analytics
- Serverless application services

For this module, Firebase will be used as a destination for storing telemetry and alarm data.

---

# Firebase Realtime Database

The Realtime Database is a cloud-hosted NoSQL database.

Key characteristics:

- Real-time synchronization
- JSON-based data model
- Automatic updates
- Cloud-managed infrastructure

Data written by one application is immediately available to all connected applications.

---

# Why Firebase is Used in This Module

Firebase provides an easy way to store and monitor live IoT data generated through:

```text
Sensor
   ↓
Mosquitto
   ↓
ThingsBoard
   ↓
Firebase
```

This allows telemetry data to be:

- Persisted
- Shared
- Queried
- Monitored

---

# Firebase Setup Process

## Step 1

Navigate to:

```text
https://firebase.google.com
```

---

## Step 2

Sign in using a Google account.

---

## Step 3

Create a new Firebase Project.

Example:

```text
Module24-IoT-Project
```

---

## Step 4

Enable:

```text
Realtime Database
```

---

## Step 5

Select database region.

Choose a region closest to users or applications.

Example:

```text
us-west
```

---

## Step 6

Configure security rules.

For learning environments:

```text
Test Mode
```

Production environments should use restricted access.

---

# Firebase Data Example

Example temperature reading:

```json
{
  "temperature": 71,
  "humidity": 48
}
```

Stored in Firebase:

```json
{
  "sensorData": {
    "temperature": 71,
    "humidity": 48
  }
}
```

---

# Why Data Engineers Care About Firebase

Advantages include:

- Real-time synchronization
- Cloud scalability
- Easy integration
- Serverless architecture
- Rapid prototyping

Common use cases:

- IoT telemetry
- Mobile applications
- Web applications
- Dashboards
- Alerting systems

---

# Video 24.5
## Installing ThingsBoard in a Docker Container

### Duration

05:19

---

# What is ThingsBoard?

ThingsBoard is an open-source IoT platform used for:

- Device management
- Telemetry ingestion
- Data processing
- Real-time dashboards
- Rule engine workflows
- Alarm generation

It acts as a central hub for IoT systems.

---

# ThingsBoard Architecture

```text
Device
   ↓
Telemetry
   ↓
ThingsBoard
   ↓
Rules
   ↓
Visualization
   ↓
Storage
```

---

# Core Features

## Device Management

Manage connected devices.

Examples:

- Temperature sensors
- Humidity sensors
- GPS trackers
- Smart meters

---

## Telemetry Processing

Collect:

```text
Temperature
Humidity
GPS
Pressure
Fuel Level
```

---

## Dashboards

Visualize data using:

- Charts
- Gauges
- Tables
- KPI widgets
- Maps

---

## Rule Engine

Automates workflows.

Examples:

```text
IF Temperature > 90

THEN Create Alert
```

---

## Alarm Engine

Generates notifications when thresholds are exceeded.

Examples:

```text
High Temperature

High Humidity

Low Fuel

Device Offline
```

---

# Why Docker is Used

The course installs ThingsBoard using Docker.

Benefits:

- Fast deployment
- Consistent environment
- Easy updates
- Minimal configuration

---

# Docker-Based ThingsBoard Deployment

Architecture:

```text
Docker Container
         ↓
   ThingsBoard
```

---

# Typical Installation Workflow

## Step 1

Download module installation package.

---

## Step 2

Navigate to project directory.

```cmd
cd ThingsBoard
```

---

## Step 3

Start container.

```cmd
docker compose up
```

or

```cmd
docker-compose up
```

---

## Step 4

Verify in Docker Desktop.

Expected:

```text
thingsboard
```

Container status:

```text
Running
```

---

# Accessing ThingsBoard

Typically accessed from:

```text
http://localhost:8080
```

After startup, the ThingsBoard login page should appear.

---

# ThingsBoard's Role in Project 24.1

ThingsBoard becomes the processing layer between Mosquitto and Firebase.

---

## Data Flow

```text
Temperature Sensor
        ↓
   MQTT Publish
        ↓
Mosquitto Broker
        ↓
  ThingsBoard
        ↓
   Firebase
```

---

# Part 1 Connection

In Project 24.1 Part 1:

You will:

### Create telemetry

```text
Temperature
Humidity
```

---

### Send telemetry

```text
MQTT
```

---

### Receive telemetry

```text
ThingsBoard
```

---

### Store telemetry

```text
Firebase
```

---

# Part 2 Connection

In Project 24.1 Part 2:

ThingsBoard's Rule Engine will be extended to generate alarms.

Workflow:

```text
Incoming Telemetry
        ↓
Root Rule Chain
        ↓
Alarm Rule Chain
        ↓
Firebase
```

---

# Combined Architecture

After completing both project parts:

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
 Firebase Realtime DB
```

---

# Real-World Applications

## Smart Homes

Examples:

- Thermostats
- Cameras
- Security systems

---

## Manufacturing

Examples:

- Machine monitoring
- Equipment diagnostics
- Predictive maintenance

---

## Healthcare

Examples:

- Patient monitoring
- Wearable devices
- Medical telemetry

---

## Utilities

Examples:

- Smart meters
- Leak monitoring
- Pressure monitoring

---

## Transportation

Examples:

- GPS tracking
- Fleet monitoring
- Fuel monitoring
- Vehicle diagnostics

---

# Fleet Intelligence Platform Connections

This architecture closely mirrors a modern fleet telemetry solution.

Potential design:

```text
Vehicle GPS Device
          ↓
 MQTT Publisher
          ↓
 Mosquitto Broker
          ↓
 ThingsBoard
          ↓
 Firebase
          ↓
 Fleet Dashboard
```

Potential telemetry:

```json
{
  "vehicle_id": "SCG001",
  "latitude": 33.875,
  "longitude": -118.090,
  "speed": 62,
  "fuel_level": 74
}
```

Potential alerts:

```text
Vehicle Offline

Speed Threshold Exceeded

Fuel Theft Alert

Maintenance Alert
```

---

# Key Terms

| Term | Definition |
|----------|-------------|
| Firebase | Google's cloud development platform |
| Realtime Database | Realtime NoSQL cloud database |
| ThingsBoard | Open-source IoT platform |
| Device Management | Managing connected IoT devices |
| Telemetry | Live sensor/device data |
| Dashboard | Data visualization interface |
| Widget | Dashboard component |
| Rule Engine | Workflow processing system |
| Alarm | Threshold-triggered event |
| Docker Container | Isolated application runtime |

---

# My Key Takeaways

- Firebase provides cloud-based realtime storage for telemetry data.
- The Firebase Realtime Database stores data using a JSON structure.
- ThingsBoard is the central IoT management and processing platform used in this project.
- Docker simplifies ThingsBoard deployment and configuration.
- ThingsBoard handles device management, telemetry collection, visualization, and alerting.
- Firebase serves as the storage layer while ThingsBoard provides processing and monitoring capabilities.
- These technologies establish the foundation for Project 24.1 and closely resemble real-world IoT and telemetry architectures.