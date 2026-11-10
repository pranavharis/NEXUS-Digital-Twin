
import json
import paho.mqtt.client as mqtt

# Import the NEXUS Digital Twin Engine
from digital_twin.twin_engine import update_twin

BROKER = "broker.hivemq.com"
PORT = 1883

TOPIC = "nexus/demo/MOTOR001/telemetry"


def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code == 0:
        print("NEXUS connected to MQTT broker!")
        client.subscribe(TOPIC)
        print("Subscribed to:", TOPIC)
    else:
        print("MQTT connection failed:", reason_code)


def on_message(client, userdata, message):
    try:
        data = json.loads(message.payload.decode())

        print("\nReceived motor data:")
        print(data)

        # Update the Digital Twin
        update_twin(data)

    except (json.JSONDecodeError, KeyError) as error:
        print("Invalid motor data:", error)


client = mqtt.Client(
    callback_api_version=mqtt.CallbackAPIVersion.VERSION2
)

client.on_connect = on_connect
client.on_message = on_message


def start_subscriber():
    print("Connecting to MQTT broker...")

    client.connect(BROKER, PORT, 60)
    client.loop_forever()


if __name__ == "__main__":

def start_subscriber():
    print("Connecting to MQTT broker...")
    client.connect(BROKER, PORT, 60)
    client.loop_start()
    print("MQTT subscriber started!")


if __name__ == "__main__":
    start_subscriber()
    client.loop_forever()

    start_subscriber()
