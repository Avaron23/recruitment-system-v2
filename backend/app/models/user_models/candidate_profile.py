from sqlalchemy import Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base


class CandidateProfile(Base):
    __tablename__ = 'candidate_profiles'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id", ondelete="CASCADE"), unique=True)
    experience_years: Mapped[int] = mapped_column(Integer())
    education: Mapped[str] = mapped_column(String(50))
    salary_expectation: Mapped[int] = mapped_column(Integer)
    relocation: Mapped[bool] = mapped_column(Boolean)