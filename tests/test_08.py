import unittest
from todo import create_list, add_task, rename_task


class TestRenameTask(unittest.TestCase):
    def test_rename(self):
        tasks = create_list()
        add_task(tasks, "Старое")
        rename_task(tasks, 0, "Новое")
        self.assertEqual(tasks[0]["title"], "Новое")
