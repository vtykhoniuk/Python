import unittest
from balanced_parentheses import balpar, balpar2


class TestBalancedParenthesesCheck(unittest.TestCase):

    def setUp(self):
        self.s1 = "Hello, World!"
        self.s2 = "{}"
        self.s3 = "[]"
        self.s4 = "()"
        self.s5 = "{{}}"
        self.s6 = "{{}"
        self.s7 = "{{}]"
        self.s8 = "{{"
        self.s9 = ""
        self.s10 = "[(1+2)*32+{123+345}]"
        self.s11 = "[(1+2)*32[+{123+345}]}"

    def test_empty_string(self):
        self.assertTrue(balpar(self.s9))
        self.assertTrue(balpar2(self.s9))

    def test_no_parentheses(self):
        self.assertTrue(balpar(self.s1))
        self.assertTrue(balpar2(self.s1))

    def test_one_pair_of_parentheses(self):
        self.assertTrue(balpar(self.s2))
        self.assertTrue(balpar(self.s3))
        self.assertTrue(balpar(self.s4))

        self.assertTrue(balpar2(self.s2))
        self.assertTrue(balpar2(self.s3))
        self.assertTrue(balpar2(self.s4))

    def test_unballanced(self):
        self.assertFalse(balpar(self.s6))
        self.assertFalse(balpar(self.s7))
        self.assertFalse(balpar(self.s8))
        self.assertFalse(balpar(self.s11))

        self.assertFalse(balpar2(self.s6))
        self.assertFalse(balpar2(self.s7))
        self.assertFalse(balpar2(self.s8))
        self.assertFalse(balpar2(self.s11))

    def test_ballanced(self):
        self.assertTrue(balpar(self.s5))
        self.assertTrue(balpar(self.s10))

        self.assertTrue(balpar2(self.s5))
        self.assertTrue(balpar2(self.s10))

    def tearDown(self):
        self.s1 = None
        self.s2 = None
        self.s3 = None
        self.s4 = None
        self.s5 = None
        self.s6 = None
        self.s7 = None
        self.s8 = None
        self.s9 = None
