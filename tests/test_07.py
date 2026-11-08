import unittest
from todo import create_list, add_task, get_task


class TestGetTask(unittest.TestCase):
    def test_get(self):
        tasks = create_list()
        add_task(tasks, "Тест")
        self.assertEqual(get_task(tasks, 0)["title"], "Тест")
