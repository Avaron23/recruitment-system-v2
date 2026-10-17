from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, String, func
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base


class Vacancy(Base):
    __tablename__ = "vacancies"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    recruiter_profile_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("recruiter_profiles.id", ondelete="CASCADE")
    )
    title: Mapped[str] = mapped_column(String(50), nullable=False)
    company_name: Mapped[str] = mapped_column(String(50))
    description: Mapped[str] = mapped_column(String(300))
    salay_min: Mapped[int] = mapped_column(Integer)
    salay_max: Mapped[int] = mapped_column(Integer)
    status: Mapped[str] = mapped_column(String, nullable=False, server_default="wait")
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now
    )
