"""Given an array containing n distinct numbers taken from
0, 1, 2,..., n, find the one that is missing from the array.


Example 1:
Input: [3,0,1]
Output: 2

Example 2:
Input: [9,6,4,2,3,5,7,0,1]
Output: 8
Note:

Your algorithm should run in linear runtime complexity. Could you
implement it using only constant extra space complexity?

"""

from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        bools = [False for i in range(len(nums)+1)]
        for n in nums:
            bools[n] = True
        return bools.index(False)

    def gauss(self, nums: List[int]) -> int:
        # expected = sum([i for i in range(len(nums)+1)])
        expected = (len(nums) * (len(nums)+1)) // 2
        actual = sum(nums)
        return expected - actual


def test():
    s = Solution()
    actual = s.missingNumber([3, 0, 1])
    actual2 = s.gauss([3, 0, 1])
    expected = 2
    assert actual == expected
    assert actual == actual2

    actual = s.missingNumber([9,6,4,2,3,5,7,0,1])
    actual2 = s.gauss([9,6,4,2,3,5,7,0,1])
    expected = 8
    assert actual == expected
    assert actual == actual2
