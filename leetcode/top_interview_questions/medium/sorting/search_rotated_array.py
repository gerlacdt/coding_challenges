"""Suppose an array sorted in ascending order is rotated at some
pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return
its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

"""

from typing import List
from collections import namedtuple


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(low, high):
            if low > high:
                return -1
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                return binary_search(low, mid - 1)
            return binary_search(mid + 1, high)

        if not nums:
            return -1
        pivot = self.findPivot(nums)
        if nums[pivot] == target:
            return pivot
        elif nums[pivot] >= target and nums[0] <= target:
            return binary_search(0, pivot - 1)
        return binary_search(pivot + 1, len(nums) - 1)

    def findPivot(self, nums: List[int]) -> int:
        def helper(low, high):
            mid = (low + high) // 2

            # this works because an array with a single element is
            # compared like arr[0] >= arr[-1], and that's the same
            if (mid == len(nums) - 1 and nums[mid] >= nums[mid - 1]) or (
                nums[mid] > nums[mid + 1]
            ):
                return mid
            if nums[mid] < nums[mid + 1] and nums[low] <= nums[mid]:
                return helper(mid + 1, high)
            return helper(low, mid - 1)

        return helper(0, len(nums) - 1)


def test1():
    sol = Solution()
    cases = [Case(([4, 5, 6, 7, 0, 1, 2], 0), 4), Case(([4, 5, 6, 7, 0, 1, 2], 3), -1)]
    for c in cases:
        nums, target = c.input
        actual = sol.search(nums, target)
        assert actual == c.expected


Case = namedtuple("Case", ["input", "expected"])


def testFindPivot():
    sol = Solution()
    cases = [
        Case([4, 5, 6, 7, 0, 1, 2], 3),
        Case([8, 9, 10, 1, 2, 3, 4, 5, 6, 7], 2),
        Case([1, 2, 3, 4, 5, 6, 7], 6),
        Case([4], 0),
        Case([1, 2], 1),
        Case([2, 1], 0),
        Case([5, 1, 3], 0),
    ]
    for c in cases:
        actual = sol.findPivot(c.input)
        assert actual == c.expected
