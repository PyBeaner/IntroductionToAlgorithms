# coding=utf-8
__author__ = 'PyBeaner'

import heapq
from random import sample

alist = sample(range(10), 10)
print(alist)
heapq.heapify(alist)
print(alist)

# 已经是一个最小堆
alist = list(range(10))
print(alist)
heapq.heapify(alist)
print(alist)

alist = list(range(10, 0, -1))
# maxheap
heapq._heapify_max(alist)
print(alist)
