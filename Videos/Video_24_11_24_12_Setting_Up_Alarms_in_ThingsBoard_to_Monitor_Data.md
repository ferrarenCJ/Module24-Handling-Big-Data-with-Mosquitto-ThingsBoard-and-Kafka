# Setting Up Alarms in ThingsBoard to Monitor Data
## Videos 24.11 and 24.12

---

# Overview

These videos extend the telemetry pipeline constructed in Project 24.1 (Part 1) by introducing alarm processing and monitoring capabilities.

Previously, the focus was:

```text
Generate Telemetry
       ↓
ThingsBoard
       ↓
Firebase
```

This section introduces:

```text
Generate Telemetry
       ↓
Monitor Telemetry
       ↓
Trigger Alarms
       ↓
Send Alarms to Firebase
```

The goal is to detect threshold violations and automatically generate notifications when incoming telemetry reaches abnormal values.

---

# Prerequisite

Before completing this section, Project 24.1 (Part 1) should already be functioning.

Required components:

✅ Mosquitto

✅ MQTT Publisher

✅ ThingsBoard

✅ Firebase

✅ DHT11 Demo Device

✅ Temperature Telemetry

✅ Humidity Telemetry

---

# Video 24.11
## Setting Up Alarms in ThingsBoard to Monitor Data - Part 1

### Duration

5:11

---

# Objective

Create an Alarm Rule Chain capable of monitoring incoming telemetry and generating alarms when threshold conditions are met.

---

# Alarm Monitoring Architecture

```text
Telemetry Source
        ↓
Root Rule Chain
        ↓
Alarm Rule Chain
        ↓
Create Alarm
        ↓
Notification
```

---

# Why Alarms Matter

Real-world telemetry systems often require immediate notification when abnormal behavior occurs.

Examples:

---

## Utilities

```text
Pressure Too High

Pressure Too Low

Potential Leak Event
```

---

## Manufacturing

```text
Machine Overheating

Operational Fault
```

---

## Smart Buildings

```text
Excessive Temperature

Excessive Humidity
```

---

## Fleet Operations

```text
High Speed

Low Fuel

Vehicle Offline
```

---

# Alarm Rule Chain Review

Created in Mini-Lesson 24.5.

Structure:

```text
Input
   ↓
TempThreshold
   ├── True
   │      ↓
   │  ClearAlarm
   │
   └── False
          ↓
      CreateAlarm
```

---

# Telemetry Evaluation

Incoming telemetry:

```json
{
    "temperature": 18
}
```

Result:

```text
Clear Alarm
```

---

Incoming telemetry:

```json
{
    "temperature": 28
}
```

Result:

```text
Create Alarm
```

---

# Alarm Logic

Threshold:

```text
Temperature > 20°C
```

Condition met:

```text
Alarm Generated
```

Condition cleared:

```text
Alarm Removed
```

---

# Alarm Lifecycle

```text
Telemetry
      ↓
Threshold Check
      ↓
Create Alarm
      ↓
Alarm Active
      ↓
Condition Clears
      ↓
Clear Alarm
```

---

# Example

Temperature readings:

```text
18
19
21
23
27
```

At:

```text
21
```

Alarm becomes active.

---

Readings:

```text
22
20
18
17
```

At:

```text
18
```

Alarm is cleared.

---

# ThingsBoard Alarm Processing

The Rule Engine continuously evaluates incoming telemetry.

```text
DHT11 Device
      ↓
Temperature Data
      ↓
Threshold Evaluation
      ↓
Alarm State
```

---

# Video 24.12
## Setting Up Alarms in ThingsBoard to Monitor Data - Part 2

### Duration

5:07

---

# Objective

Send alarm information to Firebase using Rule Chains.

---

# Updated Architecture

Part 1:

```text
Telemetry
      ↓
Firebase
```

---

Part 2:

```text
Telemetry
      ↓
Alarm Processing
      ↓
Firebase
```

---

# Alarm-Driven Pipeline

```text
Device
   ↓
Telemetry
   ↓
Root Rule Chain
   ↓
Alarm Rule Chain
   ↓
Firebase
```

---

# Firebase Integration

The Alarm Rule Chain can write notifications and alarm information to Firebase.

Examples:

```json
{
    "temperature": 95,
    "alarm":
    "High Temperature"
}
```

---

# Example Alarm Event

Telemetry:

```json
{
    "temperature": 92
}
```

Threshold:

```text
20
```

Evaluation:

```text
92 > 20
```

Result:

```json
{
    "alarm": "ACTIVE",
    "temperature": 92
}
```

Sent to Firebase.

---

# Alarm Notification Workflow

```text
Temperature Reading
       ↓
Threshold Check
       ↓
Create Alarm
       ↓
Firebase
       ↓
Consumer Applications
```

---

# Why Send Alarms to Firebase?

Benefits:

### Cloud Storage

Persistent alarm history.

---

### Real-Time Monitoring

Immediate notifications.

---

### Mobile Applications

Future mobile dashboards can read alarms.

---

### Historical Analysis

Track recurring operational issues.

---

# Sample Firebase Data

```json
{
    "temperature": 98,
    "humidity": 67,
    "alarm":
    "High Temperature"
}
```

---

# Root Rule Chain Integration

The Alarm Rule Chain must be attached to the Root Rule Chain.

Workflow:

```text
Root Rule Chain
        ↓
Alarm Rule Chain
        ↓
Firebase
```

---

# Alarm Processing Flow

```text
Incoming Telemetry
         ↓
Root Rule Chain
         ↓
Alarm Rule Chain
         ↓
Create Alarm
         ↓
Firebase
```

---

# Telemetry and Alarm Separation

Telemetry:

```text
Temperature

Humidity
```

Tracks measurements.

---

Alarms:

```text
Temperature Threshold Exceeded

Humidity Threshold Exceeded
```

Track conditions.

---

# Real-World Applications

---

## Energy Utilities

Monitor:

```text
Pressure

Flow

Cathodic Protection
```

Generate:

```text
Critical Pressure Alarm
```

---

## Manufacturing

Monitor:

```text
Equipment Temperature
```

Generate:

```text
Overheat Alarm
```

---

## Healthcare

Monitor:

```text
Patient Telemetry
```

Generate:

```text
Critical Condition Alarm
```

---

## Transportation

Monitor:

```text
Vehicle Telemetry
```

Generate:

```text
Maintenance Alert
```

---

# Connection to Project 24.1 Part 2

Project 24.1 (Part 2) extends the architecture developed here.

Students will:

✅ Create Alarm Rule Chain

✅ Connect to Root Rule Chain

✅ Monitor incoming telemetry

✅ Trigger alarms

✅ Send alarms to Firebase

✅ Verify alarm processing

---

# Fleet Intelligence Platform Connections

These alarm concepts map directly to enterprise fleet management.

Examples:

---

## Overspeed Alarm

```json
{
    "vehicle": "SCG001",
    "speed": 82
}
```

Rule:

```text
Speed > 75
```

Result:

```text
Overspeed Alarm
```

---

## Fuel Theft Alarm

```json
{
    "fuel_level": 5
}
```

Rule:

```text
Fuel Level < 10
```

Result:

```text
Fuel Theft Alert
```

---

## Maintenance Alert

```json
{
    "engine_hours": 500
}
```

Rule:

```text
Engine Hours Threshold Reached
```

Result:

```text
Maintenance Notification
```

---

# Key Concepts Reinforced

| Concept | Description |
|----------|-------------|
| Alarm | Notification triggered by telemetry conditions |
| Alarm Rule Chain | Dedicated alarm-processing workflow |
| TempThreshold | Script evaluating telemetry values |
| Create Alarm | Generates alarm conditions |
| Clear Alarm | Removes resolved alarms |
| Root Rule Chain | Primary telemetry workflow |
| Firebase | Destination for telemetry and alarms |
| Telemetry | Streaming sensor data |
| Event Processing | Automated response to conditions |

---

# End-to-End Architecture

```text
TBPublish.py
      ↓
MQTT
      ↓
Mosquitto
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

# My Key Takeaways

- Alarms allow ThingsBoard to automatically monitor live telemetry streams.
- Alarm Rule Chains evaluate incoming telemetry and generate events when thresholds are exceeded.
- Create Alarm and Clear Alarm nodes manage the alarm lifecycle.
- Alarm information can be transmitted to Firebase for storage and monitoring.
- Alarm processing transforms telemetry systems from passive monitoring platforms into active event-driven systems.
- These concepts are widely used in IoT, manufacturing, utilities, transportation, and fleet management environments.
- The architecture developed in these videos directly supports Required Project 24.1 (Part 2).