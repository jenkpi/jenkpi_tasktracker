from collections.abc import Mapping
from typing import Any

from faststream.confluent.publisher.usecase import DefaultPublisher

from app.mappers.mappers import build_kafka_task_created_message
from app.repository.repository import TaskAbstractRepository
from app.schemas.task_schemas import EditTaskRequest, GetAllTasksResponse, PostTaskRequest, TaskFull


class TaskService:
    def __init__(self, task_repo: TaskAbstractRepository, publisher: DefaultPublisher):
        self.task_repo = task_repo
        self.publisher = publisher

    async def add_one(self, task: PostTaskRequest) -> Mapping[str, Any]:
        print(task)
        task_id = await self.task_repo.add_task(task)
        await self.publisher.publish(message=build_kafka_task_created_message(task_id, task))
        return {"task_id": task_id}

    async def get_all_tasks(self) -> GetAllTasksResponse:
        tasks = await self.task_repo.get_all_tasks()
        return tasks

    async def edit_task(self, task_id: int, changes: EditTaskRequest) -> TaskFull:
        if changes.deadline != None:
            self.publisher.publish(message=build_kafka_task_created_message(task_id, changes))
        return await self.task_repo.edit_task(task_id, changes)
