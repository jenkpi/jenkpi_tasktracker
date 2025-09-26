from collections.abc import Mapping
from typing import Annotated, Any

from fastapi import APIRouter, Depends

from repository.repository import TaskRepository
from schemas.task_schemas import TaskAdd, TaskEdit, TaskOut
from services.tasks_services import TaskService

router = APIRouter(prefix="/tasks")

task_service = TaskService(task_repo=TaskRepository())


def get_task_service() -> TaskService:
    return task_service


TaskServiceDep = Annotated[TaskService, Depends(get_task_service)]


@router.post("")
async def add_task(task_data: TaskAdd, task_service: TaskServiceDep) -> Mapping[str, Any]:
    return await task_service.add_one(task_data)


@router.get("")
async def get_tasks(task_service: TaskServiceDep) -> list[TaskOut]:
    return await task_service.get_all()


@router.post("/edit_task/{task_id}")
async def edit_task(task_id: int, changes: TaskEdit, task_service: TaskServiceDep) -> list[TaskOut]:
    return await task_service.edit_task(task_id, changes)
