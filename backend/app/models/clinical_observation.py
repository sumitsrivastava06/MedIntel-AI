from uuid import UUID, uuid4

from sqlalchemy import ForeignKey, String, Text, Float
from sqlalchemy.orm import Mapped, mapped_column

from backend.app.models.base import Base


class ClinicalObservation(Base):
    __tablename__ = "clinical_observations"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4,
    )

    document_id: Mapped[UUID] = mapped_column(
        ForeignKey("documents.id"),
        nullable=False,
    )

    patient_id: Mapped[UUID] = mapped_column(
        ForeignKey("patients.id"),
        nullable=False,
    )

    test_name: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
    )

    value: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    value_text: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    unit: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True,
    )

    reference_range: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    status: Mapped[str | None] = mapped_column(
        String(30),
        nullable=True,
    )