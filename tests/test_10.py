import unittest
from todo import create_list, add_task, finish_task, count_done


class TestCountDone(unittest.TestCase):
    def test_count_done(self):
        tasks = create_list()
        add_task(tasks, "Раз")
        add_task(tasks, "Два")
        finish_task(tasks, 0)
        self.assertEqual(count_done(tasks), 1)
