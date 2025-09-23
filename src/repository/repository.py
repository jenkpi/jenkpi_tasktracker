from sqlalchemy import select, update
from pampers.pampers import build_dict_from_schemas, build_task_orm_model, build_task_schemas
from schemas.task_schemas import TaskAdd, TaskEdit, TaskOut
from database import new_session
from models.task_models import TaskOrm

class TaskRepository:
    @classmethod
    async def add_task(cls, data: TaskAdd) -> int:
        async with new_session() as session:
            task = build_task_orm_model(data) #валидация модели

            session.add(task) 
            await session.flush()
            task_id = task.task_id
            await session.commit()

            return task_id  

    @classmethod
    async def find_all(cls) -> list[TaskOut]:
        async with new_session() as session:
            query = select(TaskOrm)

            result = await session.execute(query)
            
            task_models = result.scalars().all()
            return build_task_schemas(task_models)
            
    @classmethod
    async def edit_task(cls, task_id: int, changes: TaskEdit):
        async with new_session() as session:
            task_dict = build_dict_from_schemas(changes)
            query = update(TaskOrm).where(TaskOrm.task_id == task_id).values(**task_dict).returning(TaskOrm)

            result = await session.execute(query)
            task_model = result.scalars().all()

            task_schema = build_task_schemas(task_model)
            await session.commit()
            return task_schema

