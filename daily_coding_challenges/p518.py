"""Good morning! Here's your coding interview problem for today.

This problem was asked by Microsoft.

Given an array of numbers and a number k, determine if there are three
entries in the array which add up to the specified number k. For
example, given [20, 303, 3, 4, 25] and k = 49, return true as 20 + 4 +
25 = 49.

"""


class Solution:
    def solve(self, nums, k):
        pass


def test():
    nums = [20, 303, 3, 4, 25]
    k = 49
    sol = Solution()
    actual = sol.solve(nums, k)
    expected = True
    assert actual == expected
