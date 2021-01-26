"""Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Note:

Each element in the result must be unique.
The result can be in any order.

https://leetcode.com/problems/intersection-of-two-arrays/

"""

from collections import namedtuple
from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))


Case = namedtuple("Case", ["nums1", "nums2", "expected"])


def test():
    sol = Solution()
    cases = [Case([1, 2, 2, 1], [2, 2], [2]), Case([4, 9, 5], [9, 4, 9, 8, 4], [9, 4])]

    for c in cases:
        actual = sol.intersection(c.nums1, c.nums2)
        assert actual == c.expected
