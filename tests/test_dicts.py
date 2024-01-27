import unittest
from utils import dicts

class TestDict(unittest.TestCase):

    def test_get(self):
        self.assertEqual(dicts.get_val({1: 1, 2: 2, 3: 3}, 1), 1)
        self.assertEqual(dicts.get_val({1: 1, 2: 2, 3: 3}, str(-1)), "a negative number")
        self.assertEqual(dicts.get_val({1: 1, 2: 2, 3: 3}, 10), "noname")
        self.assertEqual(dicts.get_val({1: 1, 2: 2, 3: 3}, str(-10)), "a negative number")
        self.assertEqual(dicts.get_val({1: 1, 2: 2, 3: 3}, 'qwe'), "uncorrect key")
        self.assertEqual(dicts.get_val({1: 1, 2: 2, 3: 3}, 'qwe'), "uncorrect key")

