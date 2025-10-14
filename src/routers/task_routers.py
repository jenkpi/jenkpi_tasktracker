from collections.abc import Mapping
from typing import Annotated, Any

from fastapi import APIRouter, Depends

from repository.repository import TaskRepository
from schemas.task_schemas import GetAllTasksResponse, PostTaskRequest, EditTaskRequest, TaskFull
from services.tasks_services import TaskService

router = APIRouter(prefix="/tasks")

task_service = TaskService(task_repo=TaskRepository())


def get_task_service() -> TaskService:
    return task_service


TaskServiceDep = Annotated[TaskService, Depends(get_task_service)]


@router.post("")
async def add_task(task_data: PostTaskRequest, task_service: TaskServiceDep) -> Mapping[str, Any]:
    return await task_service.add_one(task_data)


@router.get("")
async def get_all_tasks(task_service: TaskServiceDep) -> GetAllTasksResponse:
    return await task_service.get_all_tasks()


@router.post("/edit_task/{task_id}")
async def edit_task(task_id: int, changes: EditTaskRequest, task_service: TaskServiceDep) -> GetAllTasksResponse:
    return await task_service.edit_task(task_id, changes)
