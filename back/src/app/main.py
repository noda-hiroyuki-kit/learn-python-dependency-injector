#!/usr/bin/env python
# main.py
"""Main module for FastAPI application.

FastAPI アプリケーションのメインモジュール.
"""

from typing import Annotated

from fastapi import Depends, FastAPI

from app.fake.fake_task_repository import FakeTaskRepository
from app.models.task import Task
from app.models.task_repository import TaskRepository

app = FastAPI()


@app.get("/")
def read_root() -> dict[str, str]:
    """Returns json with a greeting message.

    挨拶メッセージのjsonを返します。

    Returns: {"message": "Hello World"}
    """
    return {"message": "Hello World"}


@app.get("/tasks")
def get_tasks(
    task_repository: Annotated[TaskRepository, Depends(FakeTaskRepository)],
) -> list[Task]:
    """Returns a list of all tasks.

    全タスクのリストを返します。

    Returns: list[tasks]
    """
    return task_repository.get_tasks()
