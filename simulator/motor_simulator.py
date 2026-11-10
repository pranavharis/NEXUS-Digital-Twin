
import json
import time
import random
import paho.mqtt.client as mqtt

# MQTT broker details
BROKER = "broker.hivemq.com"
PORT = 1883

# Motor communication topic
TOPIC = "nexus/demo/MOTOR001/telemetry"

# Create MQTT publisher
client = mqtt.Client(
    callback_api_version=mqtt.CallbackAPIVersion.VERSION2
)

# Connect to broker
client.connect(BROKER, PORT, 60)

print("Motor Simulator Started!")
print("Sending live motor data to NEXUS...")

# Continuously generate sensor readings
while True:

    motor_data = {
        "device_id": "MOTOR001",
        "temperature": round(random.uniform(50, 80), 2),
        "vibration": round(random.uniform(1, 5), 2),
        "rpm": random.randint(1200, 1800),
        "timestamp": time.time()
    }

    # Convert Python data into JSON
    message = json.dumps(motor_data)

    # Publish data to MQTT broker
    client.publish(TOPIC, message)

    print("Published:", motor_data)

    # Send data every 2 seconds
    time.sleep(2)
