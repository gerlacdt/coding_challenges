"""
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false


https://leetcode.com/problems/contains-duplicate-ii/

"""

from collections import namedtuple, defaultdict
from typing import List, Dict


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        table: Dict[int, int] = {}
        for i, n in enumerate(nums):
            if n in table and i - table[n] <= k:
                return True
            else:
                table[n] = i

        return False


Case = namedtuple("Case", ["nums", "k", "expected"])


def test():
    cases = [
        Case([1, 2, 3, 1], 3, True),
        Case([1, 0, 1, 1], 1, True),
        Case([1, 2, 3, 1, 2, 3], 2, False),
    ]
    sol = Solution()
    for c in cases:
        actual = sol.containsNearbyDuplicate(c.nums, c.k)
        assert actual == c.expected
