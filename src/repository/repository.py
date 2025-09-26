from typing import Protocol

from sqlalchemy import select, update

from database import new_session
from mappers.mappers import (
    build_dict_from_schemas,
    build_task_orm_model,
    build_task_schemas,
)
from schemas.task_schemas import TaskAdd, TaskEdit, TaskOut
from sqlalchemy_orm_models.sqlalchemy_orm_task_models import TaskOrm


class TaskAbstractRepository(Protocol):
    @classmethod
    async def add_task(cls, task_data: TaskAdd) -> int: ...

    @classmethod
    async def find_all(cls) -> list[TaskOut]: ...

    @classmethod
    async def edit_task(cls, task_id: int, changes: TaskEdit) -> list[TaskOut]: ...


class TaskRepository:
    @classmethod
    async def add_task(cls, task_data: TaskAdd) -> int:
        async with new_session() as session:
            task = build_task_orm_model(task_data)  # валидация модели

            session.add(task)
            await session.flush()
            task_id = task.task_id
            await session.commit()

            return task_id

    @classmethod
    async def find_all(cls) -> list[TaskOut]:
        async with new_session() as session:
            query = select(TaskOrm)

            res = await session.execute(query)

            task_models = res.scalars().all()
            return build_task_schemas(task_models)

    @classmethod
    async def edit_task(cls, task_id: int, changes: TaskEdit) -> list[TaskOut]:
        async with new_session() as session:
            task_dict = build_dict_from_schemas(changes)
            query = update(TaskOrm).where(TaskOrm.task_id == task_id).values(**task_dict).returning(TaskOrm)  # noqa:WPS221

            task_model = (await session.execute(query)).scalars().all()

            task_schema = build_task_schemas(task_model)
            await session.commit()
            return task_schema
