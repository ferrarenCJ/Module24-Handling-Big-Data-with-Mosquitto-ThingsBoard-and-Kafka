# Required Project 24.1 (Part 2)
# Analyzing Live Streaming Data Using ThingsBoard

## Module 24
### Handling Big Data with Mosquitto, ThingsBoard, and Kafka

---

# Objective

The objective of Part 2 was to extend the streaming telemetry pipeline developed in Part 1 by introducing alarm processing and monitoring functionality.

This project required:

- Creating alarm processing rule chains
- Monitoring incoming telemetry
- Triggering alarms when conditions are met
- Sending alarm information to Firebase
- Sending telemetry data to Firebase
- Connecting alarm workflows to the Root Rule Chain

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
Root Rule Chain
      │
      ▼
CreateAndClearAlarms
      │
      ├───────────────► TempToFirebase
      │                        │
      │                        ▼
      │                  Firebase
      │                temperature
      │
      └───────────────► CreateAlarm
                                │
                                ▼
                        AlarmToFirebase
                                │
                                ▼
                           Firebase
                              alarm
```

---

# Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | MQTT Publisher |
| Paho MQTT | MQTT Communication |
| Mosquitto | MQTT Broker |
| ThingsBoard | IoT Processing Platform |
| Firebase | Realtime Database |
| Docker | Container Platform |
| Java Rule Chains | Alarm Processing |

---

# Firebase Configuration

## Database Structure

```json
{
    "alarm": {},
    "humidity": 0,
    "temperature": 0
}
```

---

# Rule Chains Created

## 1. CreateAndClearAlarms

Purpose:

```text
Evaluate telemetry
Create alarms
Clear alarms
Send data to other rule chains
```

---

## Components

```text
Input
   ↓
TempThreshold
```

### TempThreshold

```javascript
return msg.temperature > 20;
```

---

## Alarm Handling

```text
TempThreshold
      │
      ├── True
      │      ↓
      │  CreateAlarm
      │
      └── False
             ↓
         ClearAlarm
```

---

## Additional Outputs

```text
TempThreshold
        │
        └── True
               ↓
         TempToFirebase
```

---

## Alarm Workflow

```text
CreateAlarm
       ↓
AlarmToFirebase
```

Relation:

```text
Created
```

---

# 2. TempToFirebase Rule Chain

Purpose:

```text
Send temperature and humidity data
to Firebase
```

---

## Components

```text
Input
   ↓
TempToFirebase
```

---

## REST API Endpoint

```text
https://module24project-1eaef-default-rtdb.firebaseio.com/temperature.json
```

Method:

```text
POST
```

---

# 3. AlarmToFirebase Rule Chain

Purpose:

```text
Send alarm information
to Firebase
```

---

## Components

```text
Input
   ↓
AlarmToFirebase
```

---

## REST API Endpoint

```text
https://module24project-1eaef-default-rtdb.firebaseio.com/alarm.json
```

Method:

```text
POST
```

---

# Root Rule Chain Modifications

Added:

```text
CreateAndClearAlarm
```

Rule Chain Node

Connected:

```text
Save Timeseries
      ↓
CreateAndClearAlarm
```

Relation:

```text
Success
```

---

# Telemetry Processing

Example telemetry:

```json
{
    "temperature": 76,
    "humidity": 95
}
```

---

Processing:

```text
MQTT Publisher
      ↓
ThingsBoard
      ↓
Root Rule Chain
      ↓
CreateAndClearAlarms
```

---

# Alarm Processing

Example:

```json
{
    "temperature": 95,
    "humidity": 87
}
```

Evaluation:

```javascript
return msg.temperature > 20;
```

Result:

```text
CreateAlarm
```

---

Generated Alarm:

```text
General Alarm
Severity: Critical
```

---

# Firebase Alarm Output

Successful alarm records were written to:

```json
alarm
```

Example:

```json
{
    "ackTs": 0,
    "acknowledged": false,
    "assignTs": 0,
    "clearTs": 0,
    "cleared": false,
    "createdTime": 1795400165745,
    "name": "General Alarm",
    "severity": "CRITICAL",
    "status": "ACTIVE_UNACK",
    "type": "General Alarm",
    "originatorName": "DHT11 Demo Device"
}
```

---

# Firebase Telemetry Output

Example telemetry records:

```json
{
    "temperature": 76,
    "humidity": 95
}
```

```json
{
    "temperature": 35,
    "humidity": 93
}
```

```json
{
    "temperature": 27,
    "humidity": 91
}
```

---

# Major Issue Encountered

## Firebase HTTPS Integration Failure

ThingsBoard was unable to communicate with Firebase.

Error:

```text
SSLHandshakeException

PKIX path building failed

unable to find valid certification path to requested target
```

---

# Root Cause

The corporate network was performing SSL inspection using:

```text
Sempra Energy Utilities Root Authority SHA2
```

Certificate chain:

```text
Firebase
      ↓
SEU SSL PA-08
      ↓
Sempra Energy Utilities Enterprise SHA2 CA5
      ↓
Sempra Energy Utilities Root Authority SHA2
```

Java inside the ThingsBoard Docker container did not trust the Sempra certificate chain.

---

# Resolution

## Export Certificate

Windows:

```cmd
certmgr.msc
```

Export:

```text
Sempra Energy Utilities Root Authority SHA2
```

as:

```text
SempraRoot.cer
```

---

## Copy Certificate

```cmd
docker cp SempraRoot.cer thingsboard-mytb-1:/tmp/
```

---

## Import Certificate

```bash
keytool -importcert \
-alias sempra-root \
-file /tmp/SempraRoot.cer \
-keystore /usr/lib/jvm/java-17-openjdk-amd64/lib/security/cacerts \
-storepass changeit \
-noprompt
```

Result:

```text
Certificate was added to keystore
```

---

## Verify Import

```bash
keytool -list \
-keystore /usr/lib/jvm/java-17-openjdk-amd64/lib/security/cacerts \
-storepass changeit | grep -i sempra
```

Result:

```text
sempra-root
```

---

## Restart ThingsBoard

```cmd
docker restart thingsboard-mytb-1
```

After restart:

✅ Firebase connectivity restored

✅ Alarm data transmitted

✅ Telemetry transmitted

---

# Key Learning Outcomes

Successfully demonstrated:

✅ Rule Chain Creation

✅ Alarm Creation

✅ Alarm Clearing

✅ Firebase REST Integration

✅ Telemetry Monitoring

✅ CreateAlarm Workflow

✅ Root Rule Chain Integration

✅ MQTT Streaming Analysis

✅ SSL Truststore Management

✅ End-to-End Alarm Processing

---

# Deliverables Completed

| Step | Status |
|--------|--------|
| Firebase Alarm Field | ✅ |
| CreateAndClearAlarms Rule Chain | ✅ |
| TempToFirebase Rule Chain | ✅ |
| TempToFirebase REST Node | ✅ |
| AlarmToFirebase Rule Chain | ✅ |
| AlarmToFirebase REST Node | ✅ |
| AlarmToFirebase Rule Chain Node | ✅ |
| CreateAlarm → AlarmToFirebase | ✅ |
| TempToFirebase Rule Chain Node | ✅ |
| TempThreshold → TempToFirebase | ✅ |
| CreateAndClearAlarm Root Node | ✅ |
| SaveTimeseries → CreateAndClearAlarm | ✅ |
| Firebase Alarm Data | ✅ |
| Firebase Temperature Data | ✅ |

---

# Project Status

```text
Required Project 24.1 (Part 2)
COMPLETED SUCCESSFULLY
```

---

**Author:** Clifford Ferraren  
**Program:** MIT Professional Education - Applied Data Engineering Program  
**Module:** Module 24 - Handling Big Data with Mosquitto, ThingsBoard, and Kafka