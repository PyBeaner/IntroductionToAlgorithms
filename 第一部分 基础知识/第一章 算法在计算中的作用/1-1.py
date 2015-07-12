# coding=utf-8
__author__ = 'PyBeaner'

from math import log, sqrt

# log(n)
def f1(t):
    return 2 ** t


# sqrt(n)
def f2(t):
    return t ** 2


# n
def f3(t):
    return t


# n*log(n) = log(n**n)
def f4(t):
    n = 2
    while n ** n <= 2 ** t:
        n += 1

    return n - 1


# n**2
def f5(t):
    return t ** 0.5


# n**3
def f6(t):
    return t ** (1 / 3)


# 2**n
def f7(t):
    return log(t, 2)


# n!
def f8(t):
    def factorial(n):
        if n <= 1:
            return 1
        return factorial(n - 1) * n

    n = 1
    while factorial(n) <= t:
        n += 1
    return n - 1


if __name__ == '__main__':

    print("1秒钟","\t\t\t", "1分钟")
    funcs = [f1, f2, f3, f4, f5, f6, f7, f8]
    for f in funcs:
        for t in [1, 1 * 60]:
            n = f(t)
            print("%e" % n, end="\t")
        print()
