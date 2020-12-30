"""Given an array nums of n integers, are there elements a, b, c in
nums such that a + b + c = 0? Find all unique triplets in the array
which gives the sum of zero.

Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Example 2:

Input: nums = []
Output: []

Example 3:

Input: nums = [0]
Output: []

"""

from typing import List
from collections import namedtuple


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result: List[List[int]] = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            lo = i + 1
            hi = len(nums) - 1
            while lo < hi:
                current = nums[i] + nums[lo] + nums[hi]
                if current < 0:
                    lo += 1
                elif current > 0:
                    hi -= 1
                else:
                    result.append([nums[i], nums[lo], nums[hi]])
                    lo += 1
                    while nums[lo] == nums[lo - 1] and lo < hi:
                        lo += 1
        return result


Case = namedtuple("Case", ["nums", "expected"])


def test():
    sol = Solution()
    cases = [
        Case([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
        Case([], []),
        Case([0], []),
        Case([0, 1], []),
    ]

    for c in cases:
        actual = sol.threeSum(c.nums)
        assert sorted(actual) == sorted(c.expected), f"{c.nums}"
