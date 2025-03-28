from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

# Создаём движок для асинхронной работы с БД
engine = create_async_engine(DATABASE_URL, echo=True)

# Создаём фабрику сессий
AsyncSessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

# Автоматическое создание и закрытие сессий
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session

