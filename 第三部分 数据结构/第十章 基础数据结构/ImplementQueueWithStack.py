__author__ = 'PyBeaner'

from stack import Stack


class Queue:
    def __init__(self):
        self._s1 = Stack()
        self._s2 = Stack()

    def enqueue(self, x):
        self._s1.push(x)

    def dequeue(self):
        if self.isEmpty():
            raise Exception("Empty Queue")
        if self._s2.isEmpty():
            while not self._s1.isEmpty():
                self._s2.push(self._s1.pop())
        return self._s2.pop()

    def isEmpty(self):
        return self._s1.isEmpty() and self._s2.isEmpty()


if __name__ == '__main__':
    q = Queue()
    for i in range(10):
        q.enqueue(i)

    while not q.isEmpty():
        print(q.dequeue())

    # q.dequeue()
