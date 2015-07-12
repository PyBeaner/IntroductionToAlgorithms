__author__ = 'PyBeaner'


def insertion_sort(alist):
    length = len(alist)
    if length < 2:
        return

    for i in range(1, length):
        value = alist[i]
        while value < alist[i - 1] and i > 0:
            alist[i] = alist[i - 1]
            i -= 1
        alist[i] = value


if __name__ == '__main__':
    import random

    alist = random.sample(range(10), 10)
    print("original list:", alist)
    insertion_sort(alist)
    print("sorted list:", alist)
