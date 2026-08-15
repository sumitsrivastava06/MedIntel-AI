import shutil
from pathlib import Path
from uuid import UUID, uuid4

from fastapi import FastAPI, File, HTTPException, UploadFile
from sqlalchemy import text

from backend.app.database import SessionLocal, engine
from backend.app.models.document import Document
from backend.app.models.patient import Patient

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


UPLOAD_DIR = Path("data/uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


@app.post("/documents/upload")
def upload_document(
    patient_id: UUID,
    file: UploadFile = File(...),
):
    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are supported",
        )

    db = SessionLocal()
    file_path = None

    try:
        patient = db.get(Patient, patient_id)

        if patient is None:
            raise HTTPException(
                status_code=404,
                detail="Patient not found",
            )

        document_id = uuid4()
        safe_filename = f"{document_id}.pdf"
        file_path = UPLOAD_DIR / safe_filename

        with file_path.open("wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        document = Document(
            id=document_id,
            patient_id=patient_id,
            filename=file.filename or safe_filename,
            document_type="medical_report",
            storage_path=str(file_path),
            status="uploaded",
        )

        db.add(document)
        db.commit()
        db.refresh(document)

        return {
            "document_id": str(document.id),
            "patient_id": str(document.patient_id),
            "filename": document.filename,
            "storage_path": document.storage_path,
            "status": document.status,
        }

    except HTTPException:
        raise

    except Exception:
        db.rollback()

        if file_path is not None and file_path.exists():
            file_path.unlink()

        raise HTTPException(
            status_code=500,
            detail="Failed to upload document",
        )

    finally:
        db.close()
        

