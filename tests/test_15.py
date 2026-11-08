import unittest
from todo import create_list, add_task, exists_task


class TestExistsTask(unittest.TestCase):
    def test_exists(self):
        tasks = create_list()
        add_task(tasks, "Купить хлеб")
        self.assertTrue(exists_task(tasks, "Купить хлеб"))
        self.assertFalse(exists_task(tasks, "Купить молоко"))
