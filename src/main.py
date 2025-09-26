from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI

from routers.task_routers import router as task_router


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(task_router)
