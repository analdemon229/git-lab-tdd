import unittest
from todo import create_list, add_task, finish_task


class TestFinishTask(unittest.TestCase):
    def test_finish(self):
        tasks = create_list()
        add_task(tasks, "Домашняя работа")
        finish_task(tasks, 0)
        self.assertTrue(tasks[0]["done"])
