from abc import ABC, abstractmethod
from typing import Optional
from uuid import UUID
from app.domain.models.todo import TodoItem

class TodoRepository(ABC):
    @abstractmethod
    def add(self, todo: TodoItem):
        """Добавляет новую задачу в хранилище."""
        pass

    @abstractmethod
    def get_by_id(self, todo_id: UUID) -> Optional[TodoItem]:
        """Возвращает задачу по её UUID."""
        pass
