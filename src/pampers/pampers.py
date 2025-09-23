from models.task_models import TaskOrm
from schemas.task_schemas import TaskAdd, TaskEdit, TaskOut


def build_task_orm_model(data: TaskAdd | TaskEdit) -> TaskOrm:
    task_dict = data.model_dump()
    task = TaskOrm(**task_dict)
    return task


def build_task_schemas(task_models: list[TaskOrm]):
    task_schemas = [TaskOut.model_validate(task_model, from_attributes=True) for task_model in task_models]
    return task_schemas


def build_dict_from_schemas(task_schema: TaskEdit):
    return task_schema.model_dump(exclude_none=True)