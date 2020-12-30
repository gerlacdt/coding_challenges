"""Given an array of integers nums and an integer target, return
indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and
you may not use the same element twice.

You can return the answer in any order.


Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

"""

from typing import List, Dict
from collections import namedtuple


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen: Dict[int, int] = {}
        for i, n in enumerate(nums):
            x = target - n
            if x in seen:
                return [seen[x], i]
            seen[n] = i
        return []


Case = namedtuple("Case", ["nums", "target", "expected"])


def test():
    cases = [
        Case([2, 7, 11, 15], 9, [0, 1]),
        Case([3, 2, 4], 6, [1, 2]),
        Case([3, 3], 6, [0, 1]),
    ]
    sol = Solution()
    for c in cases:
        actual = sol.twoSum(c.nums, c.target)
        assert actual == c.expected
