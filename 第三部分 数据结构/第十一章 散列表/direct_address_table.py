__author__ = 'PyBeaner'


class Element:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class DirectAddressTable:
    def __init__(self):
        self._table = list([None for i in range(100)])

    def search(self, key):
        return self._table[key]

    def insert(self, ele):
        self._table[ele.key] = ele.value

    def delete(self, ele):
        del self._table[ele.key]


if __name__ == '__main__':
    dat = DirectAddressTable()
    e = Element(2,30)
    dat.insert(e)
    print(dat.search(2))
    dat.delete(e)
    print(dat.search(2))