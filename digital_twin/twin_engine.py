
# NEXUS Digital Twin Engine

from datetime import datetime, timezone

# Stores the latest state of each virtual device
digital_twins = {}


def update_twin(data):
    """
    Updates the virtual machine using incoming sensor data.
    """

    device_id = data["device_id"]

    digital_twins[device_id] = {
        "device_id": device_id,
        "temperature": data["temperature"],
        "vibration": data["vibration"],
        "rpm": data["rpm"],
        "last_updated": datetime.now(timezone.utc).isoformat()
    }

    print("\n DIGITAL TWIN UPDATED!")
    print(digital_twins[device_id])


def get_twin(device_id):
    """
    Returns the latest state of a virtual machine.
    """

    return digital_twins.get(device_id)


def get_all_twins():
    """
    Returns all virtual machines.
    """

    return digital_twins
