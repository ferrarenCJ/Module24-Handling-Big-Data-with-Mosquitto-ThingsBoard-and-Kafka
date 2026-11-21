# Mini-Lesson 24.5: Setting Up Alarms in ThingsBoard

---

# Overview

This lesson introduces alarm management in ThingsBoard.

As IoT environments generate continuous streams of telemetry data, it becomes important to automatically detect abnormal conditions and notify users when threshold values are exceeded.

Examples include:

- Temperature too high
- Temperature too low
- High pressure
- Low fuel level
- Device offline
- Excessive speed

ThingsBoard provides alarm capabilities through custom Rule Chains that evaluate incoming telemetry and automatically trigger or clear alarms.

---

# What Are Alarms in ThingsBoard?

An alarm is a notification mechanism that alerts users when telemetry reaches a predefined threshold or condition.

Example:

A thermostat continuously sends temperature readings.

```text
18°C
20°C
21°C
24°C
28°C
```

If a threshold is configured:

```text
Temperature > 20°C
```

Then ThingsBoard can automatically create an alarm whenever the condition becomes true.

---

# Why Alarms Matter

Without alarms:

```text
Sensor
   ↓
Dashboard
```

A user must manually monitor the data.

With alarms:

```text
Sensor
   ↓
Rule Chain
   ↓
Alarm
   ↓
Notification
```

The system monitors itself and reports abnormal conditions automatically.

---

# Common Alarm Use Cases

## Smart Buildings

```text
High Temperature

High Humidity

HVAC Failure
```

---

## Manufacturing

```text
Machine Overheating

Pressure Above Limit

Equipment Failure
```

---

## Utilities

```text
Pressure Threshold Exceeded

Gas Leak Detection

Flow Rate Abnormalities
```

---

## Transportation

```text
Vehicle Overspeed

Low Fuel

Vehicle Offline
```

---

# How Are Alarms Created?

ThingsBoard uses:

```text
Custom Rule Chains
```

to evaluate telemetry and determine when alarms should be triggered.

Alarm processing follows:

```text
Telemetry
      ↓
Alarm Rule Chain
      ↓
Create Alarm
      ↓
Notify Users
```

---

# Alarm Rule Chain

A dedicated Rule Chain is created specifically for alarm handling.

Name:

```text
Alarms
```

---

# Creating the Alarm Rule Chain

Navigate:

```text
Rule Chains
```

↓

```text
+
Create New Rule Chain
```

---

## Name

```text
Alarms
```

---

## Result

```text
Alarm Rule Chain
```

created successfully.

---

# Alarm Rule Chain Structure

Final structure:

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

# Input Node

The Input Node is automatically created.

Purpose:

```text
Receive incoming telemetry
```

Examples:

```json
{
    "temperature": 18
}
```

```json
{
    "temperature": 28
}
```

---

# TempThreshold Node

## Node Type

```text
Script Node
```

---

## Name

```text
TempThreshold
```

---

## Purpose

Evaluate incoming telemetry.

Example:

```text
temperature > 20
```

---

## Logic

Temperature less than threshold:

```text
TRUE
```

Temperature above threshold:

```text
FALSE
```

The threshold can be modified as needed.

Examples:

```text
20°C
25°C
30°C
```

---

# Script Node Function

The script evaluates telemetry values and determines which path should be followed inside the Rule Chain.

Workflow:

```text
Temperature
      ↓
Threshold Evaluation
      ↓
True / False
```

---

# Connecting Input and TempThreshold

Create relation:

```text
Input
   ↓
TempThreshold
```

This allows telemetry to enter the alarm workflow.

---

# Clear Alarm Node

## Node Type

```text
Clear Alarm
```

---

## Name

```text
ClearAlarm
```

---

## Purpose

Remove previously generated alarms when telemetry returns to a normal state.

Example:

```text
Temperature Alarm Active
```

Later:

```text
Temperature Returns to Normal
```

Alarm should automatically clear.

---

# Clear Alarm Script

```javascript
var details = {};

if (metadata.prevAlarmDetails) {

    details =
        JSON.parse(
            metadata.prevAlarmDetails
        );
}

return details;
```

---

# What the Script Does

Checks whether a previous alarm exists.

If found:

```text
Load prior alarm details
```

then clear the alarm.

---

# Connect TempThreshold → ClearAlarm

Relation:

```text
TempThreshold
       ↓
   ClearAlarm
```

Link Label:

```text
True
```

---

# Create Alarm Node

## Node Type

```text
Create Alarm
```

---

## Name

```text
CreateAlarm
```

---

## Purpose

Generates a new alarm when threshold conditions are met.

Example:

```text
Temperature = 28°C

Threshold = 20°C
```

Result:

```text
High Temperature Alarm
```

---

# Create Alarm Script

```javascript
var details = {};

if (metadata.prevAlarmDetails) {

    details =
        JSON.parse(
            metadata.prevAlarmDetails
        );
}

return details;
```

---

# Connect TempThreshold → CreateAlarm

Relation:

```text
TempThreshold
       ↓
  CreateAlarm
```

Link Label:

```text
False
```

---

# Completed Alarm Rule Chain

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

# Alarm Processing Example

Incoming telemetry:

```json
{
    "temperature": 18
}
```

Result:

```text
ClearAlarm
```

---

Incoming telemetry:

```json
{
    "temperature": 26
}
```

Result:

```text
CreateAlarm
```

---

# Connecting Alarms to the Root Rule Chain

The Alarm Rule Chain will later be attached to the:

```text
Root Rule Chain
```

Workflow:

```text
Telemetry
     ↓
Root Rule Chain
     ↓
Alarm Rule Chain
     ↓
Create Alarm
```

---

# Firebase Integration

Eventually:

```text
Telemetry
      ↓
Alarm Rule Chain
      ↓
Firebase
```

---

# Example Alarm Event

Incoming telemetry:

```json
{
    "temperature": 95
}
```

Generated alarm:

```json
{
    "alarm":
    "High Temperature",

    "temperature":
    95
}
```

Sent to:

```text
Firebase
```

---

# Relationship to Project 24.1 Part 2

Part 2 extends Part 1.

Part 1 focused on:

```text
Producing Telemetry
```

---

Part 2 focuses on:

```text
Monitoring Telemetry
```

---

Part 2 Workflow

```text
TBPublish.py
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

# Why Data Engineers Use Alarms

Alarms provide:

## Data Monitoring

Detect unusual values.

---

## Data Quality Validation

Identify telemetry problems.

---

## Operational Awareness

Provide immediate visibility.

---

## Automated Response

Trigger additional workflows.

---

# Real-World Examples

## Utility Industry

```text
Pressure > Threshold
```

Generate:

```text
High Pressure Alarm
```

---

## Manufacturing

```text
Machine Temperature > Limit
```

Generate:

```text
Maintenance Alert
```

---

## Smart Buildings

```text
Humidity > Limit
```

Generate:

```text
Environmental Alert
```

---

## Fleet Management

```text
Speed > 75 MPH
```

Generate:

```text
Overspeed Alarm
```

---

# Fleet Intelligence Platform Connections

The same alarm concepts apply directly to fleet telemetry.

Potential alarms:

```text
Fuel Theft

Vehicle Offline

Overspeed Event

Geofence Violation

Maintenance Due
```

---

# Example Fleet Rule Chain

```text
Vehicle Telemetry
        ↓
 Speed Threshold
        ↓
 Create Alarm
        ↓
 Dashboard Alert
```

---

# Example Telemetry

```json
{
    "vehicle_id": "SCG001",
    "speed": 82
}
```

Result:

```text
Overspeed Alarm
```

---

# Key Terms

| Term | Definition |
|--------|------------|
| Alarm | Notification generated from telemetry conditions |
| Alarm Rule Chain | Workflow used to process alarms |
| Threshold | Condition that triggers an alarm |
| Script Node | JavaScript processing node |
| Clear Alarm | Removes an active alarm |
| Create Alarm | Generates a new alarm |
| Input Node | Receives incoming telemetry |
| Root Rule Chain | Main processing workflow |
| Telemetry | Streaming sensor data |

---

# My Key Takeaways

- ThingsBoard alarms allow automated monitoring of telemetry data.
- Alarm Rule Chains evaluate incoming data and trigger notifications based on threshold conditions.
- Script nodes determine whether alarm conditions are met.
- Create Alarm nodes generate new alarms when abnormal conditions occur.
- Clear Alarm nodes automatically remove resolved alarms.
- Alarm Rule Chains connect to the Root Rule Chain to monitor live telemetry streams.
- These same concepts are widely used in IoT, utility monitoring, industrial automation, and fleet management platforms.
- The Alarm Rule Chain created in this lesson forms the foundation for Required Project 24.1 (Part 2).