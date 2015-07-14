# coding=utf-8
__author__ = 'PyBeaner'

# 当前已经找到的最大子数组
max_sum = -10 ** 10
left = right = 0


def find_max_subarray(alist, low, high):
    global max_sum, left, right
    if low == high:
        if alist[low] > max_sum:
            left, right, max_sum = low, low, alist[low]
        return left, right, max_sum

    # find the max-subarray of the list exclude the high item
    sub_low, sub_high, sub_sum = find_max_subarray(alist, low, high - 1)
    high_value = alist[high]
    # 上一轮的结果是负数
    if sub_sum < 0:
        # 当前high的值大于零，直接舍弃上一轮的结果；否则下一步
        if high_value > sub_sum:
            left, right, max_sum = high, high, high_value
    else:
        # 除去上一轮的区间，剩下的item求和，大于零，则加上，否则不变
        remainder_sum = sum(alist[sub_high + 1:high + 1])
        if remainder_sum > 0:
            left, right, max_sum = sub_low, high, sub_sum + remainder_sum
        # 当前high的值大于所有的和，直接取high
        if high_value >= max_sum:
            left, right, max_sum = high, high, high_value
    return left, right, max_sum


if __name__ == '__main__':
    from random import sample

    alist = sample(range(-10, 10), 10)
    # alist = [4, -10, 6, -4, -1, 8, -9, 0, 1, -6]
    print(alist)
    result = find_max_subarray(alist, 0, 9)
    print(result)
