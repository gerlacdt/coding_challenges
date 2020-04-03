"""https://leetcode.com/explore/interview/card/top-interview-questions-medium/111/dynamic-programming/810/

Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4

Explanation: The longest increasing subsequence is [2,3,7,101],
therefore the length is 4.  Note:

There may be more than one LIS combination, it is only necessary for
you to return the length.  Your algorithm should run in O(n2)
complexity.  Follow up: Could you improve it to O(n log n) time
complexity?


Given an array, find the longest increasing subsequence.

L(0) = 0
L(1) = 1
L(j) = 1 + max(L(1), L(2), L(3), ... L(j-1))

"""


from collections import namedtuple
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        table = [1 for i in range(len(nums))]
        prev = [
            -1 for i in range(len(nums))
        ]  # variable to reconstruct the whole subsequence not only the max length
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    table[i] = max(1 + table[j], table[i])
                    prev[i] = j

        # collect path
        result = max(table)
        index = table.index(result)
        path = []
        while index != -1:
            path.append(nums[index])
            index = prev[index]

        print("path values: {}".format(list(reversed(path))))
        return result


def test():
    Case = namedtuple("Case", ["input1", "expected"])
    cases = [
        Case([], 0),
        Case([1], 1),
        Case([1, 2, 3, 4], 4),
        Case([10, 9, 2, 5, 3, 7, 101, 18], 4),
        Case([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15], 6),
    ]

    for c in cases:
        sol = Solution()
        result = sol.lengthOfLIS(c.input1)
        assert result == c.expected
