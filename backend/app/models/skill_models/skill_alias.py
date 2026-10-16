from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base


class SkillAlias(Base):
    __tablename__ = 'skill_aliases'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    skill_id: Mapped[int] = mapped_column(Integer, ForeignKey("skills.id", ondelete="CASCADE"))
    alias: Mapped[str] = mapped_column(String(50), unique=True)