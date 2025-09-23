from typing import Annotated
from fastapi import APIRouter, Depends

from models.task_models import TaskOrm
from pampers.pampers import build_dict_from_schemas, build_task_schemas
from schemas.task_schemas import TaskAdd, TaskEdit, TaskOut
from repository.repository import TaskRepository
from services.tasks_services import TaskService

router = APIRouter(prefix="/tasks")

@router.post("")
async def add_task(data: Annotated[TaskAdd, Depends()]) -> dict:
    task = TaskService()
    return await task.add_one(data) 


@router.get("", response_model=list[TaskOut])
async def get_tasks() -> list[TaskOut]:
    tasks = TaskService()
    return await tasks.get_all()

@router.post("/edit_task/{task_id}")
async def edit_task(task_id: int, changes: TaskEdit):
    task = TaskService()
    return await task.edit_task(task_id, changes)