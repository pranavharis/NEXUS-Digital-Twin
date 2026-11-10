from fastapi import FastAPI
from datetime import datetime

app = FastAPI(
    title="NEXUS Digital Twin",
    description="Industrial IoT Monitoring Platform",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "project": "NEXUS",
        "message": "NEXUS Backend is Running!",
        "status": "ONLINE"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat()
    }