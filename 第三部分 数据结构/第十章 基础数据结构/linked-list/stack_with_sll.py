__author__ = 'PyBeaner'

from single_linked_list import SingleLinkedList, Node


class Stack:
    def __init__(self):
        self._sll = SingleLinkedList()

    def push(self, value):
        node = Node(value)
        self._sll.insert(node, pos=0)

    def pop(self):
        if self._sll.isEmpty():
            raise Exception("Empty Stack")

        node = self._sll.head
        self._sll.head = self._sll.head.next
        return node.value


if __name__ == '__main__':
    s = Stack()
    s.push(1)
    s.push(2)

    print(s.pop())
    print(s.pop())
