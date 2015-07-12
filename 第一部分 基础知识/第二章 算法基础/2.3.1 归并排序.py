__author__ = 'PyBeaner'


# sentinel card���ڱ��ƣ�
MAX = 10 ** 10


def merge(llist, rlist):
    len_l = len(llist)
    len_r = len(rlist)
    length = len_l + len_r

    # ����ÿ���ж��Ƿ�ĳ���б������
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


def merge_sort(alist):
    length = len(alist)
    if length == 1:
        return alist
    half = length // 2
    llist = alist[:half]
    rlist = alist[half:]
    llist = merge_sort(llist)
    rlist = merge_sort(rlist)

    return merge(llist, rlist)


if __name__ == '__main__':
    from random import sample

    alist = sample(range(100), 20)
    print("Before:")
    print(alist)
    print("After:")
    alist = merge_sort(alist)
    print(alist)
