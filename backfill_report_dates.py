
from pathlib import Path

from backend.app.models.base import Base
from backend.app.models.patient import Patient
from backend.app.models.document import Document
from backend.app.models.clinical_observation import ClinicalObservation
from backend.app.database import SessionLocal
from backend.app.services.pdf_extractor import extract_text_from_pdf
from backend.app.services.report_date_extractor import extract_report_date


db = SessionLocal()

try:
    documents = (
        db.query(Document)
        .filter(Document.report_date.is_(None))
        .all()
    )

    updated = 0

    for document in documents:
        file_path = Path(document.storage_path)

        try:
            if document.extracted_text:
                report_text = document.extracted_text
            elif file_path.exists():
                report_text = extract_text_from_pdf(file_path)
            else:
                print(f"File missing: {document.filename}")
                continue

            report_date = extract_report_date(report_text)

            if report_date:
                document.report_date = report_date
                updated += 1

                print(
                    f"Updated {document.filename}: {report_date}"
                )
            else:
                print(
                    f"No report date found: {document.filename}"
                )

        except Exception as exc:
            print(
                f"Could not process {document.filename}: {exc}"
            )

    db.commit()

    print(f"\nTotal documents updated: {updated}")

except Exception:
    db.rollback()
    raise

finally:
    db.close()
