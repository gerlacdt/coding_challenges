"""Given an array nums of n integers where n > 1, return an array
output such that output[i] is equal to the product of all the elements
of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The
output array does not count as extra space for the purpose of space
complexity analysis.)

"""

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix list
        prefix = []
        for v in nums:
            if not prefix:
                prefix.append(v)
            else:
                prefix.append(prefix[-1] * v)

        # suffix list
        suffix = nums[:]
        for i in range(len(nums)-2, -1, -1):
            suffix[i] = suffix[i] * suffix[i+1]

        # compose complete list
        result = []
        for i in range(len(nums)):
            if i == 0:
                result.append(suffix[i+1])
            elif i == len(nums) - 1:
                result.append(prefix[i-1])
            else:
                result.append(prefix[i-1] * suffix[i+1])
        return result


def test():
    input1 = [3, 2, 1]
    expected1 = [2, 3, 6]
    sol = Solution()
    result1 = sol.productExceptSelf(input1)
    assert result1 == expected1

    input2 = [1, 2, 3, 4, 5]
    expected2 = [120, 60, 40, 30, 24]
    result2 = sol.productExceptSelf(input2)
    assert result2 == expected2
