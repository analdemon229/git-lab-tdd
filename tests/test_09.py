import unittest
from todo import create_list, add_task, finish_task, reopen_task


class TestReopenTask(unittest.TestCase):
    def test_reopen(self):
        tasks = create_list()
        add_task(tasks, "Задача")
        finish_task(tasks, 0)
        reopen_task(tasks, 0)
        self.assertFalse(tasks[0]["done"])
