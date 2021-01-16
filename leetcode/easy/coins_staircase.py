"""You have a total of n coins that you want to form in a staircase
shape, where every k-th row must have exactly k coins.

Given n, find the total number of full staircase rows that can be formed.

n is a non-negative integer and fits within the range of a 32-bit signed integer.

Example 1:

n = 5

The coins can form the following rows:
0
0 0
0 0

Because the 3rd row is incomplete, we return 2.
Example 2:

n = 8

The coins can form the following rows:
0
0 0
0 0 0
0 0

Because the 4th row is incomplete, we return 3.

"""

from collections import namedtuple


class Solution:
    def arrangeCoins(self, n: int) -> int:
        lo, hi = 0, n
        while lo <= hi:
            k = (lo + hi) // 2  # mid of range
            curr = (k * (k + 1)) // 2
            if curr == n:
                return k
            if n < curr:
                hi = k - 1
            else:
                lo = k + 1
        return hi

    def iterative(self, n: int) -> int:
        total = 0
        step = 1
        while n - step >= 0:
            n -= step
            step += 1
            total += 1

        return total


Case = namedtuple("Case", ["n", "expected"])


def test():
    sol = Solution()
    cases = [Case(8, 3)]  # Case(5, 2),
    for c in cases:
        actual = sol.arrangeCoins(c.n)
        assert actual == c.expected, f"{c.n}"
