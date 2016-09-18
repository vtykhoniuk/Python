import unittest

from twosum import twosum, twosumv2

class Test2Sum(unittest.TestCase):

    def test_2sum_raises_exception(self):
        with self.assertRaises(ValueError):
            twosum('a', 1)

        with self.assertRaises(ValueError):
            twosum([], "a")

    def test_2sum_trivial(self):
        self.assertListEqual([(1, 3)], twosum([1,2,3], 4));
        self.assertListEqual([(1, 2)], twosum([1,2,3], 3));
        self.assertListEqual([(1, 3), (2,2)], twosum([1,3,2,2], 4));
        self.assertListEqual([(1, 2)], twosum([1,2,3,1], 3));
        self.assertListEqual([(-1, 11), (1, 9), (2, 8), (3, 7), (4, 6), (5, 5)], sorted(twosum([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1], 10)));

    def test_2sum_on_same_elements(self):
        self.assertListEqual([(2, 2), (2, 2)], twosum([2,2,2,2], 4))
        self.assertListEqual([(2, 2), (2, 2)], twosum([2,2,2,2,4], 4))
        self.assertListEqual([(0, 4), (2, 2), (2, 2)], sorted(twosum([2,2,0,2,2,4], 4)))

    def test_2sum_on_empty_set(self):
        self.assertListEqual([], twosum([], 4))

    def test_2sum_on_empty_set(self):
        self.assertListEqual([], twosum([], 4))


class Test2SumV2(unittest.TestCase):

    def test_2sum_raises_exception(self):
        with self.assertRaises(ValueError):
            twosumv2('a', 1)

        with self.assertRaises(ValueError):
            twosumv2([], "a")

    def test_2sum_trivial(self):
        self.assertListEqual([(1, 3)], twosumv2([1,2,3], 4));
        self.assertListEqual([(1, 2)], twosumv2([1,2,3], 3));
        self.assertListEqual([(1, 3), (2,2)], twosumv2([1,3,2,2], 4));
        self.assertListEqual([(1, 2)], twosumv2([1,2,3,1], 3));
        self.assertListEqual([(-1, 11), (1, 9), (2, 8), (3, 7), (4, 6), (5, 5)], sorted(twosumv2([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1], 10)));

    def test_2sum_on_same_elements(self):
        self.assertListEqual([(2, 2), (2, 2)], twosumv2([2,2,2,2], 4))
        self.assertListEqual([(2, 2), (2, 2)], twosumv2([2,2,2,2,4], 4))
        self.assertListEqual([(0, 4), (2, 2), (2, 2)], sorted(twosumv2([2,2,0,2,2,4], 4)))

    def test_2sum_on_empty_set(self):
        self.assertListEqual([], twosumv2([], 4))

    def test_2sum_on_empty_set(self):
        self.assertListEqual([], twosumv2([], 4))
