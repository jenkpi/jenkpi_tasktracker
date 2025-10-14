from typing import Protocol

from sqlalchemy import select, update

from database import new_session
from mappers.mappers import (
    build_dict_from_schemas,
    build_task_orm_model,
    build_task_schemas_from_orm,
)
from schemas.task_schemas import GetAllTasksResponse, PostTaskRequest, EditTaskRequest, TaskFull
from sqlalchemy_orm_models.sqlalchemy_orm_task_models import TaskOrm


class TaskAbstractRepository(Protocol):
    async def add_task(self, task_data: PostTaskRequest) -> int: ...

    async def get_all_tasks(self) -> GetAllTasksResponse: ...

    async def edit_task(self, task_id: int, changes: EditTaskRequest) -> GetAllTasksResponse: ...


class TaskRepository:
    async def add_task(self, task_data: PostTaskRequest) -> int:
        async with new_session() as session:
            task = build_task_orm_model(task_data)  # валидация модели

            session.add(task)
            await session.flush()
            task_id = task.task_id
            await session.commit()

            return task_id

    async def get_all_tasks(self) -> GetAllTasksResponse:
        async with new_session() as session:
            query = select(TaskOrm)

            res = await session.execute(query)

            task_models = res.scalars().all()
            return build_task_schemas_from_orm(task_models)


    async def edit_task(self, task_id: int, changes: EditTaskRequest) -> GetAllTasksResponse:
        async with new_session() as session:
            task_dict = build_dict_from_schemas(changes)
            query = update(TaskOrm).where(TaskOrm.task_id == task_id).values(**task_dict).returning(TaskOrm)  # noqa:WPS221

            task_model = (await session.execute(query)).scalars().all()

            task_schema = build_task_schemas_from_orm(task_model)
            await session.commit()
            return task_schema
