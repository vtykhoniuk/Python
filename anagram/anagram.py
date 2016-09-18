from collections import defaultdict

def isanagram(s1, s2):
    if not isinstance(s1, str) or not isinstance(s2, str):
        raise ValueError()

    d1 = defaultdict(int)
    for c in s1:
        if c == " ": continue
        d1[c.lower()] += 1

    for c in s2:
        if c == " ": continue
        c = c.lower()
        if c not in d1: return False
          
        if d1[c] == 1:
            del(d1[c])
        else:
            d1[c] -= 1

    return False if d1 else True
