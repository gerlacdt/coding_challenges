"""Good morning! Here's your coding interview problem for today.

Given a real number n, find the square root of n. For example, given n
= 9, return 3.

"""

from pytest import approx

from collections import namedtuple


class Solution:
    def sqrt(self, n):
        delta = 0.01

        def fixpoint(f, guess):
            new_guess = f(guess)
            if delta >= abs(new_guess - guess):
                return new_guess
            return fixpoint(f, new_guess)

        return fixpoint(lambda x: (x + n / x) / 2, 1)


Case = namedtuple("Case", ["n", "expected"])


def test():
    cases = [Case(9, 3), Case(2, 1.414)]
    sol = Solution()
    for c in cases:
        actual = sol.sqrt(c.n)
        assert actual == approx(c.expected, rel=0.01), "Case: {}".format(c)
