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

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self.size

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
        """Removes element from the top of the stack"""

        if not self._size:
            raise IndexError()

        value = self._head.value

        self._size -= 1

        # If it was last element of the list
        if self._size:
            self._head = self._head.next_node
        else:
            self._head = self._tail = None

        return value

    def head(self):
        """Returns element from the head of the list.
        Index error hasa been raised if list is empty"""

        if not self._size:
            raise IndexError()

        return self._head.value
