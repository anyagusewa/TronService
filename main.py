from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
import models
import schemas
from database import engine, get_db
from contextlib import asynccontextmanager
from tronpy import Tron
from sqlalchemy.future import select
from typing import List



# Соединение с БД и создание в ней таблиц
async def init_db() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)


# Жизненный цикл приложения
@asynccontextmanager
async def lifespan(app: FastAPI):  # Создаём функцию для старта и завершения приложения
    await init_db()
    yield


# Создаём объект приложения
app = FastAPI(lifespan=lifespan)

# Подключаемся к Tron-сети
tron = Tron()


# Эндпоинт для запроса данных о кошельке Tron
@app.post("/wallet", response_model=schemas.TronRequestResponse)
async def get_wallet_data(
        request: schemas.TronRequestCreate, db: AsyncSession = Depends(get_db)
) -> schemas.TronRequestResponse:

    # Получаем информацию о кошельке через Tron API
    try:
        account_info = tron.get_account(request.address)
        balance = str(account_info.get("balance", 0))
        bandwidth = str(account_info.get("bandwidth", 0))
        energy = str(account_info.get("energy", 0))
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid Tron address")


    # Создаём запись в базе данных
    new_request = models.TronRequest(
        address=request.address,
        balance=balance,
        bandwidth=bandwidth,
        energy=energy,
    )
    db.add(new_request) # добавляет объект в текущую сессию
    await db.commit() # фиксация изменений в базе
    await db.refresh(new_request) # обновляем объект из базы

    return new_request

# Эндпоинт для получения списка запросов
@app.get("/wallets", response_model=list[schemas.TronRequestResponse])
async def get_wallets(
        db: AsyncSession = Depends(get_db),
        # пагинация
        limit: int = 10,
        offset: int = 0
) -> List[schemas.TronRequestResponse]:

    # Формирование SQL-запроса
    result = await db.execute(
        select(models.TronRequest) # выбор всех записей из таблицы
        .order_by(models.TronRequest.created_at.desc()) # сортируем от новых к старым
        .limit(limit)
        .offset(offset)
    )

    wallets = result.scalars().all()

    return list(wallets)