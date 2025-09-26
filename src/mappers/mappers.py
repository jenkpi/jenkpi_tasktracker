from collections.abc import Iterable, Mapping
from typing import Any

from schemas.task_schemas import TaskAdd, TaskEdit, TaskOut
from sqlalchemy_orm_models.sqlalchemy_orm_task_models import TaskOrm


def build_task_orm_model(task_data: TaskAdd | TaskEdit) -> TaskOrm:
    task_dict = task_data.model_dump()
    task = TaskOrm(**task_dict)
    return task


def build_task_schemas(task_models: Iterable[TaskOrm]) -> list[TaskOut]:
    task_schemas = [TaskOut.model_validate(task_model, from_attributes=True) for task_model in task_models]
    return task_schemas


def build_dict_from_schemas(task_schema: TaskEdit) -> Mapping[str, Any]:
    return task_schema.model_dump(exclude_none=True)
