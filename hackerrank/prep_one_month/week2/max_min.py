"""

https://www.hackerrank.com/challenges/one-month-preparation-kit-angry-children/problem

"""

from collections import namedtuple


def maxMin(k, arr):
    arr.sort()
    totalMin = float("inf")

    for i in range(len(arr) - k + 1):
        # calc distance of k-len sub-array, store minimum
        current = arr[i + k - 1] - arr[i]
        if current < totalMin:
            totalMin = current
    return totalMin


Case = namedtuple("Case", ["k", "arr", "expected"])


def test1():
    cases = [Case(4, [1, 2, 3, 4, 10, 20, 30, 40, 100, 200], 3)]

    for c in cases:
        actual = maxMin(c.k, c.arr)
        assert actual == c.expected


def test2():
    test_input = """6327
571
6599
479
7897
9322
4518
571
6677
7432
815
6920
4329
4104
7775
5708
7991
5802
8619
6053
7539
7454
9000
3267
6343
7165
4095
439
5621
4095
153
1948
1018
6752
8779
5267
2426
9649
2190
9103
7081
3006
2376
7762
3462
151
3471
1453
2305
8442"""
    arr = [int(line) for line in test_input.splitlines()]
    k = 8
    expected = 816
    actual = maxMin(k, arr)
    assert actual == expected


def test3():
    test_input = """100
200
300
350
400
401
402"""
    arr = [int(line) for line in test_input.splitlines()]
    k = 3
    expected = 2
    actual = maxMin(k, arr)
    assert actual == expected
