__author__ = 'PyBeaner'


def find_max_crossing_subarray(alist, low, mid, high):
    left_sum = 0
    sum = 0
    max_left = mid
    for i in range(mid - 1, low, -1):
        sum += alist[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i

    right_sum = 0
    sum = 0
    max_right = mid
    for i in range(mid, high):
        sum += alist[i]
        if sum > right_sum:
            right_sum = sum
            max_right = i

    return (max_left, max_right, left_sum + right_sum)
