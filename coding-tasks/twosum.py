def twosum(a, k):
    if not isinstance(a, list) or not isinstance(k, int):
        raise ValueError()

    d = {}
    for i in a:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    r = []

    for i in a:
        if not i in d:
            continue

        if d[i] == 1: del(d[i])
        else: d[i] -= 1

        j = k - i

        if not j in d:
            continue

        r.append((min([i, j]), max([i, j])))

        if d[j] == 1: del(d[k-i])
        else: d[k-i] -= 1

    return r

def twosumv2(a, k):
    if not isinstance(a, list) or not isinstance(k, int):
        raise ValueError()

    a.sort()

    j = len(a) - 1
    i = 0
    r = []
    while i < j:
        s = a[i] + a[j]
        if s == k:
            r.append((min(a[i], a[j]), max(a[i], a[j])))
            i += 1
            j -= 1
        elif s < k:
            i += 1
        else:
            j -= 1

    return r
