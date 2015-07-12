__author__ = 'PyBeaner'


def binary_add(a, b):
    a_chars = convert_to_binary(a)
    print("first num in binary:", a_chars)
    b_chars = convert_to_binary(b)
    print("second num in binary:", b_chars)

    len_a = len(a_chars)
    len_b = len(b_chars)

    min_len = min(len_a, len_b)
    plus_one = 0
    c_chars = []
    for i in range(min_len):
        a_char = a_chars[-1 - i]
        b_char = b_chars[-1 - i]
        sum = a_char + b_char + plus_one
        c_char = sum % 2
        c_chars.append(c_char)
        plus_one = 1 if sum >= 2 else 0

    max_len = max(len_a, len_b)
    if max_len > min_len:
        if max_len == len_a:
            longer = a_chars
        else:
            longer = b_chars
        for i in range(max_len - min_len):
            v = longer[-1 - min_len - i]
            v += plus_one
            c_char = v % 2
            plus_one = 1 if v >= 2 else 0
            c_chars.append(c_char)

    if plus_one:
        c_chars.append(1)
    c_chars.reverse()

    print("the sum of the two nums in binary:", c_chars)
    return c_chars


def convert_to_binary(n):
    chars = []
    while True:
        n, remainder = n // 2, n % 2
        chars.append(remainder)
        if not n:
            break
    chars.reverse()
    return chars


if __name__ == '__main__':
    binary_add(3, 4)
