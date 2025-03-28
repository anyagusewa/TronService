from sqlalchemy import Column, String, Integer, DateTime, func
from sqlalchemy.orm import declarative_base

# Общий класс для всех таблиц в БД
Base = declarative_base()

# Структура таблицы в БД
class TronRequest(Base):
    __tablename__ = "tron_requests"

    id = Column(Integer, primary_key=True, index=True)
    address = Column(String, nullable=False)
    balance = Column(String, nullable=False)
    bandwidth = Column(String, nullable=False)
    energy = Column(String, nullable=False)
    created_at = Column(DateTime, default=func.now())


