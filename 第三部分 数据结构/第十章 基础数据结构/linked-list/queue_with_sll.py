__author__ = 'PyBeaner'

from single_linked_list import SingleLinkedList, Node


class Queue:
    def __init__(self):
        self._sll = SingleLinkedList()

    def enqueue(self, value):
        node = Node(value)
        self._sll.append(node)

    def dequeue(self):
        if self._sll.isEmpty():
            raise Exception("Empty Queue")
        v = self._sll.head
        self._sll.head = self._sll.head.next

        return v.value


if __name__ == '__main__':
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)

    print(q.dequeue())
    print(q.dequeue())
    # print(q.dequeue())
