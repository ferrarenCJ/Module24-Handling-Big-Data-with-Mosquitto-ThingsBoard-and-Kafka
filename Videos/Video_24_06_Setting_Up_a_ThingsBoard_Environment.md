# Video 24.6: Setting Up a ThingsBoard Environment

## Duration

7:27

---

# Overview

In this video, Dr. Williams demonstrates how to configure a ThingsBoard environment and simulate an IoT device that generates temperature telemetry.

The objective is to create a complete telemetry simulation inside ThingsBoard without requiring a physical sensor. This simulated device will generate random temperature readings and send them through a ThingsBoard Rule Chain.

This exercise establishes the foundation for:

- Required Project 24.1 Part 1
- Required Project 24.1 Part 2
- Telemetry generation
- Rule Chain processing
- Dashboard visualization
- Alarm generation

---

# Learning Objectives

By completing this exercise, I should be able to:

- Configure a ThingsBoard environment
- Create devices and assets
- Create a Rule Chain
- Simulate telemetry data
- Generate temperature readings
- Send telemetry through ThingsBoard
- Understand how ThingsBoard processes incoming messages

---

# Environment Architecture

The simulated environment follows the architecture below:

```text
Temperature Generator
          ↓
 Thermostat Rule Chain
          ↓
  Root Rule Chain
          ↓
      Device
          ↓
    Dashboard
```

---

# Simulating an IoT Device

Instead of connecting a real thermometer, ThingsBoard uses a script to generate synthetic telemetry.

The simulated device acts like:

```text
Outdoor Temperature Sensor
```

and continuously produces readings.

Example outputs:

```text
18.5°C

22.1°C

26.4°C

19.3°C
```

---

# Thermostat Rule Chain

The video introduces a custom Rule Chain named:

```text
Thermostat
```

This rule chain generates random temperatures and passes them into ThingsBoard for processing.

Purpose:

- Simulate device telemetry
- Test dashboards
- Test alarms
- Test Rule Engine workflows

---

# Temperature Generation Script

The following JavaScript is used inside ThingsBoard.

```javascript
var msg = {
    temperature: (18 + 10 * Math.random()).toFixed(1)
};

return {
    msg: msg,
    metadata: {
        deviceType: "outdoor thermometer"
    },
    msg_Type: "POST_TELEMETRY_REQUEST"
};
```

---

# Understanding the Code

## Step 1

Generate a random temperature.

```javascript
18 + 10 * Math.random()
```

Produces a value between:

```text
18.0
and
28.0
```

---

## Step 2

Format the value.

```javascript
.toFixed(1)
```

Rounds the result to one decimal place.

Examples:

```text
18.4

22.8

27.1
```

---

## Step 3

Create telemetry data.

```javascript
msg = {
    temperature: value
}
```

Example:

```json
{
  "temperature": "24.7"
}
```

---

## Step 4

Add metadata.

```javascript
metadata: {
    deviceType:
    "outdoor thermometer"
}
```

Metadata provides descriptive information about the device.

---

## Step 5

Specify message type.

```javascript
POST_TELEMETRY_REQUEST
```

This tells ThingsBoard:

```text
Treat this message
as telemetry
```

---

# Sample Message

Generated output:

```json
{
  "temperature": "22.4"
}
```

Metadata:

```json
{
  "deviceType":
  "outdoor thermometer"
}
```

---

# Telemetry Flow

Generated temperature:

```text
22.4
```

Processing workflow:

```text
Thermostat Rule Chain
           ↓
      Root Rule Chain
           ↓
         Device
           ↓
      Dashboard
```

---

# Root Rule Chain

The Root Rule Chain is the primary entry point for all telemetry.

Responsibilities:

- Receive data
- Process messages
- Apply transformations
- Route messages
- Forward to additional rule chains

---

# Message Processing Example

Incoming telemetry:

```json
{
  "temperature": "26.2"
}
```

Processing:

```text
Root Rule Chain
       ↓
Store Telemetry
       ↓
Device
       ↓
Dashboard
```

---

# Device Configuration

Earlier lessons introduced device creation.

Example device:

```text
Thermometer A
```

Label:

```text
Therm A
```

The generated telemetry is routed to this device.

---

# Device Telemetry Example

A device timeline might show:

| Time | Temperature |
|--------|------------|
| 10:00 | 18.6 |
| 10:01 | 20.4 |
| 10:02 | 22.1 |
| 10:03 | 24.9 |
| 10:04 | 21.7 |

---

# Why Simulate Data?

Simulation provides a controlled environment for testing.

Benefits:

- No physical hardware required
- Repeatable testing
- Faster development
- Easier debugging
- Safe experimentation

---

# Applications of Simulated Telemetry

Examples:

### Smart Buildings

```text
Temperature Sensors
Humidity Sensors
```

---

### Utilities

```text
Pressure Monitoring
Flow Monitoring
Gas Sensors
```

---

### Manufacturing

```text
Equipment Temperature
Machine Health
```

---

### Fleet Operations

```text
Vehicle Sensors
Fuel Sensors
GPS Devices
```

---

# Relationship to Project 24.1 Part 1

This exercise provides the telemetry generation concepts required for:

## Streaming Live Data to ThingsBoard

Workflow:

```text
MQTT Publisher
      ↓
Mosquitto Broker
      ↓
ThingsBoard
      ↓
Firebase
```

Instead of randomly generated temperatures inside ThingsBoard, Project 24.1 will receive telemetry from MQTT devices.

---

# Relationship to Project 24.1 Part 2

Part 2 introduces alarm processing.

Example:

```text
Temperature > 26
```

Could trigger:

```text
High Temperature Alert
```

Workflow:

```text
Telemetry
     ↓
Root Rule Chain
     ↓
Alarm Rule Chain
     ↓
Firebase
```

---

# Real-World Example

Imagine a smart building containing:

```text
Building A
```

Assets:

```text
Building A
```

Devices:

```text
Thermometer A

Humidity Sensor B

Pressure Sensor C
```

Generated temperature:

```text
27.8°C
```

ThingsBoard:

- Receives telemetry
- Processes telemetry
- Displays telemetry
- Generates alerts if needed

---

# Fleet Intelligence Platform Connections

This video is very similar to telemetry simulations we may eventually build for the Fleet Intelligence Platform.

Potential simulation:

```text
Vehicle Telemetry Generator
           ↓
 ThingsBoard Rule Chain
           ↓
 Dashboard
```

Generated data:

```json
{
  "vehicle_id": "SCG001",
  "speed": 62,
  "fuel_level": 74,
  "latitude": 33.875,
  "longitude": -118.090
}
```

Possible alert:

```text
Speed > 75 MPH
```

or

```text
Fuel Level < 10%
```

---

# Key Terms

| Term | Definition |
|--------|------------|
| ThingsBoard | Open-source IoT platform |
| Telemetry | Streaming sensor data |
| Device | Telemetry source |
| Rule Chain | Workflow for processing messages |
| Root Rule Chain | Primary processing workflow |
| Metadata | Descriptive device information |
| POST_TELEMETRY_REQUEST | Telemetry message type |
| Thermostat Rule Chain | Simulated temperature generator |
| Dashboard | Visualization interface |

---

# Code Reference

```javascript
var msg = {
    temperature: (18 + 10 * Math.random()).toFixed(1)
};

return {
    msg: msg,
    metadata: {
        deviceType: "outdoor thermometer"
    },
    msg_Type: "POST_TELEMETRY_REQUEST"
};
```

Purpose:

- Generate random temperatures
- Create telemetry messages
- Simulate an outdoor thermometer
- Pass data into ThingsBoard

---

# My Key Takeaways

- ThingsBoard can simulate IoT devices without requiring physical hardware.
- Rule Chains are used to generate and process telemetry.
- The Thermostat Rule Chain creates random temperatures between approximately 18°C and 28°C.
- Telemetry enters the Root Rule Chain for processing.
- Generated telemetry can be attached to devices and visualized on dashboards.
- This simulation environment serves as the foundation for Project 24.1 and future alarm-processing workflows.