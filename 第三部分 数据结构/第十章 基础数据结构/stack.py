__author__ = 'PyBeaner'


class Stack:
    def isEmpty(self):
        return self.len == 0

    def __init__(self, arr=None):
        if arr is None:
            arr = []
        self.arr = arr
        self.len = len(arr)

    def push(self, x):
        self.arr.append(x)
        self.len += 1

    def pop(self):
        if self.isEmpty():
            raise Exception("underflow")
        self.len -= 1
        return self.arr.pop()


if __name__ == '__main__':
    s = Stack(list(range(3)))
    print(s.isEmpty())
    print(s.pop())
    print(s.pop())
    print(s.pop())
    # print(s.pop())  # pop from empty list

    s.push(10)
    print(s.pop())
