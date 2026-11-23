# Project 24.1 Part 1
# Streaming Live Data to ThingsBoard

## Objective

Create a real-time telemetry pipeline using:

- MQTT
- Mosquitto
- ThingsBoard
- Firebase

## File

```text
TBPublish.py
```

## Telemetry

```json
{
  "temperature": 76,
  "humidity": 93
}
```

## Architecture

```text
TBPublish.py
      ↓
Mosquitto
      ↓
ThingsBoard
      ↓
Firebase
```

## Outcome

✅ Temperature Telemetry

✅ Humidity Telemetry

✅ Firebase Storage