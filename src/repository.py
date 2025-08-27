from sqlalchemy import select
from schemas import TaskAdd, TaskAddToDb
from database import new_session, TaskOrm

class TaskRepository:
    @classmethod
    async def add_task(cls, data: TaskAdd) -> int:
        async with new_session() as session:
            task_dict = data.model_dump()

            task = TaskOrm(**task_dict)
            session.add(task)
            await session.flush()
            task_id = task.id
            await session.commit()
            return task_id
        
        

    @classmethod
    async def find_all(cls) -> list[TaskAddToDb]:
        async with new_session() as session:
            query = select(TaskOrm)
            result = await session.execute(query)
            task_models = result.scalars().all()
            task_schemas = [TaskAddToDb.model_validate(task_model, from_attributes=True) for task_model in task_models]
            return task_schemas
            