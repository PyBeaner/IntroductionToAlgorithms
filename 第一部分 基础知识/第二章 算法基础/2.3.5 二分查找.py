# coding=utf-8

__author__ = 'PyBeaner'


# lg(n)
def bisection_search(alist, target, offset=0):
    # assume the list is already sorted
    # offset: 当前列表相对于整个列表的位置
    length = len(alist)
    if length == 1:
        return offset if alist[0] == target else None
    if length == 0:
        return None

    mid = length // 2
    if alist[mid] == target:
        return mid + offset
    if alist[mid] > target:
        return bisection_search(alist[:mid], target, offset=offset)

    if alist[mid] < target:
        offset += mid + 1
        return bisection_search(alist[mid + 1:], target, offset=offset)


if __name__ == '__main__':
    from random import sample

    alist = sample(range(30), 20)
    alist = sorted(alist)
    found = bisection_search(alist, 10)
    print(alist)
    if found is not None:
        print("Found target at ", found)
        print(alist[found] == 10)
    else:
        print("Not found")
