import unittest

import ccipher


class EncodeCharTest(unittest.TestCase):

    def test_exception_for_invalid_value(self):
        with self.assertRaises(ValueError):
            ccipher.encode_char("adfadsf", 1)

    def test_single_positive_shift(self):
        self.assertEqual("b", ccipher.encode_char("a", 1))

    def test_single_positive_shift_on_the_border(self):
        self.assertEqual("a", ccipher.encode_char("z", 1))

    def test_positive_shift(self):
        self.assertEqual("e", ccipher.encode_char("a", 4))

    def test_roundtrip_shift(self):
        self.assertEqual("z", ccipher.encode_char("z", 26))

    def test_double_roundtrip_shift(self):
        self.assertEqual("a", ccipher.encode_char("a", 52))

    def test_double_roundtrip_plus_one_shift(self):
        self.assertEqual("b", ccipher.encode_char("a", 53))

    def test_zero_shift(self):
        self.assertEqual("a", ccipher.encode_char("a", 0))

    def test_single_negative_shift(self):
        self.assertEqual("a", ccipher.encode_char("b", -1))

    def test_negative_shift(self):
        self.assertEqual("a", ccipher.encode_char("z", -25))

    def test_negative_roundtrip_shift(self):
        self.assertEqual("z", ccipher.encode_char("z", -26))

    def test_negative_double_roundtrip_shift(self):
        self.assertEqual("z", ccipher.encode_char("z", -52))
