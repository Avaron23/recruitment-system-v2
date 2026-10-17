from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase


# Базовая модель от которой будут наследоваться все модели
class Base(AsyncAttrs, DeclarativeBase):
    __abstract__ = True
