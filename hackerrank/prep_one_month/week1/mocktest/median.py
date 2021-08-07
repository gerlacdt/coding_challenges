"""

Find the median of the given array.

"""

from collections import namedtuple


def findMedian(arr):
    arr.sort()
    mid = len(arr) // 2
    return arr[mid]


Case = namedtuple("Case", ["arr", "expected"])


def test():
    cases = [Case([5, 3, 1, 2, 4], 3)]

    for c in cases:
        actual = findMedian(c.arr)
        assert actual == c.expected
