import unittest
from datastructures import LinkedList


class TestConstructor(unittest.TestCase):

    def test_default(self):
        n = LinkedList.Node()
        self.assertIsNone(n.value)
        self.assertIsNone(n.next_node)

    def test_with_parameters(self):
        n = LinkedList.Node("123")
        self.assertIsNone(n.next_node)
        self.assertEqual("123", n.value)

        m = LinkedList.Node("456", n)
        self.assertEqual("456", m.value)
        self.assertEqual(n, m.next_node)


class TestInterface(unittest.TestCase):

    def test_next_node_setter(self):
        n = LinkedList.Node("123")
        n.next_node = LinkedList.Node("456")
