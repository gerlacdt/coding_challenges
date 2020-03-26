"""Good morning! Here's your coding interview problem for today.

This problem was asked by Amazon.

There exists a staircase with N steps, and you can climb up either 1
or 2 steps at a time. Given N, write a function that returns the
number of unique ways you can climb the staircase. The order of the
steps matters.

For example, if N is 4, then there are 5 unique ways:

1, 1, 1, 1
2, 1, 1
1, 2, 1
1, 1, 2
2, 2

What if, instead of being able to climb 1 or 2 steps at a time, you
could climb any number from a set of positive integers X? For example,
if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.

N = 1 -> 1 (1)
N = 2 -> 2 (1 1, 2)
N = 3 -> 3 (1 1 1, 2 1, 1 2)
N = 4 -> 5 (see above)

F(N) = F(n-1) + F(n-2)

"""

from collections import namedtuple


def stairs(n):
    if n < 2:
        return 1
    return stairs(n-1) + stairs(n-2)


def stairs_x(n, X):
    if n == 0:
        return 1
    total = 0
    for v in X:
        if n - v >= 0:
            total += stairs_x(n-v, X)
    return total


def test():
    Case = namedtuple('Case', ['input1', 'expected'])
    cases = [Case(1, 1), Case(2, 2), Case(3, 3), Case(4, 5), Case(5, 8)]

    for c in cases:
        result = stairs(c.input1)
        assert result == c.expected

    for i in range(10):
        result = stairs_x(i, {1, 3, 5})
        print("F[{}] = {}".format(i, result))
