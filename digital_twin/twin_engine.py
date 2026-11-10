
# NEXUS Digital Twin Engine

from datetime import datetime, timezone

# Stores all virtual machines
digital_twins = {}


class DigitalTwin:

    def __init__(self, machine_id):

        self.machine_id = machine_id

        self.state = {
            "machine_id": machine_id,
            "temperature": 0,
            "vibration": 0,
            "rpm": 0,
            "current": 0,
            "status": "OFFLINE",
            "last_updated": None
        }

    # Update virtual machine using sensor data
    def update(self, machine_data):

        self.state["temperature"] = machine_data["temperature"]
        self.state["vibration"] = machine_data["vibration"]
        self.state["rpm"] = machine_data["rpm"]
        self.state["current"] = machine_data.get("current", 0)
        self.state["status"] = machine_data.get("status", "UNKNOWN")

        self.state["last_updated"] = datetime.now(
            timezone.utc
        ).isoformat()

    # Display virtual machine state
    def display(self):

        print("\n========== NEXUS DIGITAL TWIN ==========")

        print("Machine ID:", self.machine_id)
        print("Temperature:", self.state["temperature"])
        print("Vibration:", self.state["vibration"])
        print("RPM:", self.state["rpm"])
        print("Current:", self.state["current"])
        print("Status:", self.state["status"])
        print("Last Updated:", self.state["last_updated"])

        print("========================================")


# Multi-device Digital Twin update function
def update_twin(data):

    # Support both device_id and machine_id
    device_id = data.get("device_id") or data.get("machine_id")

    if not device_id:
        raise ValueError("Machine ID is missing")

    # Create a twin if it doesn't already exist
    if device_id not in digital_twins:
        digital_twins[device_id] = DigitalTwin(device_id)

    # Update the corresponding virtual machine
    twin = digital_twins[device_id]
    twin.update(data)

    print("\nDIGITAL TWIN UPDATED!")
    twin.display()


# Retrieve one virtual machine
def get_twin(device_id):

    twin = digital_twins.get(device_id)

    return twin.state if twin else None


# Retrieve all virtual machines
def get_all_twins():

    return {
        machine_id: twin.state
        for machine_id, twin in digital_twins.items()
    }
