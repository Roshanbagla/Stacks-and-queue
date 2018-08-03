"""Implementing queue."""


class Queue:
    """Class to implement QUEUE."""

    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return self.queue == []

    def enqueue(self, item):
        return self.queue.append(item)

    def dequeue(self):
        return self.queue.pop(0)

    def size(self):
        return len(self.queue)

    def elements(self):
        for i in self.queue:
            print(i)


q = Queue()
q.enqueue(14)
q.enqueue(20)
q.enqueue(100)
q.elements()
print (" ***** ")
q.dequeue()
q.dequeue()
q.elements()
