__author__ = 'PyBeaner'
from MyQueue import Queue


class Deque(Queue):
    def enqueueFirst(self, x):
        if self.isFull():
            raise Exception("Queue is full")

        if self.head > 0:
            self.head -= 1
        else:
            self.head = self._storage_len - 1
        self.q[self.head] = x

        self._length += 1

    def dequeueLast(self):
        if self.isEmpty():
            raise Exception("Queue is empty")
        self.tail = self.tail - 1 if self.tail != 0 else self._storage_len - 1
        x = self.q[self.tail]

        self._length -= 1
        return x


if __name__ == '__main__':
    q = Deque(2)
    q.show()

    q.enqueue(10)
    q.enqueueFirst(5)
    q.show()

    q.dequeueLast()
    q.show()

    q.enqueue(1)
    q.show()

    q.dequeueLast()
    q.dequeue()
    q.show()
