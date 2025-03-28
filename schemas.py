from pydantic import BaseModel
from datetime import datetime


# Схема для входящих данных
class TronRequestCreate(BaseModel):
    address: str

# Схема для ответа API
class TronRequestResponse(BaseModel):
    id: int
    address: str
    balance: str
    bandwidth: str
    energy: str
    created_at: datetime

# Настраиваем поведение Pydantic
class Config:
    from_attributes = True  # позволяет превращать ORM-модели в Pydantic-схемы


