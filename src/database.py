from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from models.task_models import Base


engine = create_async_engine("postgresql+asyncpg://postgres:password@localhost:5432/tasks")

new_session = async_sessionmaker(engine)


# async def delete_tables():
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.drop_all)


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

