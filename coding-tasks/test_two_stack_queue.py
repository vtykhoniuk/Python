import pytest
from two_stack_queue import TwoStackQueue


@pytest.fixture
def queue():
    return TwoStackQueue()


def _fill_the_queue(q, filename):
    with open(filename) as f:
        result = f.readline().rstrip()
        for instruction in map(lambda s: s.rstrip(), f):
            if instruction == 'd':
                q.dequeue()
            else:
                q.enqueue(instruction)

    return result


def test_push(queue):
    n = 10
    for x in range(n):
        queue.enqueue(x)

    for x in range(9, -1):
        assert x == queue.dequeue()


def test_queue1(queue):
    result = _fill_the_queue(queue, "./queue_test1.txt")
    assert result == "".join(queue.as_list())


def test_queue2(queue):
    result = _fill_the_queue(queue, "./queue_test2.txt")
    assert result == "".join(queue.as_list())


def test_queue3(queue):
    with pytest.raises(IndexError):
        _fill_the_queue(queue, "./queue_test3.txt")
