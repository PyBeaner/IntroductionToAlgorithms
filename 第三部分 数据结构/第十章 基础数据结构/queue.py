__author__ = 'PyBeaner'


class Queue:
    def __init__(self, length=5):
        assert length > 0 and isinstance(length, int), "Length of a Queue must be at least 1."
        self._storage_len = length
        self.q = [0] * length
        self.head = 0
        # the next position to enqueue
        self.tail = 0
        self._length = 0

    def isEmpty(self):
        return self._length == 0

    def isFull(self):
        return self._length == self._storage_len

    def enqueue(self, x):
        if self.isFull():
            raise Exception("Queue is full")

        self.q[self.tail] = x
        if self.tail == self._storage_len - 1:
            self.tail = 0
        else:
            self.tail += 1

        self._length += 1

    def dequeue(self):
        if self.isEmpty():
            raise Exception("Queue is empty")
        x = self.q[self.head]
        if self.head == self._storage_len - 1:
            self.head = 0
        else:
            self.head += 1
        if self.head == self.tail:
            self.head = self.tail = 0
        self._length -= 1
        return x

    def show(self):
        if self.isEmpty():
            l = []
        elif self.head < self.tail:
            l = self.q[self.head:self.tail]
        else:
            l = self.q[self.head:self._storage_len] + self.q[:self.tail]

        print(l)


if __name__ == '__main__':
    q = Queue(2)
    print(q.head, q.tail)
    q.show()
    # q.dequeue()  # empty Queue

    q.enqueue(10)
    print(q.head, q.tail)
    q.show()

    q.dequeue()
    print(q.head, q.tail)
    q.show()

    q.enqueue(1)
    print(q.head, q.tail)
    q.show()
    q.enqueue(2)
    print(q.head, q.tail)
    q.show()

    q.dequeue()
    q.dequeue()
    # q.dequeue()
