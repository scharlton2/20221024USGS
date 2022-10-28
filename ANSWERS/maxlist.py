#!/usr/bin/env python

class MaxList(list):
    def __init__(self, max_size, iterable=None):
        self._max_size = max_size
        if iterable is not None:
            super().__init__(iterable)

    def append(self, value):
        if len(self) == self._max_size:
            raise IndexError("Maximum size reached")
        else:
            super().append(value)

if __name__ == '__main__':

    m = MaxList(3)

    for letter in 'abcdef':
        try:
            m.append(letter)
        except IndexError as err:
            print(err)
        print(m)

    print(type(m))
    print(isinstance(m, list))
    x = m[::]
    print(x)
    print(type(x))

    biglist = MaxList(20, [1, 2, 3])
    print(len(biglist))
