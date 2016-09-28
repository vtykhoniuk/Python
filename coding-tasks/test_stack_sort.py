import unittest
from datastructures import Stack
from stack_sort import stack_sort_1, stack_sort_2


class StackSortTest(unittest.TestCase):

    def setUp(self):
        self.l = [9, 1, 3, 5, 7, 2, 1]
        self.s = Stack(self.l)

    def test_stack_sort_on_empty_stack(self):
        self.assertSequenceEqual(stack_sort_1(Stack()), sorted([]))
        self.assertSequenceEqual(stack_sort_2(Stack()), sorted([]))

    def test_stack_sort_1_on_one_element_stack(self):
        x = [1]
        s = Stack(x)
        self.assertSequenceEqual(stack_sort_1(s), sorted(x))

    def test_stack_sort_2_on_one_element_stack(self):
        x = [1]
        s = Stack(x)
        self.assertSequenceEqual(stack_sort_2(s), sorted(x))

    def test_stack_sort(self):
        self.assertSequenceEqual(stack_sort_1(self.s), sorted(self.l))

    def test_stack_sort_2(self):
        self.assertSequenceEqual(stack_sort_2(self.s), sorted(self.l))

    def tearDown(self):
        self.l = None
        self.s = None
