def stringcompression(s):
    if not isinstance(s, str):
        raise ValueError()

    n = len(s)
    if n == 0:
        raise ValueError()

    r = []
    j = 0
    while j < n:
        i = j
        while j < n and s[i] == s[j]:
            j += 1

        r.append(s[i])
        r.append(str(j-i))

    return "".join(r)
