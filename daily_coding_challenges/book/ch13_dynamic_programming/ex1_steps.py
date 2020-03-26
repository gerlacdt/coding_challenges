"""There exists a staircase with n steps which you can climb up either
1 or 2 steps at a time. Given n, write a function that returns the
number of unique ways you can climb up the staircase. The order of the
steps matters.

Example n = 4:
[1,1,1,1]
[2,1,1]
[1,2,1]
[1,1,2]
[2,2]

Follow-up: What if, instead of being able to climb 1 or 2 steps at a
time, you could climb any number from a set of positive integers X?
"""

from collections import namedtuple


def stairs(n, X=set([1, 2])):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    result = 0
    for step in X:
        result += stairs(n - step, X)
    return result


def stairsBottomUp(n, X=set([1, 2])):
    table = {0: 1}
    for i in range(1, n + 1):
        table[i] = 0
        for step in X:
            table[i] += table.get(i - step, 0)
    return table[n]


def stairsMemo(n, X=set([1, 2])):
    cache = {}

    def helper(n):
        if n == 0:
            return 1
        elif n < 0:
            return 0
        elif n in cache:
            return cache[n]
        result = 0
        for step in X:
            result += helper(n - step)
        cache[n] = result
        return result

    return helper(n)


def testNSteps():
    actual = stairs(5, set([1, 3, 5]))
    expected = 5
    assert actual == expected


def testAll():
    Case = namedtuple("Case", ["input", "expected"])
    cases = [
        Case(0, 1),
        Case(1, 1),
        Case(2, 2),
        Case(3, 3),
        Case(4, 5),
        Case(5, 8),
        Case(10, 89),
    ]

    for c in cases:
        actual1 = stairs(c.input)
        actual2 = stairsBottomUp(c.input)
        actual3 = stairsMemo(c.input)
        assert actual1 == c.expected
        assert actual2 == c.expected
        assert actual3 == c.expected
