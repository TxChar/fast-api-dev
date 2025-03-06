from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
import uuid


class TaskBase(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), alias="_id")
    title: str
    description: Optional[str]
    completed: Optional[bool] = False
    created_at: Optional[datetime] = Field(default_factory=datetime, alias="createdAt")

    class Config:
        populate_by_name = True


class TaskCreate(TaskBase):
    title: str


class TaskUpdate(TaskBase):
    updated_at: Optional[datetime] = Field(default_factory=datetime, alias="updatedAt")
