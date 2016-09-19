import unittest

from longestsum import longestsum


class LongestSumTest(unittest.TestCase):

    def test_longestsum_function_exists(self):
        longestsum([])

    def test_longestsum_raises_value_error(self):
        with self.assertRaises(ValueError):
            longestsum("Asdf");

    def test_longestsum_empty_list(self):
        self.assertEqual(0, longestsum([]))

    def test_longestsum_positive_values_list(self):
        self.assertEqual(10, longestsum([1,2,3,4]))

    def test_longestsum_with_negatives(self):
        self.assertEqual(11, longestsum([1,2,3,4,-1,2]))
        self.assertEqual(6, longestsum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))

    def test_longestsum_negative_values_list(self):
        self.assertEqual(-1, longestsum([-6, -5, -4, -1, -4, -5]))
