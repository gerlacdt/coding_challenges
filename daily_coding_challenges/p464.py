"""Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given a set of distinct positive integers, find the largest subset
such that every pair of elements in the subset (i, j) satisfies either
i % j = 0 or j % i = 0.

For example, given the set [3, 5, 10, 20, 21], you should return [5,
10, 20]. Given [1, 3, 6, 24], return [1, 3, 6, 24].

"""

from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        nums.sort()
        n = len(nums)
        dp = [1] * n
        path = [-1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    path[i] = j
        # find max subset in dp table
        index = dp.index(max(dp))
        # rebuild path
        current = index
        result = []
        while current != -1:
            result.append(nums[current])
            current = path[current]
        return list(reversed(result))


def test():
    sol = Solution()

    nums = [3, 5, 10, 20, 21]
    actual = sol.largestDivisibleSubset(nums)
    expected = [5, 10, 20]
    assert actual == expected

    nums = [1, 3, 6, 24]
    actual = sol.largestDivisibleSubset(nums)
    expected = [1, 3, 6, 24]
    assert actual == expected
