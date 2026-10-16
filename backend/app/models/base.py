from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncAttrs


# Базовая модель от которой будут наследоваться все модели
class Base(AsyncAttrs, DeclarativeBase):
    __abstract__ = True