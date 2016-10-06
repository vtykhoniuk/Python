def fac1(x):
    if x <= 1:
        return 1

    return x * fac1(x-1)


def fac2(x):
    result = 1
    for i in range(1, x+1):
        result *= i

    return result
