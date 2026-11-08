import unittest
from todo import create_list, add_task, finish_task, done_tasks


class TestDoneTasks(unittest.TestCase):
    def test_done(self):
        tasks = create_list()
        add_task(tasks, "Раз")
        add_task(tasks, "Два")
        finish_task(tasks, 0)
        self.assertEqual(
            [task["title"] for task in done_tasks(tasks)],
            ["Раз"]
        )
