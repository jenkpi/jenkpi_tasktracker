from pydantic import BaseModel


class TaskAdd(BaseModel):
    task: str
    description: str | None = None

class TaskAddToDb(TaskAdd):
    id: int
    model_config = {"from_attributes": True}