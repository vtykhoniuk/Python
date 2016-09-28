from datastructures import Stack


# Sort stack, using another stack
def stack_sort_1(s):
    r = []

    # Edge-case
    if not s:
        return r

    aux = Stack()

    while s:
        tmp = s.pop()
        if aux:
            while aux.peek() < tmp:
                s.push(aux.pop())
            aux.push(tmp)
        else:
            aux.push(tmp)

    while aux:
        r.append(aux.pop())

    return r


# Sort stack without using additional stack
def stack_sort_2(s):
    r = []

    # Edge-case
    if not s:
        return r

    _stack_sort(s)

    while s:
        r.append(s.pop())

    return r


def _stack_sort(s):
    if s:
        tmp = s.pop()
        _stack_sort(s)
        _stack_insert_sorted(s, tmp)


def _stack_insert_sorted(s, k):
    if not s or s.peek() > k:
        s.push(k)
    else:
        tmp = s.pop()
        _stack_insert_sorted(s, k)
        s.push(tmp)
