# coding=utf-8
from random import sample

__author__ = 'PyBeaner'


# 原插入排序
def insertion_sort(alist):
    for i in range(1, len(alist)):
        value = alist[i]
        while value < alist[i - 1] and i > 0:
            alist[i] = alist[i - 1]
            i -= 1
        alist[i] = value


# 利用二分查找的插入排序
# nlg(n)
def insertion_sort_using_bisection(alist):
    for i in range(1, len(alist)):
        value = alist[i]
        # lg(n/2)
        pos = bisection_search_position(alist[:i], value)
        alist[pos+1:i+1] = alist[pos:i]
        alist[pos] = value


def bisection_search_position(alist, target, offset=0):
    length = len(alist)
    if length == 1:
        return offset if alist[0] > target else offset + 1
    if length == 0:
        return offset

    mid = length // 2
    if alist[mid] == target:
        return mid + offset
    if alist[mid] > target:
        return bisection_search_position(alist[:mid], target, offset=offset)

    if alist[mid] < target:
        offset += mid + 1
        return bisection_search_position(alist[mid + 1:], target, offset=offset)


if __name__ == '__main__':
    alist = sample(range(20), 10)
    print(alist)
    insertion_sort_using_bisection(alist)
    print(alist)
