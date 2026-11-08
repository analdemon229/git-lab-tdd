import unittest
from todo import create_list, add_task, finish_task, pending_tasks


class TestPendingTasks(unittest.TestCase):
    def test_pending(self):
        tasks = create_list()
        add_task(tasks, "Раз")
        add_task(tasks, "Два")
        finish_task(tasks, 0)
        self.assertEqual(
            [task["title"] for task in pending_tasks(tasks)],
            ["Два"]
        )
