# MQTT Publisher

## Purpose

Publishes telemetry data to MQTT topics.

## Technology

- Python
- Paho MQTT
- Mosquitto

## Workflow

```text
Python
   ↓
MQTT Topic
   ↓
Mosquitto
```

## Example Payload

```json
{
  "temperature": 78
}
```

## File

```text
pahopublish.py
```