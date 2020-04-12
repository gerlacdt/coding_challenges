# coding: utf-8

"""Given an array of size n, find the majority element. The majority
element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element
always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3


Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2

"""

from typing import List
from collections import Counter


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = Counter(nums)
        sortedList = sorted(counts.items(), key=lambda x: x[1])
        return sortedList[-1][0]


def test1():
    sol = Solution()
    nums = [3, 2, 3]
    actual = sol.majorityElement(nums)
    expected = 3
    assert actual == expected

    nums = [2, 2, 1, 1, 1, 2, 2]
    actual = sol.majorityElement(nums)
    expected = 2
    assert actual == expected
