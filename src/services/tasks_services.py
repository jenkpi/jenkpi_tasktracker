from typing import Annotated

from fastapi import Depends
from repository.repository import TaskRepository
from schemas.task_schemas import TaskAdd, TaskEdit

class TaskService():
    async def add_one(self, task: Annotated[TaskAdd, Depends()]):
        task_id = await TaskRepository.add_task(task)
        return {"ok": True, "task_id": task_id}
    

    async def get_all(self):
        tasks = await TaskRepository.find_all()
        return tasks
    
    
    async def edit_task(self, task_id: int, changes: TaskEdit):
        return await TaskRepository.edit_task(task_id, changes)