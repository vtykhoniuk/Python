import unittest
from datastructures import LinkedQueue


class TestConstructor(unittest.TestCase):

    def test_empty(self):
        LinkedQueue()

    def test_list(self):
        LinkedQueue([1, 2, 3, 4])


class TestSizeProtocol(unittest.TestCase):

    def test_empty(self):
        q = LinkedQueue()
        self.assertEqual(0, len(q))

    def test_five(self):
        q = LinkedQueue([1, 2, 3, 4, 5])
        self.assertEqual(5, len(q))


class TestQueueOperations(unittest.TestCase):

    def setUp(self):
        self.q = LinkedQueue()

    def test_queue_dequeue(self):
        with self.assertRaises(IndexError):
            self.q.dequeue()

        x = 1
        self.q.enqueue(x)
        self.assertEqual(1, len(self.q))
        self.assertEqual(x, self.q.dequeue())
        self.assertEqual(0, len(self.q))

        for x in range(10):
            self.q.enqueue(x)

        self.assertEqual(10, len(self.q))

        for x in range(10):
            self.assertEqual(x, self.q.dequeue())

    def test_peek(self):
        with self.assertRaises(IndexError):
            self.q.peek()

        self.q.enqueue(1)
        self.assertEqual(1, self.q.peek())
        self.assertEqual(1, len(self.q))
        self.q.enqueue(2)
        self.assertEqual(1, self.q.peek())
        self.assertEqual(2, len(self.q))


class TestQueue(unittest.TestCase):
    def setUp(self):
        self.q = LinkedQueue()

    @staticmethod
    def _fill_the_queue(q, filename):
        with open(filename) as f:
            result = f.readline().rstrip()
            for instruction in map(lambda s: s.rstrip(), f):
                if instruction == 'd':
                    q.dequeue()
                else:
                    q.enqueue(instruction)

        return result

    def test_queue1(self):
        result = TestQueue._fill_the_queue(self.q, "./queue_test1.txt")
        self.assertEqual(result, "".join(self.q))

    def test_queue2(self):
        result = TestQueue._fill_the_queue(self.q, "./queue_test2.txt")
        self.assertEqual(result, "".join(self.q))

    def test_queue3(self):
        with self.assertRaises(IndexError):
            result = TestQueue._fill_the_queue(self.q, "./queue_test3.txt")
