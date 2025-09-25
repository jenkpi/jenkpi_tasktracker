from contextlib import asynccontextmanager

from fastapi import FastAPI

from routers.task_routers import router as task_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(task_router)
