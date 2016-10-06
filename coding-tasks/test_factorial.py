import math

import factorial


def test_fac1():
    for x in range(10):
        assert math.factorial(x) == factorial.fac1(x)


def test_fac2():
    for x in range(10):
        assert math.factorial(x) == factorial.fac2(x)
