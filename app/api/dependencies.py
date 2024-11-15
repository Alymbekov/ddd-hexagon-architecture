from app.infrastructure.repositories.todo_repository import InMemoryTodoRepository

def get_todo_repository():
    return InMemoryTodoRepository()
