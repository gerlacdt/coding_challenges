"""Given a sorted array of distinct integers and a target value,
return the index if the target is found. If not, return the index
where it would be if it were inserted in order.

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4

Example 4:

Input: nums = [1,3,5,6], target = 0
Output: 0

Example 5:

Input: nums = [1], target = 0
Output: 0

"""

from collections import namedtuple
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i, n in enumerate(nums):
            if target == n:
                return i
            if target < n:
                return i
        return len(nums)


Case = namedtuple("Case", ["nums", "target", "expected"])


def test():
    cases = [
        Case([1, 3, 5, 6], 5, 2),
        Case([1, 3, 5, 6], 2, 1),
        Case([1, 3, 5, 6], 7, 4),
        Case([1, 3, 5, 6], 0, 0),
        Case([1], 0, 0),
    ]
    sol = Solution()
    for c in cases:
        actual = sol.searchInsert(c.nums, c.target)
        assert actual == c.expected, f"{c.nums} , {c.target}"
