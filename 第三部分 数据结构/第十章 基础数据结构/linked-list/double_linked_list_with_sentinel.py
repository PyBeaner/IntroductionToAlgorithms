# coding=utf-8
__author__ = 'PyBeaner'

from double_linked_list import Node

# The next of the tail and the prev of the head
class Sentinel:
    def __init__(self):
        self.prev = None
        self.next = None


class DoubleLinkedList:
    def __init__(self):
        self._length = 0
        sentinel = Sentinel()
        # 哨兵指向哨兵，表示链表为空
        sentinel.prev = Sentinel()
        sentinel.next = Sentinel()
        self._sentinel = sentinel

    @property
    def tail(self):
        tail = self._sentinel.prev
        if isinstance(tail, Node):
            return tail
        # the tail is the sentinel itself
        return self._sentinel

    @property
    def head(self):
        head = self._sentinel.next
        if isinstance(head, Node):
            return head
        # the head is the sentinel itself
        return self._sentinel

    @property
    def length(self):
        return self._getLength()

    def _getLength(self):
        length = 0
        while True:
            next = self._sentinel.next
            if isinstance(next, Node):
                length += 1
            else:
                break

    def __len__(self):
        return self.length

    def delete(self, node):
        if not isinstance(node, Node):
            node = self.search(node)
            if not node:
                raise ValueError("cannot delete a non-existing node")
        # There is a sentinel
        node.prev.next = node.next
        node.next.prev = node.prev

    def append(self, node):
        node.next = self._sentinel
        node.prev = self.tail
        self.tail.next = node
        self._sentinel.prev = node

    def search(self, value):
        x = self.head
        while isinstance(x, Node) and x.value != value:
            x = x.next
        if isinstance(x, Node):
            return x

    def display(self):
        print("Displaying Double Linked List:")
        node = self.head
        while True:
            if isinstance(node, Node):
                print(node)
                node = node.next
            else:
                break
        print("List End\n")


if __name__ == '__main__':
    dll = DoubleLinkedList()
    for i in range(1, 5):
        dll.append(Node(i))

    print(dll.search(4))
    # print(len(dll))

    dll.display()

    dll.delete(3)
    dll.delete(1)
    # dll.delete(11) # not-existing...
    dll.display()
