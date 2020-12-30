"""Given an array nums of n integers and an integer target, find three
integers in nums such that the sum is closest to target. Return the
sum of the three integers. You may assume that each input would have
exactly one solution.



Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

"""

from collections import namedtuple
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff = float("inf")
        nums.sort()
        for i in range(len(nums)):
            lo, hi = i + 1, len(nums) - 1
            while lo < hi:
                summ = nums[i] + nums[lo] + nums[hi]
                if abs(target - summ) < abs(diff):
                    diff = target - summ
                if summ < target:
                    lo += 1
                else:
                    hi -= 1
                if diff == 0:
                    break
            if diff == 0:
                break
        return target - int(diff)


Case = namedtuple("Case", ["nums", "target", "expected"])


def test():
    sol = Solution()
    cases = [
        Case([-1, 2, 1, -4], 1, 2),
        Case([1, 1, 1, 0], -100, 2),
        Case([1, 1, -1, -1, 3], -1, -1),
    ]

    for c in cases:
        actual = sol.threeSumClosest(c.nums, c.target)
        assert actual == c.expected, f"nums: {c.nums} target: {c.target}"
