# test_main.py
"""tests for main module.

main モジュールのテスト.
"""

from fastapi import status
from fastapi.testclient import TestClient

from src.app.main import app


def test_read_root() -> None:
    """read_root() should return a greeting message.

    read_root() は挨拶メッセージを返すべき.
    """
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"message": "Hello World"}
