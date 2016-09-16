import unittest

import ccipher


class EncodeStrTest(unittest.TestCase):

    def setUp(self):
        self.s = "abc"

    def test_exception_for_invalid_value(self):
        with self.assertRaises(ValueError):
            ccipher.encode_str(4, 1)

    def test_single_positive_shift(self):
        self.assertEqual("bcd", ccipher.encode_str(self.s, 1))

    def test_zero_shift(self):
        self.assertEqual(self.s, ccipher.encode_str(self.s, 0))

    def test_roundtrip_shift(self):
        self.assertEqual(self.s, ccipher.encode_str(self.s, 26))

    def test_double_roundtrip_shift(self):
        self.assertEqual(self.s, ccipher.encode_str(self.s, 52))

    def test_single_positive_shift_on_the_border(self):
        self.assertEqual(self.s, ccipher.encode_str("zab", 1))

    def test_single_negative_shift(self):
        self.assertEqual("zab", ccipher.encode_str(self.s, -1))

