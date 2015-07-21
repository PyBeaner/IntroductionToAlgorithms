__author__ = 'PyBeaner'
from MyQueue import Queue


class Stack:
    def __init__(self, length=5):
        self.q1 = Queue(length)
        self.q2 = Queue(length)

    def push(self, x):
        self.q1.enqueue(x)

    def pop(self):
        if self.q1.isEmpty():
            raise Exception("Empty Stack")
        while len(self.q1) > 1:
            self.q2.enqueue(self.q1.dequeue())
        v = self.q1.dequeue()
        self.q1, self.q2 = self.q2, self.q1
        return v

    def isEmpty(self):
        return self.q1.isEmpty()


if __name__ == '__main__':
    s = Stack()
    for i in range(5):
        s.push(i)

    while not s.isEmpty():
        print(s.pop())