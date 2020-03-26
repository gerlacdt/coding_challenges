"""
Given an integer array nums, find the contiguous subarray
(containing at least one number) which has the largest sum and return
its sum.

Example:
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Follow up:

If you have figured out the O(n) solution, try coding another solution
using the divide and conquer approach, which is more subtle.

"""

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        table = [v for v in nums]
        for i in range(1, len(nums)):
            table[i] = max(table[i-1] + nums[i], nums[i])
        return max(table)


def test():
    sol = Solution()
    input1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    expected = 6
    result = sol.maxSubArray(input1)

    assert result == expected
