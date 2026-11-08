import unittest
from todo import create_list, add_task


class TestAddTask(unittest.TestCase):
    def test_add_task(self):
        tasks = create_list()
        add_task(tasks, "Купить хлеб")
        self.assertEqual(tasks, [
            {"title": "Купить хлеб", "done": False}
        ])
