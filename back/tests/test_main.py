#!/usr/bin/env python3
# test_main.py
"""tests for main module.

main モジュールのテスト.
"""

from fastapi import status
from fastapi.testclient import TestClient

from app.main import app


def test_read_root() -> None:
    """read_root() should return a greeting message.

    read_root() は挨拶メッセージを返すべき.
    """
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"message": "Hello World"}


def test_get_tasks() -> None:
    """get_tasks() should return a list of tasks.

    get_tasks() はタスクのリストを返すべき.
    """
    client = TestClient(app)
    response = client.get("/tasks")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == [
        {"id": 1, "title": "Task 1"},
        {"id": 2, "title": "Task 2"},
        {"id": 3, "title": "Task 3"},
    ]
