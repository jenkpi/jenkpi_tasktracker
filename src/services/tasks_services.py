from collections.abc import Mapping
from typing import Any

from repository.repository import TaskAbstractRepository
from schemas.task_schemas import TaskAdd, TaskEdit, TaskOut


class TaskService:
    def __init__(self, task_repo: TaskAbstractRepository):
        self.task_repo = task_repo

    async def add_one(self, task: TaskAdd) -> Mapping[str, Any]:
        task_id = await self.task_repo.add_task(task)
        return {"ok": True, "task_id": task_id}

    async def get_all(self) -> list[TaskOut]:
        tasks = await self.task_repo.find_all()
        return tasks

    async def edit_task(self, task_id: int, changes: TaskEdit) -> list[TaskOut]:
        return await self.task_repo.edit_task(task_id, changes)
