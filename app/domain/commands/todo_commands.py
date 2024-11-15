from typing import Optional
from uuid import UUID

from pydantic import BaseModel

class CreateTodoCommand(BaseModel):
    user_id: UUID
    title: str
    description: Optional[str] = None
