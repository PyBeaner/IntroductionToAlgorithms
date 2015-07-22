__author__ = 'PyBeaner'


class Node:
    def __init__(self, value):
        self.next = None
        self.value = value

    def __str__(self):
        return "Node({})<at {}>".format(self.value, id(self))


class SingleLinkedList:
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
        return self._getLength()

    def __len__(self):
        return self.length

    def _getTail(self):
        tail = self.head
        if tail is not None:
            while True:
                if tail.next is None:
                    break
                tail = tail.next
        return tail

    def isEmpty(self):
        return self.head is None

    def delete(self, node):
        if isinstance(node, Node):
            value = node.value
        else:
            value = node

        if self.isEmpty():
            raise Exception("cannot delete %s: not found" % value)
        if self.head.value == value:
            self.head = self.head.next
            return

        prev_node = self.head
        while prev_node and prev_node.next and prev_node.next.value != value:
            prev_node = prev_node.next
        if prev_node and prev_node.next and prev_node.next.value == value:
            prev_node.next = prev_node.next.next
        else:
            raise Exception("cannot delete %s: not found" % value)

    def append(self, node):
        node.next = None
        if self.tail:
            self.tail.next = node
        else:
            self.head = node

    def insert(self, node, pos=None):
        pos = pos if pos is not None else 0
        assert isinstance(node, Node)
        assert isinstance(pos, int) and pos >= 0
        if pos == 0:
            node.next = self.head
            self.head = node
        elif pos >= self.length:
            self.append(node)
        else:
            node_before = self.head
            for i in range(pos - 1):
                node_before = node_before.next
            node_after = node_before.next
            node_before.next = node
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

    def _getLength(self):
        length = 0
        node = self.head
        while node:
            length += 1
            node = node.next
        return length


if __name__ == '__main__':
    head = Node(0)
    dll = SingleLinkedList(head=head)
    for i in range(1, 5):
        dll.append(Node(i))

    dll.display()

    dll.insert(Node(-2), 5)
    dll.insert(Node(-1), 0)
    dll.insert(Node(-3), 3)
    dll.display()

    dll.delete(1)
    dll.display()
    # dll.delete(1) # not found
