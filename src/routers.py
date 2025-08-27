from typing import Annotated
from fastapi import APIRouter, Depends

from schemas import TaskAdd, TaskAddToDb
from repository import TaskRepository

router = APIRouter(prefix="/tasks")

@router.post("")
async def add_task(task: Annotated[TaskAdd, Depends()]):
    task_id = await TaskRepository.add_task(task)
    return {"ok": True, "task_id": task_id}


@router.get("", response_model=list[TaskAddToDb])
async def get_tasks() -> list[TaskAddToDb]:
    tasks = await TaskRepository.find_all()
    return tasks