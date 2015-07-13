__author__ = 'PyBeaner'

# O(n^2)
def bubble_sort(alist):
    length = len(alist)
    for i in range(length - 1):
        for j in range(length - i - 1):
            if alist[j] > alist[j + 1]:
                alist[j], alist[j + 1] = alist[j + 1], alist[j]
    return alist


if __name__ == '__main__':
    from random import sample

    alist = sample(range(20), 10)
    print(alist)
    alist = bubble_sort(alist)
    print(alist)
