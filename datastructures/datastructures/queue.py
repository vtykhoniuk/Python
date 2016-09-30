from datastructures import LinkedList


class LinkedQueue(LinkedList):

    def enqueue(self, value):
        self.push_back(value)

    def dequeue(self):
        return self.pop_front()

    def peek(self):
        return self.head()
