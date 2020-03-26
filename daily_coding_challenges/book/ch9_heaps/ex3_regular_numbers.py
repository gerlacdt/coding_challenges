"""A regular number in mathematics is defined as one which evenly
divides some power of 60. Equivalently, we can say that a regular
number is one whose only prime divisors are 2,3 and 5.

Given an integer n, write a program that generates, in order, the
first n regular numbers.

"""

from heapq import heappop, heappush


def regularNumbers(n):
    h = [1]
    count = 0
    last = 0
    while count < n:
        current = heappop(h)
        if last < current:
            yield current
            count += 1
            heappush(h, current * 2)
            heappush(h, current * 3)
            heappush(h, current * 5)
        last = current


def test():
    n = 15
    actual = list(regularNumbers(n))
    expected = [1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, 18, 20, 24]
    assert actual == expected
