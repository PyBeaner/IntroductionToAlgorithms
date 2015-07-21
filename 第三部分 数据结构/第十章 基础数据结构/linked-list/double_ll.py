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
        self.head = head

    @property
    def tail(self):
        return self._getTail()

    def _getTail(self):
        tail = self.head
        if self.head is not None:
            while True:
                if tail.next is None:
                    break
                tail = tail.next
        return tail

    def append(self, node):
        node.next = None
        node.prev = self.tail
        self.tail.next = node

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
