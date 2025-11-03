from collections.abc import Iterable, Mapping
from typing import Any

from app.schemas.task_schemas import EditTaskRequest, GetAllTasksResponse, KafkaTaskCreatedMessage, PostTaskRequest, TaskFull
from app.sqlalchemy_orm_models.sqlalchemy_orm_task_models import TaskOrm


def build_task_orm_model(task_data: PostTaskRequest | EditTaskRequest) -> TaskOrm:
    task_dict = task_data.model_dump()
    task = TaskOrm(**task_dict)
    print(task.__dict__)
    return task


def build_task_schemas_from_orm(task_models: Iterable[TaskOrm]) -> GetAllTasksResponse:
    task_schemas = [TaskFull.model_validate(task_model, from_attributes=True) for task_model in task_models]
    return GetAllTasksResponse(tasks=task_schemas)


def build_dict_from_schemas(task_schema: EditTaskRequest) -> Mapping[str, Any]:
    return task_schema.model_dump(exclude_none=True)


def build_kafka_task_created_message(task_id: int, task_data: PostTaskRequest | EditTaskRequest) -> KafkaTaskCreatedMessage:
    kafka_task_created_message = KafkaTaskCreatedMessage(task_id=task_id, 
                                                         task=task_data.task, 
                                                         description=task_data.description, 
                                                         user_id=task_data.user_id, 
                                                         status=task_data.status, 
                                                         deadline=task_data.deadline)
    return kafka_task_created_message