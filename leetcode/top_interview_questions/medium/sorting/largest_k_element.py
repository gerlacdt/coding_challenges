# coding: utf-8

"""Find the kth largest element in an unsorted array. Note that it is the
kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5

Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4


Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.

"""

from typing import List
from heapq import heappush, heappop


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for n in nums:
            # python defaults to a min-heap, so we need to negate the numbers
            heappush(heap, -n)
        result = 0
        for _ in range(k):
            result = heappop(heap)
        return -result  # reverse negation to get original value


def test():
    sol = Solution()
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    actual = sol.findKthLargest(nums, k)
    expected = 5
    assert actual == expected

    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 4
    actual = sol.findKthLargest(nums, k)
    expected = 4
    assert actual == expected
