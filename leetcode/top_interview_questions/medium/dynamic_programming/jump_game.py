"""Given an array of non-negative integers, you are initially
positioned at the first index of the array.

Each element in the array represents your maximum jump length at that
position.

Determine if you are able to reach the last index.

Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.


Example 2:

Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.

"""

from typing import List, Dict
import sys
from collections import namedtuple


class Solution:
    def canJumpGreedy(self, nums: List[int]) -> bool:
        lastPos = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= lastPos:
                lastPos = i
        return lastPos == 0

    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        table = [0] * n
        table[-1] = 1
        for i in range(n - 2, -1, -1):
            furthestJump = min(nums[i] + i, n - 1)
            for j in range(i + 1, furthestJump + 1):
                if table[j] == 1:
                    table[i] = 1
                    break
        return True if table[0] == 1 else False

    def canJumpRec(self, nums: List[int]) -> bool:
        def helper(index):
            if index >= len(nums) - 1:
                return True

            njumps = nums[index]
            for j in range(1, njumps + 1):
                result = helper(index + j)
                if result:
                    return True
            return False

        startIndex = 0
        return helper(startIndex)

    def canJumpMemo(self, nums: List[int]) -> bool:
        cache: Dict = {}

        def helper(index):
            nonlocal cache
            if index >= len(nums) - 1:
                return True

            if index in cache:
                return cache[index]

            njumps = nums[index]
            for j in range(1, njumps + 1):
                result = helper(index + j)
                if result:
                    cache[index] = result
                    return True
            cache[index] = False
            return False

        startIndex = 0
        return helper(startIndex)


Case = namedtuple("Case", ["nums", "expected"])


def testSmall():
    sol = Solution()
    cases = [
        Case([2, 3, 1, 1, 4], True),
        Case([3, 2, 1, 0, 4], False),
        Case([0], True),
        Case([0, 2, 3], False),
        Case([1, 2], True),
        Case([1, 0, 1, 0], False),
    ]

    for c in cases:
        actual = sol.canJumpRec(c.nums)
        actual2 = sol.canJumpMemo(c.nums)
        actual3 = sol.canJump(c.nums)
        assert actual == c.expected, "Case: {}".format(c)
        assert actual2 == c.expected, "Case: {}".format(c)
        assert actual3 == c.expected, "Case: {}".format(c)


def testBig():
    sol = Solution()
    nums = list(range(25000, 0, -1))
    nums.extend([1, 0, 0])
    actual = sol.canJumpGreedy(nums)
    expected = False
    assert actual == expected
