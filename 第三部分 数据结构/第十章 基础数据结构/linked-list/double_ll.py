__author__ = 'PyBeaner'


class Node:
    def __init__(self, value):
        self.prev = None
        self.next = None
        self.value = value

    def __str__(self):
        return "Node({})<at {}>".format(self.value, id(self))


class DoubleLinkedList:
    def __init__(self, head=None):
        assert isinstance(head, Node) or head is None
        self.head = head
        if head is None:
            self._length = 0
        else:
            self._length = 1

    @property
    def tail(self):
        return self._getTail()

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, value):
        self._length = value

    def __len__(self):
        return self.length

    def _getTail(self):
        tail = self.head
        length = 0
        if self.head is not None:
            length = 1
            while True:
                if tail.next is None:
                    break
                tail = tail.next
                length += 1
        self._length = length
        return tail

    def append(self, node):
        node.next = None
        node.prev = self.tail
        self.tail.next = node

    def insert(self, node, pos=None):
        pass

    def search(self, value):
        x = self.head
        while x is not None and x.value != value:
            x = x.next
        return x


if __name__ == '__main__':
    head = Node(0)
    dll = DoubleLinkedList(head=head)
    for i in range(10):
        dll.append(Node(i))

    print(dll.search(9))
