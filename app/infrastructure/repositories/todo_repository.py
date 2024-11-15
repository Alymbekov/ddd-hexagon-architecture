from app.domain.interfaces.todo_repository import TodoRepository
from app.domain.models.todo import TodoItem
from typing import Optional
from uuid import UUID

class InMemoryTodoRepository(TodoRepository):
    def __init__(self):
        self.todos = {}

    def add(self, todo: TodoItem):
        """Добавляет новую задачу в хранилище."""
        self.todos[todo.id] = todo

    def get_by_id(self, todo_id: UUID) -> Optional[TodoItem]:
        """Возвращает задачу по её UUID."""
        return self.todos.get(todo_id)
