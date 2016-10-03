import unittest
from datastructures import LinkedStack
from stack_sort import stack_sort_1, stack_sort_2


class LinkedStackSortTest(unittest.TestCase):

    def setUp(self):
        self.l = [9, 1, 3, 5, 7, 2, 1]
        self.s = LinkedStack(self.l)

    def test_stack_sort_on_empty_stack(self):
        self.assertSequenceEqual(stack_sort_1(LinkedStack()), sorted([]))
        self.assertSequenceEqual(stack_sort_2(LinkedStack()), sorted([]))

    def test_stack_sort_1_on_one_element_stack(self):
        x = [1]
        s = LinkedStack(x)
        self.assertSequenceEqual(stack_sort_1(s), sorted(x))

    def test_stack_sort_2_on_one_element_stack(self):
        x = [1]
        s = LinkedStack(x)
        self.assertSequenceEqual(stack_sort_2(s), sorted(x))

    def test_stack_sort(self):
        self.assertSequenceEqual(stack_sort_1(self.s), sorted(self.l))

    def test_stack_sort_2(self):
        self.assertSequenceEqual(stack_sort_2(self.s), sorted(self.l))

    def tearDown(self):
        self.l = None
        self.s = None
