# coding=utf-8
__author__ = 'PyBeaner'


# O(lg(n))
# height = lg(i)
def heapify(alist, i=0, heap_size=None):
    # 使某个结点堆化，(前提：假设该结点的子节点都已堆化）
    if heap_size is None:
        heap_size = len(alist)
    l = 2 * i
    r = 2 * i + 1
    smallest = i
    if l < heap_size and alist[l] < alist[i]:
        smallest = l

    if r < heap_size and alist[r] < alist[smallest]:
        smallest = r

    if smallest != i:
        alist[i], alist[smallest] = alist[smallest], alist[i]
        heapify(alist, smallest, heap_size)


def heapify_max(alist, i=0, heap_size=None):
    if heap_size is None:
        heap_size = len(alist)
    l = 2 * i
    r = 2 * i + 1
    biggest = i
    if l < heap_size and alist[l] > alist[i]:
        biggest = l

    if r < heap_size and alist[r] > alist[biggest]:
        biggest = r

    if biggest != i:
        alist[i], alist[biggest] = alist[biggest], alist[i]
        heapify_max(alist, biggest, heap_size)


# O(nlg(n))
# O(n) # 每个节点调用heapify的时间和高度有关，最终可得到构建一个heap的时间复杂度是和线性的
def build_heap(alist, maxheap=False):
    length = len(alist)
    # 从叶子上层开始逐步往上层heapify
    if maxheap:
        for i in range(length // 2, -1, -1):
            heapify_max(alist, i)
    else:
        for i in range(length // 2, -1, -1):
            heapify(alist, i)


# O(nlg(n))
def heap_sort(alist):
    build_heap(alist, maxheap=True)
    heap_size = len(alist)
    for i in range(heap_size - 1, 0, -1):
        # 得到有效heap中最值
        alist[i], alist[0] = alist[0], alist[i]
        # 通过限制heap的大小，使得heapify的时候可以不影响已经得到的排好序的部分
        heapify_max(alist, 0, i)
        # 应该构建最大堆，可以避免此处的reverse
        # alist.reverse()


def heap_extract_max(maxheap, heap_size=None):
    # 从最大堆中提取最大值
    if heap_size is None:
        heap_size = len(maxheap)
    if heap_size == 0:
        raise Exception("heap underflow")
    max = maxheap[0]
    maxheap[0] = maxheap[heap_size - 1]
    heap_size -= 1
    heapify_max(maxheap, 0, heap_size)
    return max


def maxheap_increase_node(alist, i, value):
    if value <= 0:
        raise Exception("increasing value cannot be less than 1")
    alist[i] += value
    # 重新排序（此处不应该使用heapify，而是和parent对比）
    while i > 0 and alist[i] > alist[i // 2]:
        parent = i // 2
        alist[i], alist[parent] = alist[parent], alist[i]
        i = parent


if __name__ == '__main__':
    from random import sample

    alist = sample(range(100), 10)
    print(alist)

    build_heap(alist)
    print(alist)

    heap_sort(alist)
    print(alist)

    build_heap(alist, maxheap=True)
    print(alist)
    for i in range(len(alist)):
        print(heap_extract_max(alist, len(alist) - i), end=",")
    print()

    alist = sample(range(100), 10)
    build_heap(alist,maxheap=True)
    print(alist)
    maxheap_increase_node(alist,5,50)
    print(alist)
