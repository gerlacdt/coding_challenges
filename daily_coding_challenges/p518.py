"""Good morning! Here's your coding interview problem for today.

This problem was asked by Microsoft.

Given an array of numbers and a number k, determine if there are three
entries in the array which add up to the specified number k. For
example, given [20, 303, 3, 4, 25] and k = 49, return true as 20 + 4 +
25 = 49.

"""

from collections import namedtuple


class Solution:
    def solve(self, nums, k):
        for i, n in enumerate(nums):
            seen = set()
            k2 = k - n
            # solve the 2Sum problem
            for j, n2 in enumerate(nums):
                if i == j:
                    continue
                if n2 in seen:
                    return True
                seen.add(k2 - n2)
        return False


Case = namedtuple("Case", ["nums", "k", "expected"])


def test():
    cases = [
        Case([20, 303, 3, 4, 25], 49, True),
        Case([20, 303, 3, 4, 25], 50, False),
    ]
    sol = Solution()
    for c in cases:
        actual = sol.solve(c.nums, c.k)
        assert actual == c.expected, "Case: {}, {}".format(c.nums, c.k)
