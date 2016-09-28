import unittest

from sentencereverse import sentencereverse


class SentenceReverseTest(unittest.TestCase):

    def test_sentencereverse_function_exists(self):
        sentencereverse("")

    def test_sentencereverse_raises_value_error(self):
        with self.assertRaises(ValueError):
            sentencereverse(123);

    def test_sentencereverse(self):
        self.assertEqual("456 123", sentencereverse("123 456"))
        self.assertEqual("test a is This", sentencereverse("This is a test"))
        self.assertEqual("World! Hello,", sentencereverse("Hello, World!"))
