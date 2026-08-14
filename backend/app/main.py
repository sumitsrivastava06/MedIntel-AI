from fastapi import FastAPI
from sqlalchemy import text

from backend.app.database import engine

app = FastAPI(
    title="MedIntel AI API",
    description="AI-powered longitudinal medical intelligence platform",
    version="0.1.0",
)


@app.get("/")
def root():
    return {
        "message": "MedIntel AI API is running",
        "version": "0.1.0",
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
    }


@app.get("/health/db")
def database_health_check():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        return {
            "status": "healthy",
            "database": result.scalar(),
        }
