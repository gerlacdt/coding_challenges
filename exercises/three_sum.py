"""Given an array nums of n integers, are there elements a, b, c in
nums such that a + b + c = target? Return True if such a triplet
(a,b,c) exists. Otherwise return False.

"""

from typing import List
from collections import namedtuple


class Solution:
    def threeSum(self, nums: List[int], target: int) -> bool:
        for i in range(len(nums)):
            seen = {}
            for j in range(i + 1, len(nums)):
                x = target - nums[i] - nums[j]
                if x in seen:
                    return True
                seen[nums[j]] = j
        return False

    def threeSum2(self, nums: List[int], target: int) -> bool:
        for i in range(len(nums)):
            lo = i + 1
            hi = len(nums)
            while lo < hi:
                current = nums[i] + nums[lo] + nums[hi]
                if current < target:
                    lo += 1
                elif current > target:
                    hi -= 1
                else:
                    return True

        return False


Case = namedtuple("Case", ["nums", "target", "expected"])


def test():
    sol = Solution()
    cases = [
        Case([-1, 0, 1, 2, -1, -4], 0, True),
        Case([1, 2, 3, 4, 5], 9, True),
        Case([1, 2, 3, 4, 5], 8, True),
        Case([1, 2, 3, 4, 5], 13, False),
    ]

    for c in cases:
        actual = sol.threeSum(c.nums, c.target)
        assert actual == c.expected
