import unittest
from todo import create_list, add_task, delete_task


class TestDeleteTask(unittest.TestCase):
    def test_delete(self):
        tasks = create_list()
        add_task(tasks, "Удалить")
        delete_task(tasks, 0)
        self.assertEqual(tasks, [])
