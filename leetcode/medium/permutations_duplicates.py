"""Given a collection of numbers, nums, that might contain
duplicates, return all possible unique permutations in any order.



Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]


Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]


https://leetcode.com/problems/permutations-ii/
"""

from collections import namedtuple
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def helper(numbers, result):
            pass

        helper(nums, [])
        # uniquifiy result
        return []


Case = namedtuple("Case", ["nums", "expected"])


def test():
    sol = Solution()
    cases = [
        Case([1, 1, 2], [[1, 1, 2], [1, 2, 1], [2, 1, 1]]),
        Case(
            [1, 2, 3],
            [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]],
        ),
    ]
    for c in cases:
        actual = sol.permuteUnique(c.nums)
        assert actual == c.expected
