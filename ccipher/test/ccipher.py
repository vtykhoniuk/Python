import unittest

import ccipher


class CCipherTest(unittest.TestCase):

    def test_encode_char(self):
        """encode_char unit test"""

        self.assertRaises(ValueError, ccipher.encode_char, "adfadsf", 1)

        self.assertEqual("b", ccipher.encode_char("a", 1))
        self.assertEqual("a", ccipher.encode_char("z", 1))
        self.assertEqual("z", ccipher.encode_char("z", 26))
        self.assertEqual("c", ccipher.encode_char("a", 2))
        self.assertEqual("a", ccipher.encode_char("a", 0))
        self.assertEqual("a", ccipher.encode_char("a", 52))
        self.assertEqual("a", ccipher.encode_char("b", -1))
        self.assertEqual("a", ccipher.encode_char("z", -25))
        self.assertEqual("z", ccipher.encode_char("z", -26))
        self.assertEqual("z", ccipher.encode_char("z", -52))

    def test_encode_str(self):
        """encode_str unit test"""

        encoder = ccipher.encode_str(4, 1)
        with self.assertRaises(ValueError):
            next(encoder)

        s = "abc"
        self.assertEqual(("b", "c", "d"), tuple(ccipher.encode_str(s, 1)))
        self.assertEqual(tuple(s), tuple(ccipher.encode_str(s, 0)))
        self.assertEqual(tuple(s), tuple(ccipher.encode_str(s, 26)))
        self.assertEqual(tuple(s), tuple(ccipher.encode_str(s, 52)))
        self.assertEqual(tuple(s), tuple(ccipher.encode_str("zab", 1)))
        self.assertEqual(("z", "a", "b"), tuple(ccipher.encode_str("abc", -1)))
