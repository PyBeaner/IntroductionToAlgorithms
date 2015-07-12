__author__ = 'PyBeaner'


def find_ele(alist, target):
    length = len(alist)

    for i in range(length):
        value = alist[i]
        if value == target:
            return i

if __name__ == '__main__':
    alist = [1,2,3,4,5,6,7,8,9]
    print(find_ele(alist,3))
