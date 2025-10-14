import json
from unittest.mock import call
from schemas.task_schemas import GetAllTasksResponse, PostTaskRequest, PostTaskResponse, TaskFull
from test_routers.conftest import get_mock_repo_and_client
from test_data_parsers.test_data_parsers import get_bytes


def test_add_task():
    mock_repo, client = get_mock_repo_and_client()
    response = client.post("/tasks", json={"task": "t", "user_id": 1, "status": "open"})
    assert response.status_code == 200
    assert mock_repo.mock_calls == [call.add_task(PostTaskRequest(task='t', description=None, user_id=1, status='open', deadline=None))]
    response_content_schema = PostTaskResponse.model_validate_json(response.content)
    assert response_content_schema.model_dump() == {"task_id": 111}


def test_get_tasks():
    mock_repo, client = get_mock_repo_and_client()
    response = client.get("/tasks")
    assert response.status_code == 200
    assert response.content == get_bytes("test_routers/all_tasks_out.json")


def test_edit_task():
    