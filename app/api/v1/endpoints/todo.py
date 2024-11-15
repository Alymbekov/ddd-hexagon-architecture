from fastapi import APIRouter, Depends
from app.domain.commands.todo_commands import CreateTodoCommand
from app.application.handlers.todo_handlers import CreateTodoHandler
from app.api.dependencies import get_todo_repository

router = APIRouter()

@router.post("/todos/")
def create_todo(
    command: CreateTodoCommand,
    repository = Depends(get_todo_repository)
):
    handler = CreateTodoHandler(repository=repository)
    return handler.handle(command)
