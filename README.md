✨ Tron Service API ✨

TronService — это микросервис, который предоставляет информацию о кошельках в сети Tron, включая данные о балансе, bandwidth и energy. Этот сервис позволяет пользователю отправлять запросы через два эндпоинта и сохранять информацию в базу данных для дальнейшего использования.

Возможности:
- POST-запрос: Получение данных о кошельке по адресу в сети Tron (balance, bandwidth, energy).
- GET-запрос: Получение списка последних запросов с пагинацией.
- Каждый запрос записывается в базу данных с полями о кошельке.
	
Технологии:
- Backend: Python, FastAPI, Asyncio, Pydantic
- База данных: PostgreSQL, SQLAlchemy ORM
- Взаимодействие с Tron: TronPy
- Тестирование: Pytest(интеграционные тесты для проверки работы эндпоинтов и юнит-тесты для проверки записи в базу данных с использованием мок-объектов)
- Документация API: Swagger 
 
![post](https://github.com/user-attachments/assets/83b51cd7-1cc8-4bbd-8e84-51d29a80dbec)

![swagger](https://github.com/user-attachments/assets/0a47d57f-3a66-44c1-aba8-af30197f7641)

![get](https://github.com/user-attachments/assets/3891fb6e-1a86-4228-b6f6-a881544b5007)

![pytest](https://github.com/user-attachments/assets/90f21511-f3b0-4f37-9b15-5f2007caed00)


