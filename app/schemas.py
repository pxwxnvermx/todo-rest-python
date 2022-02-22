from datetime import datetime
from typing import Optional

from pydantic import BaseModel, BaseConfig

BaseConfig.arbitrary_types_allowed = True


class TodoItemBase(BaseModel):
    description: str
    is_completed: bool = False


class TodoItemCreate(TodoItemBase):
    pass


class TodoItemUpdate(BaseModel):
    description: Optional[str]
    is_completed: Optional[bool]


class TodoItem(TodoItemBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int

    class Config:
        orm_mode = True
