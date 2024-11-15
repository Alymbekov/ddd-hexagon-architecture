from pydantic import BaseModel
from uuid import UUID
from typing import Optional
from datetime import datetime

class TodoItem(BaseModel):
    id: UUID
    title: str
    description: Optional[str] = None
    completed: bool = False
    created_at: datetime
    updated_at: Optional[datetime] = None
