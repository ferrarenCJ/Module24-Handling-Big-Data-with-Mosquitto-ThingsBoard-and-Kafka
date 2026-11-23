# Module 24 Cheat Sheet
# Handling Big Data with Mosquitto, ThingsBoard, and Kafka

---

# Module 24 Architecture Overview

## MQTT / ThingsBoard

```text
TBPublish.py
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

## Alarm Processing

```text
Telemetry
     ↓
Root Rule Chain
     ↓
CreateAndClearAlarms
     ↓
AlarmToFirebase
     ↓
Firebase
```

---

## Kafka Architecture

```text
Python Producer
       ↓
Kafka Topic
       ↓
Kafka Broker
       ↓
Node.js Consumer
       ↓
Web Server
       ↓
Browser
```

---

# MQTT Cheat Sheet

## Install Paho

```cmd
pip install "paho-mqtt<2.0.0"
```

---

## Connect to Broker

```python
import paho.mqtt.client as mqtt

client = mqtt.Client()

client.connect(
    "localhost",
    1883,
    60
)
```

---

## Publish

```python
client.publish(
    "topic",
    payload
)
```

---

## Subscribe

```python
client.subscribe(topic)
```

---

## on_connect

```python
def on_connect(
    client,
    userdata,
    flags,
    rc
):
    client.subscribe(topic)
```

---

## on_message

```python
def on_message(
    client,
    userdata,
    msg
):
    print(msg.payload)
```

---

## Continuous Listener

```python
client.loop_forever()
```

---

# Mosquitto Cheat Sheet

## Docker Start

```cmd
docker compose up -d
```

---

## Check Containers

```cmd
docker ps
```

---

## View Logs

```cmd
docker logs broker
```

---

## Stop Container

```cmd
docker compose down
```

---

# Firebase Cheat Sheet

## Firebase URL Pattern

```text
https://<project>.firebaseio.com/.json
```

---

## Alarm Endpoint

```text
https://<project>.firebaseio.com/alarm.json
```

---

## Temperature Endpoint

```text
https://<project>.firebaseio.com/temperature.json
```

---

## Manual Test

```cmd
curl -k -X PUT ^
-H "Content-Type: application/json" ^
-d "{\"temperature\":99}" ^
"https://<project>.firebaseio.com/.json"
```

---

## Reset Database

```json
{
  "alarm": {},
  "humidity": 0,
  "temperature": 0
}
```

---

# ThingsBoard Cheat Sheet

## Login

```text
URL:
http://localhost:8080

User:
tenant@thingsboard.org

Password:
tenant
```

---

# Devices

Example:

```text
DHT11 Demo Device
```

---

# Root Rule Chain

Required Nodes:

```text
Input

Message Type Switch

Save Attributes

Log RPC from Device

Log Other

RPC Call Request

Save Timeseries

Rule Chain
```

---

# CreateAndClearAlarms Rule Chain

```text
Input
   ↓
TempThreshold

True  → CreateAlarm

True  → TempToFirebase

False → ClearAlarm

CreateAlarm
      ↓ Created
AlarmToFirebase
```

---

# TempThreshold

```javascript
return msg.temperature > 20;
```

---

# CreateAlarm Details Script

```javascript
var details = {};

if (metadata.prevAlarmDetails != null) {

    details =
        JSON.parse(
            metadata.prevAlarmDetails
        );

    metadata.remove(
        'prevAlarmDetails'
    );
}

return details;
```

---

# ClearAlarm Details Script

```javascript
var details = {};

if (metadata.prevAlarmDetails != null) {

    details =
        JSON.parse(
            metadata.prevAlarmDetails
        );
}

return details;
```

---

# TempToFirebase

## Endpoint

```text
https://module24project-xxxxx.firebaseio.com/temperature.json
```

---

# AlarmToFirebase

## Endpoint

```text
https://module24project-xxxxx.firebaseio.com/alarm.json
```

---

# Alarm Verification

ThingsBoard:

```text
Notifications
```

Displays:

```text
New alarm "General Alarm"

Alarm "General Alarm" - cleared
```

---

Firebase:

```json
alarm
 └── General Alarm
```

---

# SSL Certificate Fix

## Problem

```text
PKIX path building failed

SSLHandshakeException
```

---

## Root Cause

```text
Sempra Energy Utilities Root Authority SHA2
```

not trusted inside Docker Java runtime.

---

## Export Certificate

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

## Copy to Container

```cmd
docker cp SempraRoot.cer thingsboard-mytb-1:/tmp/
```

---

## Import Into Truststore

```bash
keytool -importcert \
-alias sempra-root \
-file /tmp/SempraRoot.cer \
-keystore /usr/lib/jvm/java-17-openjdk-amd64/lib/security/cacerts \
-storepass changeit \
-noprompt
```

---

## Restart ThingsBoard

```cmd
docker restart thingsboard-mytb-1
```

---

# Kafka Cheat Sheet

## Start Kafka Cluster

```cmd
docker compose up -d
```

---

## Access Confluent Control Center

```text
http://localhost:9021
```

---

## Create Topic

```text
vehicle-coordinates
```

Partitions:

```text
1
```

---

# Kafka Producer

## Install

```cmd
pip install kafka-python
```

---

## Producer Payload

```json
{
    "longitude": 127,
    "latitude": 50
}
```

---

## Generate Coordinates

```python
longitude =
random.randint(
    -180,
    180
)

latitude =
random.randint(
    -90,
    90
)
```

---

# Kafka Topic

```python
topic_name =
'vehicle-coordinates'
```

---

# KafkaJS Consumer

## Install

```cmd
npm install kafkajs
```

---

## Why KafkaJS?

Used instead of:

```text
node-rdkafka
```

because:

```text
node-gyp

Visual Studio Build Tools

Desktop Development with C++
```

were unavailable.

---

# KafkaJS Import

```javascript
const { Kafka } =
require('kafkajs');
```

---

# Node.js

## Verify Install

```cmd
node --version
```

---

## Install Dependencies

```cmd
npm install

npm install kafkajs
```

---

# Start Server

```cmd
node server.js
```

Expected:

```text
Listening on 5000
```

---

# Web Page

```text
http://localhost:5000
```

Button:

```text
Consume Vehicle Coordinates
```

---

# Consumer Output

```text
Consumed value
{"longitude":46,"latitude":-20}

Consumed value
{"longitude":55,"latitude":63}
```

---

# Project 24.1 Part 1

✅ MQTT → ThingsBoard → Firebase

---

# Project 24.1 Part 2

✅ Alarm Processing → Firebase

---

# Project 24.2

✅ Kafka Producer

✅ Kafka Consumer

✅ Web Server

✅ Browser Integration

---

# Module 24 Key Commands

## MQTT

```cmd
python TBPublish.py
```

---

## Kafka Producer

```cmd
python PublishVehicleCoordinates.py
```

---

## Node Server

```cmd
node server.js
```

---

## Kafka Containers

```cmd
docker ps
```

---

## Kafka Logs

```cmd
docker logs broker
```

---

# Module 24 Summary

✅ Mosquitto

✅ MQTT

✅ ThingsBoard

✅ Rule Chains

✅ Alarm Chains

✅ Firebase

✅ Kafka

✅ Producers

✅ Consumers

✅ Node.js

✅ Express

✅ KafkaJS

✅ Streaming Architectures

✅ SSL Troubleshooting