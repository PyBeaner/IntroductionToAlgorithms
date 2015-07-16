__author__ = 'PyBeaner'


def partition(alist, l, r):
    x = alist[l]
    ret = l
    for i in range(l + 1, r + 1):
        if alist[i] < x:
            ret += 1
            alist[i], alist[ret] = alist[ret], alist[i]
    alist[l], alist[ret] = alist[ret], alist[l]
    return ret


def quick_sort(alist, l=None, r=None):
    if l is None:
        l = 0
    if r is None:
        r = len(alist) - 1
    if l >= r:
        return
    q = partition(alist, l, r)

    quick_sort(alist, l, q - 1)
    quick_sort(alist, q + 1, r)


if __name__ == '__main__':
    from random import sample

    alist = sample(range(10), 10)
    print(alist)
    quick_sort(alist)
    print(alist)
