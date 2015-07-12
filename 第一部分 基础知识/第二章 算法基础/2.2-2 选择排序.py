__author__ = 'PyBeaner'


def select_sort(alist):
    length = len(alist)
    for i in range(length - 1):
        min_ele = alist[i]
        min_pos = i
        for j in range(i + 1, length):
            ele = alist[j]
            if min_ele > ele:
                min_ele = ele
                min_pos = j
        if min_pos != i:
            alist[i], alist[min_pos] = min_ele, alist[i]


if __name__ == '__main__':
    from random import sample

    alist = sample(range(100), 10)

    select_sort(alist)
    print(alist)
