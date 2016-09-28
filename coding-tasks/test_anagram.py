import unittest
from anagram import isanagram


class TestAnagram(unittest.TestCase):

    def test_isanagram_trows_value_error_exception(self):
        with self.assertRaises(ValueError):
            isanagram(1, 2)

        with self.assertRaises(ValueError):
            isanagram("asd", 2)

        with self.assertRaises(ValueError):
            isanagram(1, "123")

    def test_isanagram(self):
        self.assertTrue(isanagram("a", "a"))
        self.assertFalse(isanagram("aa", "a"))
        self.assertTrue(isanagram("ab", "ba"))
        self.assertTrue(isanagram("public relations", "crap built on lies"))
        self.assertTrue(isanagram("clint eastwood", "old west action"))
