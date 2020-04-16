"""mplement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a
non-negative integer.

Since the return type is an integer, the decimal digits are truncated
and only the integer part of the result is returned.

Example 1:

Input: 4
Output: 2


Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since
             the decimal part is truncated, 2 is returned.

"""

from collections import namedtuple
from statistics import mean


def fixpoint(f, firstGuess):
    tolerance = 0.1

    def isCloseEnough(val1, val2):
        return True if abs(val1 - val2) <= tolerance else False

    def helper(guess):
        nextGuess = f(guess)
        if isCloseEnough(guess, nextGuess):
            return nextGuess
        return helper(nextGuess)

    return helper(firstGuess)


class Solution:
    def mySqrt(self, x: int) -> int:
        i = 1
        while i * i <= x:
            i += 1
        return i - 1

    def mySqrt2(self, x: int) -> int:
        # handle special case in order to avoid DivisionByZero
        if x == 0:
            return 0
        return int(fixpoint(lambda y: mean([y, x / y]), x))

    def mySqrt3(self, x: int) -> int:
        def helper(low, high):
            # print("low: {} high: {}".format(low, high))
            if low > high:
                raise RuntimeError("No square root found for {}".format(x))
            mid = (low + high) // 2

            # check if mid is a possible answer
            if (mid - 1) ** 2 <= x < mid ** 2:
                return mid - 1
            if mid ** 2 <= x < (mid + 1) ** 2:
                return mid

            if mid ** 2 < x:
                return helper(mid + 1, high)
            return helper(low, mid - 1)

        return helper(0, (x // 2) + 1)


Case = namedtuple("Case", ["x", "expected"])


def test():
    cases = [
        Case(1, 1),
        Case(17, 4),
        Case(5, 2),
        Case(4, 2),
        Case(8, 2),
        Case(100, 10),
        Case(15, 3),
        Case(122, 11),
    ]
    sol = Solution()
    for c in cases:
        actual = sol.mySqrt(c.x)
        assert actual == c.expected, "Case: {}".format(c)


def test2():
    cases = [
        Case(1, 1),
        Case(17, 4),
        Case(5, 2),
        Case(4, 2),
        Case(8, 2),
        Case(100, 10),
        Case(15, 3),
        Case(122, 11),
    ]
    sol = Solution()
    for c in cases:
        actual = sol.mySqrt2(c.x)
        assert actual == c.expected, "Case: {}".format(c)


def test3():
    cases = [
        Case(1, 1),
        Case(17, 4),
        Case(5, 2),
        Case(4, 2),
        Case(8, 2),
        Case(100, 10),
        Case(15, 3),
        Case(122, 11),
    ]
    sol = Solution()
    for c in cases:
        actual = sol.mySqrt3(c.x)
        assert actual == c.expected, "Case: {}".format(c)
