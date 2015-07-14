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


# O(nlg(n))
# O(n) # 每个节点调用heapify的时间和高度有关，最终可得到构建一个heap的时间复杂度是和线性的
def build_heap(alist):
    length = len(alist)
    # 从叶子上层开始逐步往上层heapify
    for i in range(length // 2, -1, -1):
        heapify(alist, i)

# O(nlg(n))
def heap_sort(alist):
    build_heap(alist)
    heap_size = len(alist)
    for i in range(heap_size - 1, 0, -1):
        # 得到有效heap中最值
        alist[i], alist[0] = alist[0], alist[i]
        # 通过限制heap的大小，使得heapify的时候可以不影响已经得到的排好序的部分
        heapify(alist, 0, i)
    # 应该构建最大堆，可以避免此处的reverse
    alist.reverse()


if __name__ == '__main__':
    from random import sample

    alist = sample(range(100), 10)
    print(alist)

    build_heap(alist)
    print(alist)

    heap_sort(alist)
    print(alist)
