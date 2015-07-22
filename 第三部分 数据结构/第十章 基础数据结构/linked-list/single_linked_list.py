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
        if not isinstance(node, Node):
            node = self.search(node)
            if not node:
                raise Exception("cannot delete %s: not found" % node)

        next_node = node.next
        # replace this node with the next-node
        # assuming it is not the tail
        if next_node:
            node.value = next_node.value
            node.next = next_node.next
            return
        # it is the tail, so we need to get the previous one
        else:
            prev_node = self.getPrevious(node)
            if prev_node:
                prev_node.next = node.next
            # it is the head at the same time
            else:
                self.head = None

    def getPrevious(self, node):
        if node is self.head:
            return

        prev_node = self.head
        while prev_node and prev_node.next is not node:
            prev_node = prev_node.next
        if prev_node and prev_node.next is node:
            return prev_node

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
        for node in self:
            print(node)
        print("List End\n")

    def _getLength(self):
        length = 0
        node = self.head
        while node:
            length += 1
            node = node.next
        return length

    def reverse(self):
        length = self.length
        for i in range(length - 1):
            import copy
            node = copy.copy(self.head)
            self.head = self.head.next
            self.insert(node, length - i - 1)

    def __iter__(self):
        if self.isEmpty():
            raise StopIteration()
        node = self.head
        while node:
            yield node
            node = node.next


if __name__ == '__main__':
    head = Node(0)
    dll = SingleLinkedList(head=head)
    for i in range(1, 5):
        dll.append(Node(i))

    dll.display()

    print("Reversing...")
    dll.reverse()

    dll.display()
