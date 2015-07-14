# coding=utf-8
__author__ = 'PyBeaner'


def heapify(alist, i=0):
    # 使某个结点堆化，(前提：假设该结点的子节点都已堆化）
    length = len(alist)
    l = 2 * i
    r = 2 * i + 1
    smallest = i
    if l in alist:
        if l <= length and alist[l] < alist[i]:
            smallest = l
    if r in alist:
        if r <= length and alist[r] < alist[smallest]:
            smallest = r

    if smallest != i:
        alist[i], alist[smallest] = alist[smallest], alist[i]
        heapify(alist, smallest)


def build_heap(alist):
    length = len(alist)
    # 从叶子上层开始逐步往上层heapify
    for i in range(length // 2, -1, -1):
        heapify(alist, i)


if __name__ == '__main__':
    from random import sample

    alist = sample(range(10), 10)
    print(alist)

    build_heap(alist)
    print(alist)

    import heapq

    heapq.heapify(alist)
    print(alist)
