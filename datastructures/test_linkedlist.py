import unittest
from datastructures import LinkedList


class TestConstructor(unittest.TestCase):

    def test_default(self):
        l = LinkedList()
        self.assertIsNone(l._head)
        self.assertIsNone(l._tail)
        self.assertEqual(0, l.size)

    def test_list(self):
        l = LinkedList(from_list=[1, 2, 3])
        self.assertEqual(3, l.size)
        self.assertEqual(1, l.head())


class TestPush(unittest.TestCase):

    def setUp(self):
        self.l = LinkedList()

    def test_front_empty(self):
        self.l.push_front(1)
        self.assertIsNotNone(self.l._head)
        self.assertIsNotNone(self.l._tail)
        self.assertEqual(self.l._head, self.l._tail)
        self.assertEqual(1, self.l.size)

    def test_front_non_empty(self):
        self.l.push_front(1)
        self.l.push_front(2)
        self.assertEqual(2, self.l._head.value)
        self.assertEqual(1, self.l._tail.value)
        self.assertEqual(2, self.l.size)

    def test_back_empty(self):
        self.l.push_back(1)
        self.assertIsNotNone(self.l._head)
        self.assertIsNotNone(self.l._tail)
        self.assertEqual(self.l._head, self.l._tail)
        self.assertEqual(1, self.l.size)

    def test_back_non_empty(self):
        self.l.push_back(1)
        self.l.push_back(2)
        self.assertEqual(1, self.l._head.value)
        self.assertEqual(2, self.l._tail.value)
        self.assertEqual(2, self.l.size)


class TestPop(unittest.TestCase):

    def setUp(self):
        self.l = LinkedList()

    def test_front_empty_raises_exception(self):
        with self.assertRaises(IndexError):
            self.l.pop_front()

    def test_front_from_one_element_list(self):
        self.l.push_back(1)
        self.assertEqual(1, self.l.pop_front())
        self.assertIsNone(self.l._head)
        self.assertIsNone(self.l._tail)
        self.assertEqual(0, self.l.size)

    def test_front_from_two_elements_list(self):
        self.l.push_back(1)
        self.l.push_back(2)
        self.l.pop_front()
        self.assertIsNotNone(self.l._head)
        self.assertIsNotNone(self.l._tail)
        self.assertEqual(self.l._head, self.l._tail)

    def test_front_from_multielements_list(self):
        for x in range(10):
            self.l.push_back(x)

        self.l.pop_front()
        self.assertEqual(1, self.l._head.value)
        self.assertEqual(9, self.l._tail.value)


class TestSizedProtocol(unittest.TestCase):

    def setUp(self):
        self.l = LinkedList()

    def test_len(self):
        self.assertEqual(0, len(self.l))
        for x in range(10):
            self.l.push_front(x)
        self.assertEqual(10, len(self.l))

    def test_bool(self):
        self.assertFalse(self.l)
        self.l.push_front(1)
        self.assertTrue(self.l)


class TestHeadTail(unittest.TestCase):

    def setUp(self):
        self.l = LinkedList()

    def test_head_raises_exception(self):
        with self.assertRaises(IndexError):
            self.l.head()

    def test_head(self):
        for x in range(3):
            self.l.push_front(x)

        for x in reversed(range(3)):
            self.assertEqual(x, self.l.head())
            self.l.pop_front()

    def test_tail_raises_exception(self):
        with self.assertRaises(IndexError):
            self.l.tail()

    def test_tail(self):
        for x in range(3):
            self.l.push_back(x)

        self.assertEqual(2, self.l.tail())
        self.assertEqual(3, self.l.size)


class TestIterationProtocol(unittest.TestCase):

    def setUp(self):
        self.l = LinkedList()

    def test_iterator(self):
        self.l.push_back(1)
        i = iter(self.l)
        self.assertEqual(1, next(i))
        with self.assertRaises(StopIteration):
            next(i)

    def test_for_loop(self):
        n = 10
        for x in range(n):
            self.l.push_back(x)

        for x, y in enumerate(self.l, 0):
            self.assertEqual(x, y)

    def test_generator(self):
        n = 10
        for x in range(n):
            self.l.push_back(x)

        self.assertListEqual(list(range(n)), list(self.l))
