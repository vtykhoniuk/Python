class LinkedList:
    """Linked list representation"""

    class Node:
        """Linked list node representation"""

        def __init__(self, value=None, next_node=None):
            self._value = value
            self._next_node = next_node

        @property
        def value(self):
            """Get value of the node"""

            return self._value

        @property
        def next_node(self):
            """Get next node"""

            return self._next_node

        @next_node.setter
        def next_node(self, value):
            self._next_node = value

    class Iterator:
        """Linked list iterator

        Iterates through the linked list in current -> next order"""

        def __init__(self, l):
            self._current = l._head

        def __iter__(self):
            return self

        def __next__(self):
            if self._current:
                value = self._current.value
                self._current = self._current.next_node
                return value
            else:
                raise StopIteration()

        @property
        def current(self):
            return self._current

    def __init__(self, from_list=[]):
        self._head = None
        self._tail = None
        self._size = 0

        if from_list:
            for x in from_list:
                self.push_back(x)

    def __len__(self):
        return self.size

    def __iter__(self):
        return LinkedList.Iterator(self)

    @property
    def size(self):
        """Returns size of Linked List"""

        return self._size

    def push_front(self, value):
        """Adding new node to the front of the list"""

        self._head = LinkedList.Node(value, self._head)

        if not self._size:
            self._tail = self._head

        self._size += 1

    def push_back(self, value):
        """Adding new node to the back of the list"""

        new_node = LinkedList.Node(value)

        if self._size:
            self._tail.next_node = new_node
            self._tail = new_node
        else:
            self._head = self._tail = new_node

        self._size += 1

    def pop_front(self):
        """Removes element from the head of the list"""

        if not self._size:
            raise IndexError()

        value = self._head.value

        self._size -= 1

        if self._size:
            self._head = self._head.next_node
        else:
            self._head = self._tail = None

        return value

    def head(self):
        """Returns element from the head of the list.
        Index error has been raised if list is empty"""

        if not self._size:
            raise IndexError()

        return self._head.value

    def tail(self):
        """Returns element from the tail of the list.
        Index error has been raised if list is empty"""

        if not self._size:
            raise IndexError()

        return self._tail.value

    def reverse(self):
        """Reverse linked list

        Warning: This method will reverse the internal order of linked list
        nodes. The complexity is: O(n) time and O(1) space
        """

        if self._size <= 1:
            return

        prev = None
        node = self._head
        self._tail = node

        while True:
            tmp = node.next_node
            node.next_node = prev
            prev = node
            node = tmp

            if not node:
                break

        self._head = prev

    @staticmethod
    def detect_circle(l):
        """Detects whether the linked list has a circle and returns pointer
        to the LinkedList.Node a circle stats with
        """

        if not l:
            return

        slow = iter(l)
        next(slow)

        fast = iter(l)
        next(fast)

        try:
            while True:
                next(slow)
                next(fast)
                next(fast)
                if slow.current == fast.current:
                    k = 1
                    next(slow)
                    while slow.current != fast.current:
                        k += 1
                        next(slow)

                    fast = iter(l)
                    for _ in range(k):
                        next(fast)

                    slow = iter(l)
                    while slow.current != fast.current:
                        next(slow)
                        next(fast)

                    return slow.current

        except StopIteration:
            return

    @staticmethod
    def has_circle(l):
        """Checks whether linked list has a circle
        """

        return LinkedList.detect_circle(l) is not None
