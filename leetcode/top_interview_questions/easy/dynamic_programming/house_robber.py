"""You are a professional robber planning to rob houses along a
street. Each house has a certain amount of money stashed, the only
constraint stopping you from robbing each of them is that adjacent
houses have security system connected and it will automatically
contact the police if two adjacent houses were broken into on the same
night.

Given a list of non-negative integers representing the amount of money
of each house, determine the maximum amount of money you can rob
tonight without alerting the police.

Example 1:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.

"""

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) < 3:
            return max(nums)
        table = [n for n in nums]
        for i in range(2, len(nums)):
            for j in range(2, i+1):
                table[i] = max(table[i], table[i-j] + nums[i], table[i-1])
        return table[-1]


def test():
    s = Solution()
    result = s.rob([1,2,3,1])
    expected = 4
    assert result == expected

    s = Solution()
    result = s.rob([2,7,9,3,1])
    expected = 12
    assert result == expected

    s = Solution()
    result = s.rob([1,10,2])
    expected = 10
    assert result == expected

    s = Solution()
    result = s.rob([2,1,1,2])
    expected = 4
    assert result == expected

    s = Solution()
    result = s.rob([1,2,1,1])
    expected = 3
    assert result == expected

    s = Solution()
    result = s.rob([2,7,9,3,1])
    expected = 12
    assert result == expected
