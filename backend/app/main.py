from fastapi import FastAPI

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