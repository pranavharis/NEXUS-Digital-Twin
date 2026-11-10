
import json
import paho.mqtt.client as mqtt

from digital_twin.twin_engine import DigitalTwin


# MQTT configuration
BROKER = "localhost"
PORT = 1883
TOPIC = "nexus/motor/001/telemetry"

# Create the virtual industrial motor
twin = DigitalTwin("NEXUS_MOTOR_001")


# Called when connected to MQTT
def on_connect(client, userdata, flags, reason_code, properties):

    if reason_code == 0:
        print("NEXUS connected to MQTT Broker!")

        client.subscribe(TOPIC)
        print("Subscribed to:", TOPIC)

    else:
        print("MQTT connection failed:", reason_code)


# Called whenever machine data arrives
def on_message(client, userdata, message):

    try:
        # Convert incoming JSON into Python data
        machine_data = json.loads(message.payload.decode())

        print("\nMACHINE DATA RECEIVED")

        # Update the Digital Twin
        twin.update(machine_data)

        # Display the updated virtual machine
        twin.display()

    except (ValueError, KeyError, TypeError) as error:
        print("Invalid machine data:", error)


# Create MQTT client
client = mqtt.Client(
    callback_api_version=mqtt.CallbackAPIVersion.VERSION2,
    client_id="NEXUS_DIGITAL_TWIN"
)

# Register MQTT callbacks
client.on_connect = on_connect
client.on_message = on_message


# Start subscriber
def start_subscriber():

    print("Connecting to NEXUS MQTT Broker...")

    client.connect(BROKER, PORT, 60)

    print("NEXUS Digital Twin Engine Started!")

    client.loop_forever()


if __name__ == "__main__":
    start_subscriber()
