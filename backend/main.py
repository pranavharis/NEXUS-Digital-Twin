
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from digital_twin.twin_engine import get_twin, get_all_twins
from backend.mqtt_subscriber import start_subscriber


# Create the NEXUS application
app = FastAPI(
    title="NEXUS Digital Twin API",
    description="Industrial IoT and Predictive Intelligence Platform",
    version="1.0.0"
)

# Temporary storage for registered devices
devices = {}


# Define the structure of an IoT device
class Device(BaseModel):
    device_id: str
    name: str
    machine_type: str = "motor"
    location: Optional[str] = None
    status: str = "offline"


# Home route
@app.get("/")
def home():
    return {
        "message": "Welcome to NEXUS Digital Twin Platform",
        "status": "Backend is running"
    }


# Health check
@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "project": "NEXUS"
    }


# Register a new IoT device
@app.post("/devices")
def register_device(device: Device):

    if device.device_id in devices:
        raise HTTPException(
            status_code=400,
            detail="Device already registered"
        )

    devices[device.device_id] = device

    return {
        "message": "Device registered successfully",
        "device": device
    }


# Get all registered devices
@app.get("/devices")
def get_devices():
    return {
        "total_devices": len(devices),
        "devices": list(devices.values())
    }


# Get one particular device
@app.get("/devices/{device_id}")
def get_device(device_id: str):

    if device_id not in devices:
        raise HTTPException(
            status_code=404,
            detail="Device not found"
        )

    return devices[device_id]
