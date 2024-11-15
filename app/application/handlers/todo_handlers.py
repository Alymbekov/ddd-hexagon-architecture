from uuid import UUID
from app.domain.commands.todo_commands import CreateTodoCommand
from app.domain.interfaces.todo_repository import TodoRepository
from app.domain.models.todo import TodoItem
from datetime import datetime

class CreateTodoHandler:
    def __init__(self, repository: TodoRepository):
        self.repository = repository

    def handle(self, command: CreateTodoCommand) -> TodoItem:
        todo_item = TodoItem(
            id=UUID(),
            title=command.title,
            description=command.description,
            completed=False,
            created_at=datetime.utcnow()
        )
        self.repository.add(todo_item)
        return todo_item
