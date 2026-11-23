# Project 24.1 Part 2
# Analyzing Live Streaming Data Using ThingsBoard

## Objective

Create an alarm-processing workflow using Rule Chains.

## Rule Chains

### CreateAndClearAlarms

```text
Input
   ↓
TempThreshold
```

### TempToFirebase

Writes telemetry to Firebase.

### AlarmToFirebase

Writes alarm information to Firebase.

## Architecture

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

## Outcome

✅ Alarm Creation

✅ Alarm Clearing

✅ Firebase Alarm Storage

✅ Real-Time Monitoring
