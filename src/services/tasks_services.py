from collections.abc import Mapping
from typing import Any

from repository.repository import TaskAbstractRepository
from schemas.task_schemas import GetAllTasksResponse, PostTaskRequest, EditTaskRequest, TaskFull


class TaskService:
    def __init__(self, task_repo: TaskAbstractRepository):
        self.task_repo = task_repo

    async def add_one(self, task: PostTaskRequest) -> Mapping[str, Any]:
        task_id = await self.task_repo.add_task(task)
        return {"task_id": task_id}

    async def get_all_tasks(self) -> GetAllTasksResponse:
        tasks = await self.task_repo.get_all_tasks()
        return tasks

    async def edit_task(self, task_id: int, changes: EditTaskRequest) -> GetAllTasksResponse:
        return await self.task_repo.edit_task(task_id, changes)
