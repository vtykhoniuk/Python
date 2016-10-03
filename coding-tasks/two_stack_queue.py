from datastructures import LinkedStack


class TwoStackQueue:

    def __init__(self):
        self._push_stack = LinkedStack()
        self._pop_stack = LinkedStack()

    @property
    def push_stack(self):
        return self._push_stack

    @property
    def pop_stack(self):
        return self._pop_stack

    def enqueue(self, value):
        self.push_stack.push(value)

    def dequeue(self):
        if not self.pop_stack:
            while self.push_stack:
                self.pop_stack.push(self.push_stack.pop())

        return self.pop_stack.pop()

    def as_list(self):
        while self.push_stack:
            self.pop_stack.push(self.push_stack.pop())

        l = []
        while self.pop_stack:
            l.append(self.pop_stack.pop())

        return l
