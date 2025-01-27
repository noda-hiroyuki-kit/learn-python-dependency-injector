# task.py
"""This module defines the Task dataclass.

このモジュールは, Taskデータクラスを定義.
"""

from dataclasses import dataclass


@dataclass
class Task:
    """Task is a dataclass that represents a task.

    Taskは, タスクを表すデータクラス.
    """

    id: int
    title: str
