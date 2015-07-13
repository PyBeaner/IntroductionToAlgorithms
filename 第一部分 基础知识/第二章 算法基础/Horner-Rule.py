__author__ = 'PyBeaner'

from random import sample

coefficients = sample(range(10), 2)

# O(n)
def horner_rule(x):
    y = 0
    for i in range(len(coefficients) - 1):
        y = coefficients[i + 1] * x + coefficients[i]
    return y


# O(n^2)
def normal(x):
    y = 0
    for i in range(len(coefficients)):
        y += coefficients[i] * x ** i

    return y


if __name__ == '__main__':
    print(coefficients)
    y = horner_rule(10)
    print(y)
    y = normal(10)
    print(y)
