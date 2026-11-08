import unittest
from todo import create_list, add_task, get_tasks


class TestGetTasks(unittest.TestCase):
    def test_get_tasks(self):
        tasks = create_list()
        add_task(tasks, "Учёба")
        self.assertEqual(get_tasks(tasks), tasks)
