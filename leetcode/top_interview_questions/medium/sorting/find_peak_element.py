"""A peak element is an element that is greater than its neighbors.

Given an input array nums, where nums[i] != nums[i+1], find a peak
element and return its index.

The array may contain multiple peaks, in that case return the index to
any one of the peaks is fine.

You may imagine that nums[-1] = nums[n] = -infinity

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.

Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 1 or 5
Explanation: Your function can return either index number 1 where the peak element is 2,
             or index number 5 where the peak element is 6.

Note:
Your solution should be in logarithmic complexity.

"""

from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        """Naive solution. Complexity O(n)"""
        for i in range(1, len(nums) - 1):
            if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
                return i
        return 0 if nums[0] > nums[-1] else len(nums) - 1

    def findPeakElement2(self, nums: List[int]) -> int:
        """Better complexity O(log n)"""

        def helper(low, high):
            if low == high:
                return low
            mid = (low + high) // 2
            if nums[mid] > nums[mid + 1]:
                return helper(low, mid)
            return helper(mid + 1, high)

        return helper(0, len(nums) - 1)


def test():
    sol = Solution()
    nums = [1, 2, 3, 1]
    actual = sol.findPeakElement(nums)
    actual2 = sol.findPeakElement2(nums)
    expected = 2
    assert actual == expected
    assert actual2 == expected

    nums = [1, 2, 1, 3, 5, 6, 4]
    actual = sol.findPeakElement(nums)
    actual2 = sol.findPeakElement2(nums)
    expected = set([1, 5])
    assert actual in expected
    assert actual2 in expected

    nums = [1, 2, 3, 4]
    actual = sol.findPeakElement(nums)
    actual2 = sol.findPeakElement2(nums)
    expected = set([3])
    assert actual in expected
    assert actual2 in expected

    nums = [4, 3, 2, 1]
    actual = sol.findPeakElement(nums)
    actual2 = sol.findPeakElement2(nums)
    expected = set([0])
    assert actual in expected
    assert actual2 in expected

    nums = [1]
    actual = sol.findPeakElement(nums)
    actual2 = sol.findPeakElement2(nums)
    expected = set([0])
    assert actual in expected
    assert actual2 in expected

    nums = [4, 3, 2, 1, 0, 5, 3]
    actual = sol.findPeakElement(nums)
    actual2 = sol.findPeakElement2(nums)
    expected = set([5, 0])
    assert actual in expected
    assert actual2 in expected
