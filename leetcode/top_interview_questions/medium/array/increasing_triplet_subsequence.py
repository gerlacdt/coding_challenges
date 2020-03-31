# coding: utf-8

"""Given an unsorted array return whether an increasing subsequence
of length 3 exists or not in the array.

Formally the function should:

Return true if there exists i, j, k
such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.
Note: Your algorithm should run in O(n) time complexity and O(1) space complexity.

Example 1:

Input: [1,2,3,4,5]
Output: true


Example 2:

Input: [5,4,3,2,1]
Output: false


https://www.geeksforgeeks.org/find-a-sorted-subsequence-of-size-3-in-linear-time/

"""

from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        smaller = [-1] * n
        localMinIndex = 0
        for i in range(1, n):
            if nums[i] <= nums[localMinIndex]:
                localMinIndex = i
            else:
                smaller[i] = localMinIndex

        greater = [-1] * n
        localMaxIndex = n - 1
        for i in range(n - 2, -1, -1):
            if nums[i] >= nums[localMaxIndex]:
                localMaxIndex = i
            else:
                greater[i] = localMaxIndex

        for i in range(1, n):
            if smaller[i] != -1 and greater[i] != -1:
                return True

        return False


def test():
    sol = Solution()
    nums = [1, 2, 3, 4, 5]
    actual = sol.increasingTriplet(nums)
    expected = True
    assert actual == expected

    nums = [1, 2, 3, 4, 5]
    actual = sol.increasingTriplet(nums)
    expected = True
    assert actual == expected

    nums = [10, 2, 1, 6, 2, 5, 4, 0]
    actual = sol.increasingTriplet(nums)
    expected = True  # triplet is 1,2,5
    assert actual == expected
