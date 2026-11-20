# Streaming Data Using ThingsBoard
## Videos 24.7 - 24.9

---

# Overview

These videos focus on the visualization and integration capabilities of ThingsBoard.

In this section, the telemetry generated and processed in the previous lessons is:

1. Visualized using ThingsBoard widgets
2. Exported from ThingsBoard to Firebase
3. Extended into a practical project involving temperature and humidity sensors

At this point, the architecture evolves into a complete IoT streaming platform:

```text
Sensor
   ↓
MQTT
   ↓
Mosquitto
   ↓
ThingsBoard
   ↓
Dashboard
   ↓
Firebase
```

---

# Video 24.7
## Setting Up a Widget in ThingsBoard

### Duration

1:32

---

# What is a Widget?

A widget is a dashboard component used to display telemetry data inside ThingsBoard.

Widgets allow users to monitor device data visually in real time.

Examples:

- Line charts
- Gauges
- Bar charts
- Tables
- Maps
- Alarm indicators

---

# Purpose

The purpose of this video is to display temperature telemetry on a Timeseries Line Chart.

Previously:

```text
Temperature Data
       ↓
ThingsBoard
```

Now:

```text
Temperature Data
       ↓
ThingsBoard
       ↓
Line Chart Widget
```

---

# Timeseries Line Chart

The Timeseries Line Chart visualizes telemetry values over time.

Example:

```text
Temperature
28 |
26 |
24 |        *
22 |      *   *
20 |   *        *
18 | *
   +------------------
      Time
```

---

# Widget Setup Process

## Step 1

Open:

```text
Dashboards
```

---

## Step 2

Create or open a dashboard.

Example:

```text
Temperature Dashboard
```

---

## Step 3

Add Widget.

```text
+
Add Widget
```

---

## Step 4

Select:

```text
Timeseries
```

---

## Step 5

Select:

```text
Line Chart
```

---

## Step 6

Bind the widget to:

```text
Thermometer A
```

---

## Step 7

Select telemetry field:

```text
temperature
```

---

# Result

The dashboard updates automatically as new telemetry arrives.

Example:

```text
20.5°C

21.1°C

22.7°C

24.0°C
```

---

# Why Widgets Matter

Widgets make telemetry actionable.

Benefits:

- Real-time monitoring
- Historical analysis
- Operational awareness
- Alert visibility

---

# Real-World Example

Facility managers could monitor:

```text
Building Temperature
```

Utilities could monitor:

```text
Gas Pressure
```

Fleet managers could monitor:

```text
Vehicle Speed
Fuel Levels
GPS Activity
```

---

# Video 24.8
## Pumping Data from ThingsBoard to Firebase

### Duration

4:46

---

# Objective

Transfer telemetry generated and processed within ThingsBoard to Firebase.

---

# Architecture

```text
Device
   ↓
ThingsBoard
   ↓
Firebase Realtime Database
```

---

# Why Firebase?

Firebase serves as a cloud-based storage platform.

Advantages:

- Realtime synchronization
- Cloud hosting
- Easy integration
- Dashboard compatibility
- Mobile/web support

---

# Before This Video

Data exists only within ThingsBoard.

```text
Device
   ↓
ThingsBoard
```

---

# After This Video

Data is shared with Firebase.

```text
Device
   ↓
ThingsBoard
   ↓
Firebase
```

---

# Typical Workflow

## Receive Telemetry

Example:

```json
{
    "temperature": 23.4
}
```

---

## Process Telemetry

Rule Engine:

```text
Root Rule Chain
```

---

## Send Telemetry

Output:

```text
Firebase Realtime Database
```

---

# Example Data

Incoming telemetry:

```json
{
    "temperature": 24.8
}
```

Stored in Firebase:

```json
{
  "temperature": 24.8
}
```

---

# Benefits of Firebase Integration

## Persistent Storage

Data remains available after processing.

---

## Historical Analysis

Review historical measurements.

---

## External Applications

Allow mobile and web apps to consume telemetry.

---

## Alerting

Future alarms can easily be stored and monitored.

---

# End-to-End Telemetry Flow

```text
Temperature Sensor
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

# Video 24.9
## ThingsBoard Exercise

### Duration

1:57

---

# Exercise Objective

Build a system capable of:

1. Generating temperature telemetry
2. Generating humidity telemetry
3. Sending telemetry into ThingsBoard
4. Forwarding telemetry to Firebase

---

# Telemetry Sources

The exercise introduces two sensor types.

---

## Temperature Sensor

Example:

```json
{
  "temperature": 22.0
}
```

---

## Humidity Sensor

Example:

```json
{
  "humidity": 45
}
```

---

# Combined Telemetry

Example:

```json
{
  "temperature": 22.0,
  "humidity": 45
}
```

---

# Target Architecture

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
Firebase
```

---

# Skills Practiced

## MQTT Publishing

Generating telemetry data.

---

## ThingsBoard Processing

Receiving telemetry.

---

## Widget Visualization

Displaying telemetry.

---

## Firebase Integration

Persisting telemetry.

---

# Connection to Required Project 24.1

The exercise directly prepares students for Project 24.1 Part 1.

Project architecture:

```text
Temperature Sensor
Humidity Sensor
          ↓
Mosquitto
          ↓
ThingsBoard
          ↓
Firebase
```

---

# Project 24.1 Deliverables

Students must demonstrate:

✅ MQTT telemetry generation

✅ Mosquitto broker operation

✅ ThingsBoard telemetry ingestion

✅ Temperature data visualization

✅ Humidity data visualization

✅ Firebase connectivity

✅ Telemetry storage

---

# Real-World Applications

## Smart Buildings

Telemetry:

```text
Temperature
Humidity
Occupancy
```

---

## Manufacturing

Telemetry:

```text
Machine Health
Equipment Temperature
Production Metrics
```

---

## Agriculture

Telemetry:

```text
Soil Moisture
Humidity
Temperature
```

---

## Utilities

Telemetry:

```text
Pressure
Flow
Leak Detection
Consumption
```

---

## Fleet Management

Telemetry:

```text
GPS
Speed
Fuel Level
Engine Diagnostics
```

---

# Fleet Intelligence Platform Connections

This architecture strongly resembles a modern fleet telemetry environment.

Potential design:

```text
Vehicle Device
         ↓
 MQTT
         ↓
 Mosquitto
         ↓
 ThingsBoard
         ↓
 Firebase
         ↓
 Fleet Dashboard
```

---

# Example Vehicle Telemetry

```json
{
  "vehicle_id": "SCG001",
  "speed": 62,
  "fuel_level": 74,
  "latitude": 33.875,
  "longitude": -118.090
}
```

---

# Potential Future Widgets

### Speed Widget

```text
62 MPH
```

---

### Fuel Widget

```text
74%
```

---

### GPS Map Widget

```text
Vehicle Location
```

---

### Alarm Widget

```text
Vehicle Offline

Maintenance Due

Fuel Theft Alert
```

---

# Combined ThingsBoard Workflow

```text
Telemetry Generator
         ↓
 MQTT Broker
         ↓
 ThingsBoard
         ↓
 Root Rule Chain
         ↓
 Dashboards
         ↓
 Firebase
```

---

# Key Concepts

| Concept | Description |
|----------|-------------|
| Widget | Dashboard visualization component |
| Timeseries Chart | Graph showing values over time |
| Telemetry | Streaming device data |
| Firebase | Cloud-hosted realtime database |
| Dashboard | Collection of widgets |
| ThingsBoard | IoT management platform |
| MQTT | Publish/Subscribe protocol |
| Mosquitto | MQTT broker |
| Root Rule Chain | Primary telemetry workflow |

---

# My Key Takeaways

- Widgets provide real-time visualization of telemetry data.
- Timeseries charts are ideal for monitoring sensor readings over time.
- ThingsBoard can forward telemetry to Firebase for persistent cloud storage.
- Firebase serves as a central repository for telemetry generated by IoT systems.
- Temperature and humidity telemetry are the foundation for Project 24.1.
- This architecture closely mirrors real-world streaming, monitoring, and telemetry platforms used in utilities, manufacturing, healthcare, and fleet management.