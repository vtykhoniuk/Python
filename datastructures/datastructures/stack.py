from .linkedlist import LinkedList


class LinkedStack(LinkedList):
    """FIFO queue representation"""

    def push(self, value):
        """Push element on the top of the stack"""

        self.push_front(value)

    def pop(self):
        """Removes and returns element from the top of the stack
        Raises IndexError if stack is empty"""

        return self.pop_front()

    def peek(self):
        """Returns element from the top of the stack
        Throws IndexError exception if stack is empty"""

        return self.head()
