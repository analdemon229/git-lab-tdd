import unittest
from todo import create_list, add_task, finish_task, clear_done


class TestClearDone(unittest.TestCase):
    def test_clear(self):
        tasks = create_list()
        add_task(tasks, "Раз")
        add_task(tasks, "Два")
        finish_task(tasks, 0)
        clear_done(tasks)
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]["title"], "Два")
