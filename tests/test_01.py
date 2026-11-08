import unittest
from todo import create_list


class TestCreateList(unittest.TestCase):
    def test_create_list(self):
        self.assertEqual(create_list(), [])
