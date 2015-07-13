# coding=utf-8
__author__ = 'PyBeaner'


# sentinel card（哨兵牌）
MAX = 10 ** 10


def merge_without_sentinel(llist, rlist):
    len_l = len(llist)
    if len_l == 0:
        return rlist
    len_r = len(rlist)
    if len_r == 0:
        return llist
    length = len_l + len_r

    i = j = 0
    ret = []
    for k in range(length):
        # the left one ends
        if i == len_l:
            ret += rlist[j:]
            break
        # the right one ends
        if j == len_r:
            ret += llist[i:]
            break
        l_val = llist[i]
        r_val = rlist[j]
        if l_val < r_val:
            ret.append(l_val)
            i += 1
        else:
            ret.append(r_val)
            j += 1
    return ret


# O(n)
def merge(llist, rlist):
    len_l = len(llist)
    if len_l == 0:
        return rlist
    len_r = len(rlist)
    if len_r == 0:
        return llist
    length = len_l + len_r

    # 避免每次判断是否某个列表结束了
    llist.append(MAX)
    rlist.append(MAX)

    i = j = 0
    ret = []
    for k in range(length):
        l_val = llist[i]
        r_val = rlist[j]
        if l_val < r_val:
            ret.append(l_val)
            i += 1
        else:
            ret.append(r_val)
            j += 1
    return ret

# O( nlg(n) )
def merge_sort(alist):
    length = len(alist)
    if length <= 1:
        return alist
    if length == 2:
        return alist if alist[0] < alist[1] else [alist[1], alist[0]]

    half = length // 2
    llist = alist[:half]
    rlist = alist[half:]
    llist = merge_sort(llist)
    rlist = merge_sort(rlist)

    # return merge(llist, rlist)
    return merge_without_sentinel(llist, rlist)


# n^2： which n=k
def insertion_sort(alist):
    for i in range(1, len(alist)):
        value = alist[i]
        while value < alist[i - 1] and i > 0:
            alist[i] = alist[i - 1]
            i -= 1
        alist[i] = value
    return alist


# 当归并排序的子序列较小时，使用插入排序可能能获得更好的效率
# O( nlg(n/k) + nk )
def merge_sort_along_with_insertion_sort(alist, threshold_to_use_insertion):
    length = len(alist)
    if length <= threshold_to_use_insertion:
        # k^2 * n/k = nk
        return insertion_sort(alist)

    half = length // 2
    llist = alist[:half]
    rlist = alist[half:]
    llist = merge_sort_along_with_insertion_sort(llist, threshold_to_use_insertion)
    rlist = merge_sort_along_with_insertion_sort(rlist, threshold_to_use_insertion)

    # 共分解为n/k个部分，因此需要lg(n/k)次合并
    # lg(n/k) * (n+n/2+n/4+n/8..) = O( nlg(n/k) )
    return merge(llist, rlist)


if __name__ == '__main__':
    from random import sample

    alist = sample(range(100), 30)
    print("Before:")
    print(alist)
    print("After:")
    # alist = merge_sort(alist)
    alist = merge_sort_along_with_insertion_sort(alist, 5)
    print(alist)
