# task_repository.py
"""This module defines the TaskRepository abstract base class.

このモジュールは、TaskRepository 抽象基底クラスを定義。
"""

from abc import ABC, abstractmethod

from app.domain.task.task import Task


class TaskRepository(ABC):
    """TaskRepository is that defines the interface for task management operations.

    TaskRepositoryは, タスク管理操作のインターフェースを定義するクラス.

    Methods:
        get_tasks() -> list[Task]:
            Retrieve a list of all tasks.

            全てのタスクのリストを取得.
    """

    @abstractmethod
    def get_tasks(self) -> list[Task]:
        """Retrieve a list of all tasks.

        全てのタスクのリストを取得.

        Returns:
            list[Task]: A list of all tasks.

            全てのタスクのリスト.
        """
        raise NotImplementedError
