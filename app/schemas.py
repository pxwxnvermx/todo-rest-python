from datetime import datetime

from pydantic import BaseModel, BaseConfig

BaseConfig.arbitrary_types_allowed = True


class TodoItemBase(BaseModel):
    description: str
    is_completed: bool = False


class TodoItemCreate(TodoItemBase):
    pass


class TodoItem(TodoItemBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
