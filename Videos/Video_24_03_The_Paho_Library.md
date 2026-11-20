# Mini-Lesson 24.2: The Paho Library

---

# Overview

This lesson introduces the Paho MQTT Python library, which provides an easy way to connect Python applications to an MQTT broker such as Mosquitto.

Using Paho, developers can:

- Connect to MQTT brokers
- Publish messages
- Subscribe to topics
- Process incoming messages
- Build real-time IoT applications

The Paho library is the Python implementation of MQTT client functionality.

---

# What is the Paho Library?

The Eclipse Paho Python library implements the MQTT protocol in Python.

It provides a client class that allows Python applications to:

- Connect to MQTT brokers
- Send messages
- Receive messages
- Manage MQTT sessions

Architecture:

```text
Python Application
         ↓
    Paho Client
         ↓
  MQTT Protocol
         ↓
 Mosquitto Broker
         ↓
Subscriber Clients
```

---

# Installing Paho

The module uses Paho MQTT Version 1.

Install using:

```cmd
pip install "paho-mqtt<2.0.0"
```

or

```cmd
pip install paho-mqtt<2.0.0
```

---

# The MQTT Client Class

The core of the Paho library is the MQTT Client class.

Import:

```python
import paho.mqtt.client as mqtt
```

Create a client:

```python
client = mqtt.Client()
```

The client object provides all MQTT functionality.

---

# Connecting to Mosquitto

Assuming a Mosquitto Docker container is running locally:

```python
import paho.mqtt.client as mqtt

broker_url = "localhost"
broker_port = 1883

client = mqtt.Client()
client.connect(broker_url, broker_port)
```

---

## Connection Components

### Broker URL

```python
broker_url = "localhost"
```

Specifies where the broker is running.

---

### Port

```python
broker_port = 1883
```

Default MQTT port.

Common ports:

| Port | Purpose |
|--------|--------|
| 1883 | MQTT |
| 8883 | MQTT over SSL/TLS |

---

# Publishing Messages

Once connected, messages can be sent to a topic.

Example:

```python
topic = "module24/learning_paho"
payload = "publishing a message"

client.publish(topic, payload)
```

---

## Publish Components

### Topic

```python
module24/learning_paho
```

Defines the communication channel.

---

### Payload

```python
publishing a message
```

The message being transmitted.

---

## Publish Workflow

```text
Python Application
         ↓
Paho publish()
         ↓
Mosquitto Broker
         ↓
Subscribed Clients
```

---

# Subscribing to Topics

Clients can subscribe to topics to receive messages.

Example:

```python
client.subscribe(topic)
```

---

## Subscribe Workflow

```text
Subscriber
     ↓
subscribe(topic)
     ↓
Mosquitto Broker
     ↓
Receive Messages
```

---

# Callback Functions

Paho uses callback functions to react to events.

Callbacks execute automatically when certain actions occur.

Examples:

| Event | Callback |
|---------|---------|
| Client connects | on_connect |
| Message arrives | on_message |
| Client disconnects | on_disconnect |

---

# The on_message Callback

The on_message callback executes whenever a message is received.

Example:

```python
def on_message(client, userdata, message):
    print(
        "Message received: "
        + message.payload.decode()
    )
```

---

## Parameters

### client

MQTT client instance.

### userdata

Custom user data.

### message

Contains:

- Topic
- Payload
- QoS information

---

## Processing Incoming Messages

Example:

```text
Topic:
sensors/temperatures

Payload:
{"temperature":72}
```

Output:

```text
Message received: {"temperature":72}
```

---

# The on_connect Callback

Executed when a connection to the broker succeeds.

Example:

```python
def on_connect(client, userdata, flags, rc):
    print(
        "connected with result code "
        + str(rc)
    )

    client.subscribe(topic)
```

---

## Purpose

Automatically subscribe after connecting.

Without this callback, subscriptions would have to be created manually.

---

## Result Codes

Common values:

| Code | Meaning |
|--------|---------|
| 0 | Success |
| 1 | Incorrect protocol version |
| 2 | Invalid client identifier |
| 3 | Server unavailable |
| 4 | Bad username/password |
| 5 | Not authorized |

---

# Registering Callback Functions

After creating the callback functions:

```python
client.on_connect = on_connect
client.on_message = on_message
```

The client now responds automatically to:

- New connections
- Incoming messages

---

# End-to-End MQTT Example

## Publisher

```text
Generate Temperature
         ↓
 Publish Message
         ↓
   Mosquitto Broker
```

---

## Subscriber

```text
 Subscribe Topic
         ↓
 Receive Message
         ↓
 Print Message
```

---

# Example 1: MQTT Publisher

File:

```text
pahopublish.py
```

Purpose:

Simulates a temperature sensor.

---

## Publisher Code

```python
import paho.mqtt.client as mqtt

import json
import time
import random

topic = 'sensors/temperatures'
broker = "localhost"
port = 1883

client = mqtt.Client()

client.connect(
    broker,
    port,
    60
)

print(f"connected on {port}")

for i in range(100):

    data = json.dumps(
        {
            "temperature":
            random.randint(0,100)
        }
    )

    client.publish(
        topic,
        data
    )

    print(
        f"published: {data}"
    )

    time.sleep(1)

client.disconnect()
```

---

# Publisher Workflow

The publisher:

1. Connects to Mosquitto
2. Generates random temperatures
3. Converts values to JSON
4. Publishes data
5. Waits one second
6. Repeats 100 times

---

## Sample Output

```text
published:
{"temperature":34}

published:
{"temperature":78}

published:
{"temperature":62}
```

---

# Example 2: MQTT Subscriber

File:

```text
pahosubscribe.py
```

Purpose:

Listen for temperature data.

---

## Subscriber Code

```python
import paho.mqtt.client as mqtt

port = 1883
broker = "localhost"

topic = 'sensors/temperatures'

def on_connect(
    client,
    userdata,
    flags,
    rc
):

    print(
        "Connected with result code "
        + str(rc)
    )

    client.subscribe(topic)

def on_message(
    client,
    userdata,
    msg
):

    print(
        msg.topic
        + " "
        + str(msg.payload)
    )

client = mqtt.Client()

client.on_connect = on_connect
client.on_message = on_message

client.connect(
    broker,
    port,
    60
)

client.loop_forever()
```

---

# loop_forever()

The subscriber runs continuously.

```python
client.loop_forever()
```

Purpose:

- Wait for incoming messages
- Process messages as they arrive
- Keep the application running

This is common in real-time streaming systems.

---

# Running the Demo

## Terminal 1

Start subscriber:

```cmd
python pahosubscribe.py
```

Expected:

```text
Connected with result code 0
```

Program waits for messages.

---

## Terminal 2

Start publisher:

```cmd
python pahopublish.py
```

Publisher begins generating temperatures.

---

## Subscriber Output

```text
sensors/temperatures
{"temperature":45}

sensors/temperatures
{"temperature":89}

sensors/temperatures
{"temperature":32}
```

---

# Understanding the Message Flow

```text
Temperature Sensor
      ↓
pahopublish.py
      ↓
Paho MQTT Client
      ↓
Mosquitto Broker
      ↓
Paho Subscriber
      ↓
pahosubscribe.py
      ↓
Console Output
```

---

# Project 24.1 Connection

In Project 24.1 Part 1, this exact architecture will be expanded.

Current lesson:

```text
Publisher
    ↓
Mosquitto
    ↓
Subscriber
```

Project architecture:

```text
Temperature Sensor
Humidity Sensor
        ↓
Mosquitto Broker
        ↓
ThingsBoard
        ↓
Firebase
```

---

# Why Paho is Important for Data Engineers

Paho simplifies IoT streaming development.

Common use cases:

- Sensor telemetry
- Smart devices
- Vehicle tracking
- Utility monitoring
- Industrial IoT
- Event-driven architectures

Data engineers frequently use MQTT clients to move data into:

- Kafka
- Spark Streaming
- Databases
- Dashboards
- Alerting systems

---

# Fleet Intelligence Platform Connections

This lesson directly applies to a future fleet telemetry architecture.

Example:

```text
Vehicle GPS Device
         ↓
Paho Client
         ↓
MQTT Broker
         ↓
Kafka
         ↓
Fleet Platform
         ↓
Dashboards
```

Potential vehicle telemetry payload:

```json
{
  "vehicle_id": "TRUCK001",
  "latitude": 33.875,
  "longitude": -118.098,
  "speed": 55
}
```

---

# Key Terms

| Term | Definition |
|--------|------------|
| Paho | Eclipse MQTT client library |
| MQTT Client | Application connected to a broker |
| Broker | Message routing server |
| Mosquitto | MQTT broker implementation |
| Publish | Send a message |
| Subscribe | Receive messages |
| Topic | MQTT communication channel |
| Payload | Data carried by a message |
| Callback Function | Function triggered by an event |
| on_connect | Callback executed after connecting |
| on_message | Callback executed when a message arrives |
| loop_forever() | Continuous event-processing loop |

---

# My Key Takeaways

- Paho provides Python support for MQTT communication.
- The MQTT Client class is the foundation of Paho applications.
- Publishers send data to topics using publish().
- Subscribers receive data using subscribe().
- Callback functions handle connection and messaging events.
- on_connect() manages subscriptions.
- on_message() processes incoming data.
- loop_forever() keeps subscribers listening continuously.
- Paho and Mosquitto form the foundation for real-time IoT data streaming systems.
- The architecture in this lesson will be expanded in Project 24.1 using ThingsBoard and Firebase.