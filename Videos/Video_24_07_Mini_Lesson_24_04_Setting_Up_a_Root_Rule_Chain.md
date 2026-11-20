# Mini-Lesson 24.4: Setting Up a Root Rule Chain in ThingsBoard

---

# Overview

This lesson demonstrates how to configure a Root Rule Chain in ThingsBoard.

The Root Rule Chain is the central processing workflow responsible for:

- Receiving telemetry
- Routing messages
- Saving data
- Logging events
- Triggering additional Rule Chains
- Forwarding data for further processing

Every message received by ThingsBoard passes through the Root Rule Chain before being processed elsewhere.

---

# Learning Objectives

By the end of this lesson, I should be able to:

- Understand the purpose of a Root Rule Chain
- Configure Rule Nodes
- Connect Rule Nodes together
- Route telemetry data
- Store telemetry and attributes
- Forward data to additional Rule Chains
- Validate telemetry generation from a device

---

# What is a Root Rule Chain?

A Root Rule Chain is the primary workflow inside the ThingsBoard Rule Engine.

Responsibilities include:

### Data Ingestion

Receive telemetry from devices.

### Message Routing

Direct messages to the correct processing path.

### Data Storage

Store telemetry and attributes.

### Event Processing

Trigger alerts and automation workflows.

### Rule Chain Integration

Forward data to other Rule Chains.

---

# Root Rule Chain Architecture

```text
Device
   ↓
Input Node
   ↓
Message Type Switch
   ↓
Storage / Logging / RPC
   ↓
Additional Rule Chains
```

---

# Required Rule Nodes

The course configuration requires eight nodes.

| Node | Purpose |
|---------|---------|
| Input | Receives incoming messages |
| Message Type Switch | Routes messages |
| Save Attributes | Stores attributes |
| Log RPC from Device | Logs RPC events |
| Log Other | Logs unmatched events |
| RPC Call Request | Sends commands to devices |
| Save Timeseries | Stores telemetry |
| Rule Chain | Forwards data to Thermostat Rule Chain |

---

# Complete Rule Chain Diagram

```text
Input
  ↓
Message Type Switch
   ├── Post Attributes
   │         ↓
   │   Save Attributes
   │
   ├── RPC Request from Device
   │         ↓
   │   Log RPC from Device
   │
   ├── RPC Request to Device
   │         ↓
   │   RPC Call Request
   │
   ├── Other
   │         ↓
   │   Log Other
   │
   └── Post Telemetry
             ↓
      Save Timeseries
             ↓
         Rule Chain
         (Thermostat)
```

---

# Step 1: Open Root Rule Chain

Navigate to:

```text
Rule Chains
```

from the ThingsBoard navigation menu.

---

Select:

```text
Root Rule Chain
```

---

Open:

```text
Open Rule Chain
```

---

# Existing Nodes

The Root Rule Chain may already contain:

```text
Input Node
```

This node receives incoming device data.

---

# Input Node

## Purpose

The Input Node is the entry point into the Rule Engine.

Receives:

- Device telemetry
- Device attributes
- RPC requests

---

# Step 2: Add Message Type Switch Node

Search for:

```text
Message Type Switch
```

---

Drag into the Rule Engine.

---

Name:

```text
Message Type Switch
```

---

Select:

```text
Add
```

---

# Purpose

The Message Type Switch acts as a filter node.

It determines where incoming data should go.

Examples:

```text
Telemetry
```

Route to:

```text
Save Timeseries
```

---

```text
Attributes
```

Route to:

```text
Save Attributes
```

---

```text
RPC
```

Route to:

```text
RPC Processing
```

---

# Connect Nodes

Create connection:

```text
Input
   ↓
Message Type Switch
```

---

# Step 3: Add Save Attributes Node

Search:

```text
Save Attributes
```

---

Create node.

---

Name:

```text
Save Attributes
```

---

Set:

```text
Entity Attributes Scope
```

to:

```text
Server Attributes
```

---

# Purpose

Stores attributes in the ThingsBoard database.

Example:

```json
{
  "device_type":
  "thermometer"
}
```

---

# Connect Nodes

Connect:

```text
Message Type Switch
          ↓
   Save Attributes
```

Label:

```text
Post Attributes
```

---

# Step 4: Add Log RPC from Device Node

Search:

```text
Log
```

---

Create node.

---

Name:

```text
Log RPC from Device
```

---

# Purpose

Logs RPC requests originating from devices.

Example:

```text
Turn Sensor On

Turn Sensor Off
```

---

# Connect Nodes

```text
Message Type Switch
          ↓
Log RPC from Device
```

Label:

```text
RPC Request from Device
```

---

# Step 5: Add Log Other Node

Create another Log node.

---

Name:

```text
Log Other
```

---

# Purpose

Captures uncategorized messages.

Useful for:

- Debugging
- Monitoring
- Troubleshooting

---

# Connect Nodes

```text
Message Type Switch
          ↓
      Log Other
```

Label:

```text
Other
```

---

# Step 6: Add RPC Call Request Node

Search:

```text
RPC Call Request
```

---

Create node.

---

Name:

```text
RPC Call Request
```

---

# What is RPC?

RPC stands for:

```text
Remote Procedure Call
```

RPC allows ThingsBoard to send commands to devices.

---

Example

ThingsBoard:

```text
Restart Device
```

---

Device:

```text
Returns Success
```

---

# Connect Nodes

```text
Message Type Switch
          ↓
RPC Call Request
```

Label:

```text
RPC Request to Device
```

---

# Step 7: Add Save Timeseries Node

Search:

```text
Save Timeseries
```

---

Create node.

---

Name:

```text
Save Timeseries
```

---

# Purpose

Stores telemetry data.

Examples:

```json
{
  "temperature": 21.5
}
```

```json
{
  "humidity": 44
}
```

---

Stored as:

```text
Time-Series Data
```

---

# Connect Nodes

```text
Message Type Switch
          ↓
   Save Timeseries
```

Label:

```text
Post Telemetry
```

---

# Step 8: Add Rule Chain Node

Search:

```text
Rule Chain
```

---

Create node.

---

Name:

```text
Rule Chain
```

---

Select:

```text
Thermostat
```

from:

```text
Rule Chain Dropdown
```

---

# Purpose

Forwards telemetry to the Thermostat Rule Chain.

---

# Connect Nodes

```text
Save Timeseries
        ↓
      Rule Chain
```

Label:

```text
Success
```

---

# Save Configuration

Select:

```text
✔ Checkmark
```

in the bottom-right corner.

---

Configuration is now active.

---

# Verifying Telemetry

Navigate:

```text
Devices
```

---

Open:

```text
Thermometer A
```

---

Open:

```text
Latest Telemetry
```

---

Expected output:

```text
temperature = 18.7

temperature = 22.4

temperature = 25.1

temperature = 20.3
```

Values should continuously update.

---

# End-to-End Flow

Once configured:

```text
Thermostat Rule Chain
          ↓
     Root Rule Chain
          ↓
   Message Routing
          ↓
   Save Timeseries
          ↓
     Device View
          ↓
      Dashboard
```

---

# Relationship to Project 24.1 Part 1

In Part 1:

```text
Mosquitto
      ↓
ThingsBoard
      ↓
Firebase
```

The Root Rule Chain processes incoming MQTT telemetry before forwarding it downstream.

---

# Relationship to Project 24.1 Part 2

In Part 2:

```text
Telemetry
     ↓
Root Rule Chain
     ↓
Alarm Rule Chain
     ↓
Firebase
```

The Root Rule Chain becomes the entry point for alarm processing.

---

# Why Data Engineers Need to Understand Rule Chains

Rule Chains form the backbone of ThingsBoard workflows.

Real-world uses:

### Smart Buildings

```text
Temperature Monitoring
```

### Utilities

```text
Pressure Monitoring
```

### Manufacturing

```text
Equipment Monitoring
```

### Fleet Tracking

```text
GPS Telemetry Processing
```

---

# Fleet Intelligence Platform Connections

Root Rule Chains resemble event-processing pipelines used in fleet systems.

Example:

```text
Vehicle Telemetry
          ↓
     Root Rule Chain
          ↓
  Speed Validation
          ↓
 Fuel Monitoring
          ↓
 Alert Generation
```

---

Telemetry Example:

```json
{
  "vehicle_id": "SCG001",
  "speed": 78,
  "fuel_level": 12
}
```

Rule Processing:

```text
Speed > 75
```

Generate:

```text
Overspeed Alert
```

---

# Key Terms

| Term | Definition |
|--------|------------|
| Root Rule Chain | Main ThingsBoard processing workflow |
| Rule Node | Individual processing component |
| Message Type Switch | Routes messages |
| Save Attributes | Stores attributes |
| Save Timeseries | Stores telemetry |
| Log Node | Logs messages |
| RPC | Remote Procedure Call |
| Rule Chain Node | Forwards data to another Rule Chain |
| Telemetry | Streaming device data |
| Device | Source of telemetry |

---

# My Key Takeaways

- The Root Rule Chain is the central processing workflow in ThingsBoard.
- Every incoming device message enters through the Input Node.
- The Message Type Switch routes messages to the appropriate processing path.
- Save Attributes stores metadata while Save Timeseries stores telemetry.
- Log Nodes help with monitoring and debugging.
- RPC Call Request nodes support device command and control.
- Rule Chain Nodes allow modular processing by forwarding messages to additional workflows.
- Understanding Rule Chains is critical for designing scalable IoT data pipelines and event-driven systems.