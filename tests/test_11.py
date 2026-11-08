import unittest
from todo import create_list, add_task, finish_task, count_pending


class TestCountPending(unittest.TestCase):
    def test_count_pending(self):
        tasks = create_list()
        add_task(tasks, "Раз")
        add_task(tasks, "Два")
        finish_task(tasks, 0)
        self.assertEqual(count_pending(tasks), 1)
