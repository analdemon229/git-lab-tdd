import unittest
from todo import create_list, add_task, count_tasks


class TestCountTasks(unittest.TestCase):
    def test_count(self):
        tasks = create_list()
        add_task(tasks, "Раз")
        add_task(tasks, "Два")
        self.assertEqual(count_tasks(tasks), 2)
