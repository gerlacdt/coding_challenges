"""Good morning! Here's your coding interview problem for today.

This problem was asked by Apple.

Implement the function fib(n), which returns the nth number in the
Fibonacci sequence, using only O(1) space.

"""


from collections import namedtuple


def fib(n):
    current = 1
    prev = 1
    i = 1
    while i < n:
        i += 1
        tmp = prev
        prev = current
        current = tmp + current
    return prev


def test():
    Case = namedtuple("Case", ["input", "expected"])

    cases = [Case(1, 1), Case(2, 1), Case(3, 2), Case(4, 3), Case(5, 5),
             Case(6, 8), Case(10, 55)]

    for c in cases:
        actual = fib(c.input)
        assert actual == c.expected, "Case: {}".format(c)
