from fastapi import FastAPI
from app.api.v1.endpoints import todo

app = FastAPI(
    title="To-Do List API",
    description="Приложение для управления задачами с авторизацией.",
    version="1.0.0",
)

# Подключаем маршруты
app.include_router(todo.router, prefix="/api/v1/todos", tags=["ToDos"])
