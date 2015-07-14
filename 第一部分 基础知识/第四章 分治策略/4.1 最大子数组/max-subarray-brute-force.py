__author__ = 'PyBeaner'

threshold = -10**10
def find_max_subarray(alist):
    length = len(alist)
    max_sum = threshold
    left = right = 0
    for i in range(length):
        left_in_loop = right_in_loop = i
        sum_in_loop = 0
        max_sum_in_loop = threshold
        for j in range(i, length):
            sum_in_loop += alist[j]
            if sum_in_loop > max_sum_in_loop:
                max_sum_in_loop = sum_in_loop
                right_in_loop = j
        if max_sum_in_loop > max_sum:
            max_sum = max_sum_in_loop
            left = left_in_loop
            right = right_in_loop
    return left, right, max_sum


if __name__ == '__main__':
    from random import sample

    # alist = sample(range(-10, 0), 10)
    alist = sample(range(-10, 10), 10)
    print(alist)
    result = find_max_subarray(alist)
    print(result)
