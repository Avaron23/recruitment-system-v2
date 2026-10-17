from decimal import Decimal

from sqlalchemy import Boolean, ForeignKey, Integer, Numeric
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base


class VacancySkill(Base):
    __tablename__ = "vacancy_skills"

    vacancy_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("vacancies.id", ondelete="CASCADE"), primary_key=True
    )
    skill_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("skills.id", ondelete="CASCADE"), primary_key=True
    )
    is_required: Mapped[bool] = mapped_column(Boolean, server_default=False)
    weight: Mapped[Decimal] = mapped_column(Numeric(5, 4))
