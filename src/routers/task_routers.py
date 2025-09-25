from typing import Annotated

from fastapi import APIRouter, Depends

from repository.repository import TaskRepository
from schemas.task_schemas import TaskAdd, TaskEdit, TaskOut
from services.tasks_services import TaskService

router = APIRouter(prefix="/tasks")

task_service = TaskService(task_repo=TaskRepository())


def get_task_service():
    return task_service


TaskServiceDep = Annotated[TaskService, Depends(get_task_service)]


@router.post("")
async def add_task(data: TaskAdd, task_service: TaskServiceDep) -> dict:
    return await task_service.add_one(data)


@router.get("")
async def get_tasks(task_service: TaskServiceDep) -> list[TaskOut]:
    return await task_service.get_all()


@router.post("/edit_task/{task_id}")
async def edit_task(task_id: int, changes: TaskEdit, task_service: TaskServiceDep):
    return await task_service.edit_task(task_id, changes)
