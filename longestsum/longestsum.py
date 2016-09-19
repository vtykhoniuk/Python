def longestsum(a):
    if not isinstance(a, list):
        raise ValueError()

    if len(a) == 0:
        return 0

    sum_here = sum_so_far = a[0]
    for x in a[1:]:
        sum_here = max(x, sum_here + x)
        sum_so_far = max(sum_so_far, sum_here)

    return sum_so_far
