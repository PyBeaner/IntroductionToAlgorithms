# coding=utf-8
__author__ = 'PyBeaner'

threshold = -10 ** 10


def find_max_crossing_subarray(alist, low, mid, high):
    left_sum = threshold
    sum = 0
    max_left = mid
    for i in range(mid - 1, low - 1, -1):
        sum += alist[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i

    right_sum = threshold
    sum = 0
    max_right = mid
    for i in range(mid, high + 1):
        sum += alist[i]
        if sum > right_sum:
            right_sum = sum
            max_right = i

    return max_left, max_right, left_sum + right_sum


def find_max_subarray(alist, low, high):
    if low == high:
        return low, low, alist[low]

    mid = (high + low) // 2
    left_low, left_high, left_sum = find_max_subarray(alist, low, mid)
    right_low, right_high, right_sum = find_max_subarray(alist, mid + 1, high)
    cross_low, cross_high, cross_sum = find_max_crossing_subarray(alist, low, mid, high)
    if left_sum >= right_sum and left_sum >= cross_sum:
        return left_low, left_high, left_sum
    elif right_sum >= left_sum and right_sum >= cross_sum:
        return right_low, right_high, right_sum
    else:
        return cross_low, cross_high, cross_sum


if __name__ == '__main__':
    from random import sample

    alist = sample(range(-10, 10), 10)
    print(alist)
    low, high, sum = find_max_subarray(alist, 0, 9)
    print(low, high, sum)

    # 当所有元素都为负数时
    alist = sample(range(-20, -1), 10)
    print(alist)
    low, high, sum = find_max_subarray(alist, 0, 9)
    print(low, high, sum)
