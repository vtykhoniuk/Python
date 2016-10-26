import unittest
from coinchange import coin_change_ways_recursive


class TestEdgeCases(unittest.TestCase):

    def test_zero_sum(self):
        self.assertEqual(1, coin_change_ways_recursive([1, 2, 3], 0))

    def test_empty_coins_set(self):
        self.assertEqual(0, coin_change_ways_recursive([], 123))


class TestCoinChange(unittest.TestCase):

    def test_one_coin(self):
        self.assertEqual(1, coin_change_ways_recursive([1], 1))
        self.assertEqual(1, coin_change_ways_recursive([1], 2))
        self.assertEqual(0, coin_change_ways_recursive([2], 1))

    def test(self):
        self.assertEqual(2, coin_change_ways_recursive([1, 2], 2))
        self.assertEqual(3, coin_change_ways_recursive([1, 3, 5], 5))
