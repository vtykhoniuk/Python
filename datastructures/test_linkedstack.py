import unittest
from datastructures import LinkedStack


class TestStack(unittest.TestCase):

    def setUp(self):
        self.stack = LinkedStack()

    def test_pop_raises_exception(self):
        with self.assertRaises(IndexError):
            self.stack.pop()

    def test_push_pop(self):
        x = 1
        self.stack.push(x)
        self.assertEqual(x, self.stack.pop())

    def test_peek_raises_exception(self):
        with self.assertRaises(IndexError):
            self.stack.peek()

    def test_peek(self):
        for x in range(2):
            self.stack.push(x)
            self.assertEqual(x, self.stack.peek())

    def tearDown(self):
        self.stack = None
