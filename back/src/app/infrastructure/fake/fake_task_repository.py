# fake_task_repository.py
"""This module defines the FakeTaskRepository class.

このモジュールは, FakeTaskRepositoryクラスを定義.
"""

from app.domain.task.task import Task
from app.domain.task.task_repository import TaskRepository


class FakeTaskRepository(TaskRepository):
    """FakeTaskRepository is a implementation class of TaskRepository.

    FakeTaskRepositoryはTaskRepositoryの実装クラス.

    Methods:
        get_tasks() -> list[Task]:
            Retrieve a list of all tasks.

            すべてのタスクのリストを取得します。
    """

    def __init__(self) -> None:
        """Initialize a new instance of FakeTaskRepository.

        FakeTaskRepositoryの新しいインスタンスを初期化します.
        """
        self.__tasks = [
            Task(1, "Task 1"),
            Task(2, "Task 2"),
            Task(3, "Task 3"),
        ]

    def get_tasks(self) -> list[Task]:
        """Retrieve a list of all tasks.

        すべてのタスクのリストを取得します。

        Returns:
            list[Task]: A list of all tasks.

            全てのタスクのリスト。
        """
        return self.__tasks
