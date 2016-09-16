import unittest

import ccipher


class EncodeStrTest(unittest.TestCase):

    def setUp(self):
        self.s = "abc"

    def test_exception_for_invalid_value(self):
        encoder = ccipher.encode_str(4, 1)
        with self.assertRaises(ValueError):
            next(encoder)

    def test_single_positive_shift(self):
        self.assertEqual(("b", "c", "d"), tuple(ccipher.encode_str(self.s, 1)))

    def test_zero_shift(self):
        self.assertEqual(tuple(self.s), tuple(ccipher.encode_str(self.s, 0)))

    def test_roundtrip_shift(self):
        self.assertEqual(tuple(self.s), tuple(ccipher.encode_str(self.s, 26)))

    def test_double_roundtrip_shift(self):
        self.assertEqual(tuple(self.s), tuple(ccipher.encode_str(self.s, 52)))

    def test_single_positive_shift_on_the_border(self):
        self.assertEqual(tuple(self.s), tuple(ccipher.encode_str("zab", 1)))

    def test_single_negative_shift(self):
        self.assertEqual(("z", "a", "b"), tuple(ccipher.encode_str(self.s, -1)))

