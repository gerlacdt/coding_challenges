"""Good morning! Here's your coding interview problem for today.

This problem was asked by Twitter.

A strobogrammatic number is a positive number that appears the same
after being rotated 180 degrees. For example, 16891 is
strobogrammatic.

Create a program that finds all strobogrammatic numbers with N digits.

"""

from collections import namedtuple


def toArr(n):
    arr = []
    while n > 0:
        arr.append(n % 10)
        n = n // 10
    return list(reversed(arr))


def isStrobo(num):
    arr = toArr(num)
    i = 0
    j = len(arr) - 1
    while i <= j:
        if (
            (arr[i] == 1 and arr[j] == 1)
            or (arr[i] == 8 and arr[j] == 8)
            or (arr[i] == 6 and arr[j] == 9)
            or (arr[i] == 9 and arr[j] == 6)
            or (arr[i] == 0 and arr[j] == 0)
        ):
            i += 1
            j -= 1
        else:
            return False
    return True


Case = namedtuple("Case", ["input", "expected"])


def test():
    cases = [
        Case(16891, True),
        Case(118899668811, True),
        Case(131, False),
        Case(816918, True),
        Case(808, True),
        Case(1001, True),
        Case(9696, True),
        Case(9966, True),
        Case(69, True),
        Case(1, True),
    ]
    for c in cases:
        actual = isStrobo(c.input)
        assert actual == c.expected


def testToArr():
    actual = toArr(123456789)
    expected = [i for i in range(1, 10)]
    assert actual == expected
