"""Given an array with n objects colored red, white or blue, sort them
in-place so that objects of the same color are adjacent, with the
colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red,
white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]


Follow up:

A rather straight forward solution is a two-pass algorithm using
counting sort.  First, iterate the array counting number of 0's, 1's,
and 2's, then overwrite array with total number of 0's, then 1's and
followed by 2's.

Could you come up with a one-pass algorithm using only constant space?

"""

from typing import List
from collections import Counter


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c = Counter(nums)
        current = 0
        for key in range(3):
            val = c[key]
            for i in range(current, current + val):
                nums[i] = key
            current += val

    def sortColors2(self, nums: List[int]) -> None:
        n = len(nums)
        low = 0
        high = n - 1
        i = 0
        while i < n:
            # adjust low and high indices
            while nums[low] == 0 and low < n - 1:
                low += 1
            while nums[high] == 2 and high > 0:
                high -= 1
            if low <= high:
                if nums[i] == 2 and high > i:
                    nums[i], nums[high] = nums[high], nums[i]
                    if nums[i] != 0:
                        i += 1
                elif nums[i] == 0 and low < i:
                    nums[i], nums[low] = nums[low], nums[i]
                    if nums[i] != 2:
                        i += 1
                else:
                    i += 1
            else:
                break


def test():
    nums = [2, 0, 2, 1, 1, 0]
    sol = Solution()
    sol.sortColors(nums)
    expected = [0, 0, 1, 1, 2, 2]
    assert nums == expected


def test2():
    nums = [2, 0, 2, 1, 1, 0]
    sol = Solution()
    sol.sortColors2(nums)
    expected = [0, 0, 1, 1, 2, 2]
    assert nums == expected


def test2_1():
    nums = [1, 2, 0]
    sol = Solution()
    sol.sortColors2(nums)
    expected = [0, 1, 2]
    assert nums == expected
