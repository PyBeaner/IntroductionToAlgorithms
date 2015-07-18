from random import sample

__author__ = 'PyBeaner'


def counting_sort(alist):
    # elements counts
    length = len(alist)
    counts = {}
    for i in range(length):
        v = alist[i]
        counts.setdefault(v, 0)
        counts[v] += 1

    # element position
    max_v = max(alist)
    min_v = min(alist)
    counts[min_v] = 0
    for i in range(min_v + 1, max_v + 1):
        counts.setdefault(i, 0)
        counts[i] += counts[i - 1]

    positions = counts
    ret = [0] * length
    for i in range(length - 1, -1, -1):
        v = alist[i]
        pos = positions[v]
        ret[pos] = v
        positions[v] -= 1
    return ret


if __name__ == '__main__':
    alist = sample(range(100), 10)
    print(alist)
    alist = counting_sort(alist)
    print(alist)
