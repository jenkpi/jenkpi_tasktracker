from datetime import datetime

from pydantic import BaseModel


class TaskAdd(BaseModel):
    task: str
    description: str | None = None
    user_id: int
    status: str
    deadline: datetime | None = None


class TaskOut(TaskAdd):
    task_id: int
    # model_config = {"from_attributes": True}


class TaskEdit(BaseModel):
    task: str | None = None
    description: str | None = None
    user_id: int | None = None
    status: str | None = None
    deadline: datetime | None = None
