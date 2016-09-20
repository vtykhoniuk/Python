import unittest
from stringcompression import stringcompression


class StringCompressionTets(unittest.TestCase):

    def test_stringcompression_exists(self):
        stringcompression("a")

    def test_stringcompression_raises_value_error(self):
        with self.assertRaises(ValueError):
            stringcompression(123)

    def test_stringcompression_with_empty_string(self):
        with self.assertRaises(ValueError):
            stringcompression("")

    def test_stringcompression_onechar_string(self):
        self.assertEqual("a1", stringcompression("a"))
        self.assertEqual("b1", stringcompression("b"))

    def test_stringcompression_monochars_string(self):
        self.assertEqual("a2", stringcompression("aa"))
        self.assertEqual("a3", stringcompression("aaa"))

    def test_stringcompression(self):
        self.assertEqual("a2b2", stringcompression("aabb"))
        self.assertEqual("a2b2c1d3f1", stringcompression("aabbcdddf"))
        self.assertEqual("a4b4c2f1", stringcompression("aaaabbbbccf"))
        self.assertEqual("a1b1c1d1", stringcompression("abcd"))
