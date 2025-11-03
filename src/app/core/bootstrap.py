from fastapi import FastAPI

from app.core.lifespan import lifespan
from app.routers.task_routers import router as task_router


def get_app() -> FastAPI:
    app = FastAPI(lifespan=lifespan)
    app.include_router(task_router)
    return app
