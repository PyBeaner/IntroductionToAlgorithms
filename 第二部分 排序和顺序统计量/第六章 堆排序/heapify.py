# coding=utf-8
__author__ = 'PyBeaner'


# O(lg(n))
# height = lg(i)
def heapify(alist, i=0):
    # 使某个结点堆化，(前提：假设该结点的子节点都已堆化）
    length = len(alist)
    l = 2 * i
    r = 2 * i + 1
    smallest = i
    if l < length and alist[l] < alist[i]:
        smallest = l

    if r < length and alist[r] < alist[smallest]:
        smallest = r

    if smallest != i:
        alist[i], alist[smallest] = alist[smallest], alist[i]
        heapify(alist, smallest)


# O(nlg(n))
# O(n) # 每个节点调用heapify的时间和高度有关，最终可得到构建一个heap的时间复杂度是和线性的
def build_heap(alist):
    length = len(alist)
    # 从叶子上层开始逐步往上层heapify
    for i in range(length // 2, -1, -1):
        heapify(alist, i)


def heap_sort(alist):
    sorted_list = []
    while alist:
        build_heap(alist)
        sorted_list.append(alist.pop(0))
    return sorted_list

if __name__ == '__main__':
    from random import sample

    alist = sample(range(100), 10)
    print(alist)

    build_heap(alist)
    print(alist)

    import heapq

    heapq.heapify(alist)
    print(alist)

    sort = heap_sort(alist)
    print(sort)