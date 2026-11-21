# Video 24.10: ThingsBoard Exercise Solution

## Duration

5:52

---

# Overview

This video presents the solution to the ThingsBoard exercise introduced in Videos 24.7 through 24.9 and serves as a walkthrough for **Required Project 24.1 (Part 1)**.

The project objective was to create an end-to-end IoT streaming pipeline capable of:

1. Generating temperature data
2. Generating humidity data
3. Publishing telemetry through MQTT
4. Receiving telemetry in ThingsBoard
5. Displaying telemetry in dashboards
6. Sending telemetry to Firebase

---

# Project 24.1 (Part 1) Recap

The project combines several technologies:

- Mosquitto
- MQTT
- Paho MQTT Library
- ThingsBoard
- Firebase
- Docker

---

# Final Architecture

```text
TBPublish.py
      │
      ▼
MQTT Publisher
      │
      ▼
Mosquitto Broker
      │
      ▼
ThingsBoard
      │
      ▼
DHT11 Demo Device
      │
      ▼
Firebase Realtime Database
```

---

# Exercise Objective

The exercise required students to expand the existing telemetry solution.

Originally:

```json
{
    "temperature": 75
}
```

The exercise required adding:

```json
{
    "temperature": 75,
    "humidity": 92
}
```

---

# Step 1: Modify Sensor Data Structure

Original:

```python
sensor_data = {
    "temperature": 0
}
```

Modified:

```python
sensor_data = {
    "temperature": 0,
    "humidity": 0
}
```

---

# Step 2: Generate Humidity Data

Temperature was already being generated.

Additional code:

```python
humidity = random.randint(50, 100)
```

Example:

```text
Temperature: 76
Humidity: 88
```

---

# Step 3: Publish Combined Telemetry

Resulting payload:

```json
{
    "temperature": 76,
    "humidity": 88
}
```

Published through MQTT:

```python
client.publish(
    "v1/devices/me/telemetry",
    json.dumps(sensor_data),
    1
)
```

---

# Step 4: Verify MQTT Telemetry

Telemetry must be visible within:

```text
ThingsBoard
```

Device:

```text
DHT11 Demo Device
```

Latest Telemetry should display:

```text
temperature

humidity
```

with continuously updating values.

---

# Step 5: Display Telemetry Using Widgets

ThingsBoard widgets visualize telemetry.

Examples:

- Gauge
- Table
- Timeseries Line Chart
- KPI Card

The exercise uses a:

```text
Timeseries Line Chart
```

to display temperature trends.

---

# Example Visualization

```text
28°
26°        *
24°      *   *
22°    *       *
20°  *
18°
```

---

# Step 6: Configure Firebase

Create:

```text
module24Project
```

inside Firebase.

---

# Create Realtime Database

Enable:

```text
Realtime Database
```

Example structure:

```json
{
    "temperature": 0,
    "humidity": 0
}
```

---

# Step 7: Connect ThingsBoard to Firebase

Within the Root Rule Chain:

Add:

```text
REST API Call Node
```

Named:

```text
Firebase
```

---

# Endpoint

Example:

```text
https://module24project-xxxxx-default-rtdb.firebaseio.com/.json
```

---

# Connection

```text
Message Type Switch
          │
          ▼
       Firebase
```

Link label:

```text
Post telemetry
```

---

# Step 8: Verify Firebase Updates

Successful integration results in telemetry appearing inside Firebase.

Example:

```json
{
    "temperature": 57,
    "humidity": 65
}
```

```json
{
    "temperature": 98,
    "humidity": 68
}
```

```json
{
    "temperature": 74,
    "humidity": 92
}
```

---

# Data Flow Through the System

Telemetry lifecycle:

```text
Temperature Sensor
Humidity Sensor
         │
         ▼
   MQTT Publisher
         │
         ▼
 Mosquitto Broker
         │
         ▼
   ThingsBoard
         │
         ▼
 Root Rule Chain
         │
         ▼
 Firebase
```

---

# Technologies Demonstrated

## MQTT

Responsible for:

```text
Publish / Subscribe Communication
```

---

## Mosquitto

Responsible for:

```text
Broker Functionality
```

---

## Paho

Responsible for:

```text
MQTT Client Communication
```

---

## ThingsBoard

Responsible for:

```text
Telemetry Processing

Visualization

Rule Chains

Integrations
```

---

## Firebase

Responsible for:

```text
Realtime Cloud Storage
```

---

# Common Troubleshooting Topics

This exercise may expose issues related to:

### MQTT Configuration

```text
Connection Refused
```

---

### Docker Container Startup

```text
Port Conflicts

Missing Images
```

---

### ThingsBoard Configuration

```text
Missing Telemetry

Improper Rule Chain Routes
```

---

### Firebase Connectivity

Examples:

```text
Authentication Errors

REST API Configuration

SSL Certificate Validation
```

---

# Real-World Applications

The completed architecture is representative of production IoT environments.

Examples:

## Smart Buildings

```text
Temperature Monitoring

Humidity Monitoring
```

---

## Utilities

```text
Pressure Telemetry

Leak Detection

Smart Metering
```

---

## Manufacturing

```text
Equipment Monitoring

Predictive Maintenance
```

---

## Fleet Operations

```text
Vehicle Tracking

Fuel Monitoring

Engine Diagnostics
```

---

# Fleet Intelligence Platform Connections

The architecture built in this project closely resembles a fleet telemetry platform.

Potential implementation:

```text
Vehicle GPS Unit
          │
          ▼
       MQTT
          │
          ▼
     Mosquitto
          │
          ▼
    ThingsBoard
          │
          ▼
      Firebase
          │
          ▼
 Fleet Dashboard
```

---

# Example Vehicle Payload

```json
{
    "vehicle_id": "SCG001",
    "latitude": 33.875,
    "longitude": -118.090,
    "speed": 62,
    "fuel_level": 74
}
```

---

# Key Concepts Reinforced

| Concept | Purpose |
|----------|----------|
| MQTT | Publish/Subscribe messaging |
| Mosquitto | MQTT broker |
| Paho | Python MQTT client |
| Telemetry | Streaming sensor data |
| ThingsBoard | IoT processing platform |
| Widget | Dashboard visualization |
| Rule Chain | Event processing workflow |
| Firebase | Realtime cloud database |
| REST API Call Node | External integration layer |

---

# Key Learning Outcomes

Successfully demonstrated:

✅ MQTT publishing

✅ Mosquitto message routing

✅ Telemetry generation

✅ ThingsBoard ingestion

✅ Dashboard visualization

✅ Firebase integration

✅ End-to-end IoT streaming

---

# My Key Takeaways

- ThingsBoard serves as the processing and visualization layer between MQTT telemetry and cloud storage.
- Temperature and humidity data can be generated, streamed, displayed, and stored in real time.
- Rule Chains provide an extensible method for integrating external systems.
- Firebase serves as a simple cloud destination for telemetry storage.
- The overall architecture reflects many real-world IoT and telemetry solutions used in utilities, manufacturing, transportation, and fleet management.
- Required Project 24.1 (Part 1) establishes the foundation for Part 2, where alarm processing and monitoring capabilities will be added.