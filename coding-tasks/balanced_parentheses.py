from datastructures import Stack


def balpar(s):
    l = Stack()

    d = {'[': ']', '(': ')', '{': '}'}

    for c in s:
        if c in d:
            l.push(c)
        elif c in d.values():
            if not l or d[l.pop()] != c:
                return False

    return len(l) == 0


def balpar2(s):
    l = []

    open_str = "[{("
    close_str = "]})"

    open_set = set(open_str)
    close_set = set(close_str)
    pairs = list(zip(open_str, close_str))

    for c in s:
        if c in open_set:
            l.append(c)
        elif c in close_set:
            if len(l) == 0 or (l.pop(), c) not in pairs:
                return False

    return len(l) == 0
