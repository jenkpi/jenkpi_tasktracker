from datetime import datetime

import pytest
from sqlalchemy.inspection import inspect

from mappers.mappers import build_dict_from_schemas, build_task_orm_model, build_task_schemas_from_orm
from schemas.task_schemas import GetAllTasksResponse, PostTaskRequest, EditTaskRequest, TaskFull
from sqlalchemy_orm_models.sqlalchemy_orm_task_models import TaskOrm


def orm_to_dict(obj):
    mapper = inspect(obj).mapper
    return {col.key: getattr(obj, col.key) for col in mapper.columns}


@pytest.mark.parametrize(
    ("model", "task_data"),
    [
        (
            PostTaskRequest,
            {"task": "task_1", "description": "descr", "user_id": 1, "status": "open", "deadline": datetime.now()},
        ),
        (
            EditTaskRequest,
            {"task": "task_1", "description": "descr", "user_id": 1, "status": "open", "deadline": datetime.now()},
        ),
    ],
)
def test_build_task_orm_model(model, task_data):
    built = build_task_orm_model(model.model_validate(task_data))
    expected = TaskOrm(**task_data)
    assert orm_to_dict(built) == orm_to_dict(expected)


def test_build_task_schemas_from_orm():
    task_dict = {
        "task": "task_1",
        "description": "descr",
        "user_id": 1,
        "status": "open",
        "deadline": datetime.now(),
        "task_id": 1,
    }
    task_orm_model = [TaskOrm(**task_dict)]
    built = build_task_schemas_from_orm(task_orm_model)
    expected = GetAllTasksResponse(tasks=[TaskFull.model_validate(task_dict)])
    assert built == expected


def test_build_dict_from_schemas():
    task_dict = {"task": "task_1", "description": "descr", "user_id": 1, "status": "open", "deadline": datetime.now()}
    task_edit_schema = EditTaskRequest.model_validate(task_dict)
    built = build_dict_from_schemas(task_edit_schema)
    assert built == task_dict
