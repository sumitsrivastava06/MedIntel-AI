from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import DateTime, String
from sqlalchemy.orm import Mapped, mapped_column

from backend.app.models.base import Base


class Patient(Base):
    __tablename__ = "patients"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4,
    )

    external_id: Mapped[str | None] = mapped_column(
        String(100),
        unique=True,
        nullable=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )
