"""Given an array nums, write a function to move all 0's to the end
of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.

"""

from collections import namedtuple
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        while i < len(nums) - 1:
            if nums[i] == 0:
                # swap with next non-zero value
                j = i + 1
                while j < len(nums):
                    if nums[j] != 0:
                        nums[i], nums[j] = nums[j], nums[i]
                        break
                    j += 1
                if j == len(nums):
                    break
            i += 1
        return None


def test():
    sol = Solution()
    Case = namedtuple('Case', ['input1', 'expected'])

    cases = [Case([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
             Case([1], [1]),
             Case([0, 1], [1, 0]),
             Case([0], [0]),
             Case([0, 0, 0, 1], [1, 0, 0, 0]),
             Case([0, 0, 0], [0, 0, 0])]

    for c in cases:
        sol.moveZeroes(c.input1)
        assert c.input1 == c.expected
