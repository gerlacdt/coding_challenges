"""Given an array nums of n integers, are there elements a, b, c in nums
such that a + b + c = 0? Find all unique triplets in the array which
gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

"""

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums2 = sorted(nums)
        result = set()
        length = len(nums2)
        for i in range(length):
            for j in range(i+1, length):
                for k in range(j+1, length):
                    if nums2[i] + nums2[j] + nums2[k] == 0:
                        result.add(tuple([nums2[i], nums2[j], nums2[k]]))
        # return list(map(lambda x: list(x), result))
        return result

    def threeSum2(self, nums: List[int]) -> List[List[int]]:
        result = set()
        for i in range(len(nums) - 1):
            seen = set()
            for j in range(i+1, len(nums)):
                if 0 - nums[i] - nums[j] in seen:
                    result.add(tuple(sorted((nums[i], nums[j], 0 - nums[i] - nums[j]))))
                seen.add(nums[j])
        # return list(map(lambda x: list(x), result))
        return result


def test():
    arr = [-1, 0, 1, 2, -1, -4]
    sol = Solution()
    result = sol.threeSum(arr)
    expected = {(-1, 0, 1), (-1, -1, 2)}
    assert result == expected

    result2 = sol.threeSum2(arr)
    assert result2 == expected

    assert result == result2

    # use different input
    arr = [-1, 0, 1, 2, -1, -4, 2]
    result2 = sol.threeSum2(arr)
    expected2 = {(-1, 0, 1), (-1, -1, 2), (-4, 2, 2)}
    assert result2 == expected2


def pairSum(arr, k):
    hashset = set()
    result = []
    for i in arr:
        if k - i in hashset:
            result.append((i, k-i))
        hashset.add(i)
    return result


def test_pair():
    input1 = [1, 2, 3, 0, 4, 7, -1]
    result = pairSum(input1, 3)
    expected = [(2, 1), (0, 3), (-1, 4)]

    assert result == expected


def test_big():
    arr = [0] * 1000
    sol = Solution()
    result = sol.threeSum2(arr)
