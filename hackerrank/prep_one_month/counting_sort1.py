"""

https://www.hackerrank.com/challenges/one-month-preparation-kit-countingsort1/problem

"""

from collections import namedtuple


def countingSort(arr):
    counter = [0] * 100

    # fill buckets
    for v in arr:
        counter[v] += 1

    return counter

    # create sorted array from buckets
    # result = []
    # for i, v in enumerate(counter):
    #     for _ in range(v):
    #         result.append(i)
    # return result


Case = namedtuple("Case", ["arr", "expected"])


def test():
    cases = [Case([1, 1, 3, 2, 1], [0, 3, 1, 1] + [0] * 96)]

    for c in cases:
        actual = countingSort(c.arr)
        assert actual == c.expected
