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
        self._getTail()
        return self._length

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
        pos = pos if pos is not None else 0
        assert isinstance(node, Node)
        assert isinstance(pos, int) and pos >= 0
        if pos == 0:
            node.next = self.head
            node.prev = None
            self.head.prev = node

            self.head = node
        elif pos >= self.length:
            self.append(node)
        else:
            node_after = self.head
            for i in range(pos):
                node_after = node_after.next
            node_before = node_after.prev

            node_before.next = node
            node_after.prev = node

            node.prev = node_before
            node.next = node_after

    def search(self, value):
        x = self.head
        while x is not None and x.value != value:
            x = x.next
        return x

    def display(self):
        print("Displaying Double Linked List:")
        node = self.head
        while True:
            if node:
                print(node)
                node = node.next
            else:
                break
        print("List End\n")


if __name__ == '__main__':
    head = Node(0)
    dll = DoubleLinkedList(head=head)
    for i in range(1, 5):
        dll.append(Node(i))

    # print(dll.search(4))
    # print(len(dll))

    dll.display()

    dll.insert(Node(-2), 5)
    dll.insert(Node(-1), 0)
    dll.insert(Node(-3), 3)
    dll.display()
