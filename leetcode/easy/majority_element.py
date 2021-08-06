"""Given an array nums of size n, return the majority element.

The majority element is the element that appears more than [n / 2]
times. You may assume that the majority element always exists in the
array.



Example 1:

Input: nums = [3,2,3]
Output: 3

Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2

"""

from collections import namedtuple, Counter
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = Counter(nums)
        majority = len(nums) // 2
        for n, count in counts.items():
            if count > majority:
                return n
        return 0


Case = namedtuple("Case", ["nums", "expected"])


def test():
    cases = [Case([3, 2, 3], 3), Case([2, 2, 1, 1, 1, 2, 2], 2)]
    sol = Solution()
    for c in cases:
        actual = sol.majorityElement(c.nums)
        assert actual == c.expected
