from unittest.mock import AsyncMock, MagicMock

from fastapi import FastAPI
from fastapi.testclient import TestClient
from test_data_parsers.test_data_parsers import get_json

from app.main import get_app
from app.routers.task_routers import get_task_service
from app.schemas.task_schemas import GetAllTasksResponse, TaskFull
from app.services.tasks_services import TaskService


def get_mock_repo() -> MagicMock:
    repo = MagicMock()
    repo.add_task = AsyncMock(return_value=111)

    all_tasks = get_json("test_routers/get_all_tasks_in.json")
    all_tasks_schema = GetAllTasksResponse(tasks=[TaskFull.model_validate(all_tasks)])
    repo.get_all_tasks = AsyncMock(return_value=all_tasks_schema)

    all_tasks = get_json("test_routers/get_all_tasks_in.json")
    all_tasks_schema = TaskFull.model_validate(all_tasks)
    repo.edit_task = AsyncMock(return_value=all_tasks_schema)
    return repo


def get_mock_repo_and_dependency_override() -> tuple[MagicMock, FastAPI]:
    app = get_app()
    mock_repo = get_mock_repo()
    app.dependency_overrides[get_task_service] = lambda: TaskService(mock_repo)
    return mock_repo, app


def get_mock_repo_and_client() -> tuple[MagicMock, TestClient]:
    mock_repo, app = get_mock_repo_and_dependency_override()
    return mock_repo, TestClient(app)
