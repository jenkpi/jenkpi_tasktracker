import datetime
from pydantic import BaseModel


class PostTaskRequest(BaseModel):
    task: str
    description: str | None = None
    user_id: int
    status: str
    deadline: datetime.datetime | None = None


class PostTaskResponse(BaseModel):
    task_id: int


class TaskFull(PostTaskRequest):
    task_id: int


class GetAllTasksResponse(BaseModel):
    tasks: list[TaskFull]


class EditTaskRequest(BaseModel):
    task: str | None = None
    description: str | None = None
    user_id: int | None = None
    status: str | None = None
    deadline: datetime.datetime | None = None


class KafkaTaskCreatedMessage(PostTaskRequest):
    task_id: int