
import random
import time
import json
from datetime import datetime

import paho.mqtt.client as mqtt


# MQTT broker configuration
BROKER = "localhost"
PORT = 1883

# Machine identification
MACHINE_ID = "NEXUS_MOTOR_001"

# MQTT communication topic
TOPIC = "nexus/motor/001/telemetry"


# Create MQTT publisher
client = mqtt.Client(
    callback_api_version=mqtt.CallbackAPIVersion.VERSION2,
    client_id="NEXUS_MOTOR"
)


def main():

    print("Connecting motor to NEXUS MQTT broker...")

    client.connect(BROKER, PORT, 60)
    client.loop_start()

    print("NEXUS Motor Simulator Started!")
    print("Sending live motor data to NEXUS...")

    try:
        while True:

            # Generate industrial motor readings
            machine_data = {
                "machine_id": MACHINE_ID,
                "temperature": round(random.uniform(55, 75), 2),
                "vibration": round(random.uniform(1, 5), 2),
                "rpm": random.randint(1350, 1500),
                "current": round(random.uniform(3, 6), 2),
                "status": "RUNNING",
                "timestamp": datetime.now().astimezone().isoformat()
            }

            # Convert Python dictionary into JSON
            payload = json.dumps(machine_data)

            # Publish readings to MQTT broker
            result = client.publish(
                TOPIC,
                payload,
                qos=1
            )

            result.wait_for_publish()

            print("DATA SENT TO NEXUS:", payload)

            # Generate new readings every second
            time.sleep(1)

    except KeyboardInterrupt:
        print("\nMotor simulator stopped.")

    finally:
        client.loop_stop()
        client.disconnect()


if __name__ == "__main__":
    main()
