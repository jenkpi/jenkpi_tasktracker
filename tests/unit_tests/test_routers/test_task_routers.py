from unittest.mock import call

import pytest
from test_data_parsers.test_data_parsers import get_bytes, get_json
from test_routers.conftest import get_mock_repo_and_client

from app.routers.task_routers import get_task_service
from app.schemas.task_schemas import EditTaskRequest, PostTaskRequest, PostTaskResponse
from app.services.tasks_services import TaskService


def test_get_task_service() -> None:
    assert isinstance(get_task_service(), TaskService)


def test_add_task() -> None:
    mock_repo, client = get_mock_repo_and_client()
    response = client.post("/tasks", json=get_json("test_routers/add_or_edit_task_in.json"))
    assert response.status_code == 200
    assert mock_repo.mock_calls == [
        call.add_task(PostTaskRequest(task="t", description=None, user_id=1, status="open", deadline=None))
    ]
    response_content_schema = PostTaskResponse.model_validate_json(response.content)
    assert response_content_schema.model_dump() == {"task_id": 111}


def test_get_tasks() -> None:
    mock_repo, client = get_mock_repo_and_client()
    response = client.get("/tasks")
    assert response.status_code == 200
    assert mock_repo.mock_calls == [call.get_all_tasks()]
    assert response.content == get_bytes("test_routers/get_all_tasks_out.json")


@pytest.mark.parametrize("task_id", [1])
def test_edit_task(task_id) -> None:
    mock_repo, client = get_mock_repo_and_client()
    response = client.post(f"/tasks/edit_task/{task_id}", json=get_json("test_routers/add_or_edit_task_in.json"))
    assert response.status_code == 200
    assert mock_repo.mock_calls == [
        call.edit_task(1, EditTaskRequest(task="t", description=None, user_id=1, status="open", deadline=None))
    ]
    assert response.content == get_bytes("test_routers/edit_task_out.json")
