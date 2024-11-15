from pydantic import BaseModel, Field
from uuid import UUID
from typing import Optional
from datetime import datetime

class User(BaseModel):
    id: UUID
    username: str
    password_hash: str
    created_at: datetime
    updated_at: Optional[datetime] = None
