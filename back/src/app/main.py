#!/usr/bin/env python
# main.py
"""Main module for FastAPI application.

FastAPI アプリケーションのメインモジュール.
"""

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root() -> dict[str, str]:
    """Returns json with a greeting message.

    挨拶メッセージのjsonを返します。

    Returns: {"message": "Hello World"}
    """
    return {"message": "Hello World"}
