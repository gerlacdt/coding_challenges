"""Given an array of integers nums sorted in ascending order, find
the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]


Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

"""

from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary_search(low, high):
            if low > high:
                return None
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                return binary_search(low, mid - 1)
            return binary_search(mid + 1, high)

        index = binary_search(0, len(nums) - 1)
        if index == None:
            return [-1, -1]
        # expand left
        left = index
        while left >= 0 and nums[left] == target:
            left -= 1

        # expand right
        right = index
        while right < len(nums) and nums[right] == target:
            right += 1

        return [left + 1, right - 1]


def test1():
    sol = Solution()
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    actual = sol.searchRange(nums, target)
    expected = [3, 4]
    assert actual == expected


def test2():
    sol = Solution()
    nums = [5, 7, 7, 8, 8, 10]
    target = 6
    actual = sol.searchRange(nums, target)
    expected = [-1, -1]
    assert actual == expected


def test3():
    sol = Solution()
    nums = [1]
    target = 1
    actual = sol.searchRange(nums, target)
    expected = [0, 0]
    assert actual == expected
