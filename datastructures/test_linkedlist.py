import unittest
from datastructures import LinkedList


class TestLinkedListNode(unittest.TestCase):

    def test_default_constructor(self):
        n = LinkedList.Node()
        self.assertIsNone(n.value)
        self.assertIsNone(n.next_node)

    def test_constructor(self):
        n = LinkedList.Node("123")
        self.assertIsNone(n.next_node)
        self.assertEqual("123", n.value)

        m = LinkedList.Node("456", n)
        self.assertEqual("456", m.value)
        self.assertEqual(n, m.next_node)

    def test_next_node_setter(self):
        n = LinkedList.Node("123")
        n.next_node = LinkedList.Node("456")


class TestLinkedList(unittest.TestCase):

    def setUp(self):
        self.linkedlist = LinkedList()

    def test_default_constructor(self):
        self.assertIsNone(self.linkedlist._head)
        self.assertIsNone(self.linkedlist._tail)
        self.assertEqual(0, self.linkedlist.size)

    def test_push_front_empty_list(self):
        self.linkedlist.push_front(1)
        self.assertIsNotNone(self.linkedlist._head)
        self.assertIsNotNone(self.linkedlist._tail)
        self.assertEqual(self.linkedlist._head, self.linkedlist._tail)
        self.assertEqual(1, self.linkedlist.size)

    def test_push_front_non_empty_list(self):
        self.linkedlist.push_front(1)
        self.linkedlist.push_front(2)
        self.assertEqual(2, self.linkedlist._head.value)
        self.assertEqual(1, self.linkedlist._tail.value)
        self.assertEqual(2, self.linkedlist.size)

    def test_push_back_empty_list(self):
        self.linkedlist.push_back(1)
        self.assertIsNotNone(self.linkedlist._head)
        self.assertIsNotNone(self.linkedlist._tail)
        self.assertEqual(self.linkedlist._head, self.linkedlist._tail)
        self.assertEqual(1, self.linkedlist.size)

    def test_push_back_non_empty_list(self):
        self.linkedlist.push_back(1)
        self.linkedlist.push_back(2)
        self.assertEqual(1, self.linkedlist._head.value)
        self.assertEqual(2, self.linkedlist._tail.value)
        self.assertEqual(2, self.linkedlist.size)

    def test_pop_front_on_empty_list_raises_exception(self):
        with self.assertRaises(IndexError):
            self.linkedlist.pop_front()

    def test_pop_front_from_one_element_list(self):
        self.linkedlist.push_back(1)
        self.assertEqual(1, self.linkedlist.pop_front())
        self.assertIsNone(self.linkedlist._head)
        self.assertIsNone(self.linkedlist._tail)
        self.assertEqual(0, self.linkedlist.size)

    def test_pop_front_from_two_elements_list(self):
        self.linkedlist.push_back(1)
        self.linkedlist.push_back(2)
        self.linkedlist.pop_front()
        self.assertIsNotNone(self.linkedlist._head)
        self.assertIsNotNone(self.linkedlist._tail)
        self.assertEqual(self.linkedlist._head, self.linkedlist._tail)

    def test_pop_front_from_multielements_list(self):
        for x in range(10):
            self.linkedlist.push_back(x)

        self.linkedlist.pop_front()
        self.assertEqual(1, self.linkedlist._head.value)
        self.assertEqual(9, self.linkedlist._tail.value)

    def test_builtin_len_works_correctly(self):
        self.assertEqual(0, len(self.linkedlist))
        for x in range(10):
            self.linkedlist.push_front(x)
        self.assertEqual(10, len(self.linkedlist))

    def test_linkedlist_in_conditional_statements(self):
        self.assertFalse(self.linkedlist)
        self.linkedlist.push_front(1)
        self.assertTrue(self.linkedlist)

    def test_front_raises_exception(self):
        with self.assertRaises(IndexError):
            self.linkedlist.head()

    def test_front(self):
        for x in range(3):
            self.linkedlist.push_front(x)

        for x in reversed(range(3)):
            self.assertEqual(x, self.linkedlist.head())
            self.linkedlist.pop_front()

    @unittest.skip("till double-linked list is emplemented")
    def test_pop_back_from_empty_list_raises_exception(self):
        with self.assertRaises(IndexError):
            self.linkedlist.pop_back()

    @unittest.skip("till double-linked list is emplemented")
    def test_pop_back_from_one_element_list(self):
        self.linkedlist.push_back(1)
        self.assertEqual(1, self.linkedlist.pop_back())
        self.assertIsNone(self.linkedlist._head)
        self.assertIsNone(self.linkedlist._tail)
        self.assertEqual(0, self.linkedlist.size)

    @unittest.skip("till double-linked list is emplemented")
    def test_pop_back_from_two_element_list(self):
        self.linkedlist.push_back(1)
        self.linkedlist.push_back(2)
        self.assertEqual(2, self.linkedlist.pop_back())
        self.assertIsNotNone(self.linkedlist._head)
        self.assertIsNotNone(self.linkedlist._tail)
        self.assertEqual(self.linkedlist._head, self.linkedlist._tail)

    def tearDown(self):
        self.linkedlist = None
