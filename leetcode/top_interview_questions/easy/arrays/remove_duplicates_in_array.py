# coding: utf-8

"""Given a sorted array nums, remove the duplicates in-place such that
each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by
modifying the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of
nums being 1 and 2 respectively.

It doesn't matter what you leave beyond the returned length.

Example 2:

Given nums = [0,0,1,1,1,2,2,3,3,4],

Your function should return length = 5, with the first five elements
of nums being modified to 0, 1, 2, 3, and 4 respectively.

It doesn't matter what values are set beyond the returned length.

"""

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        prev = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[prev]:
                prev += 1
                nums[prev] = nums[i]
        return prev + 1


def test():
    input1 = [1, 1, 2]
    sol = Solution()
    result = sol.removeDuplicates(input1)
    expected = 2
    assert result == expected

    input2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    result2 = sol.removeDuplicates(input2)
    expected2 = 5
    assert result2 == expected2
