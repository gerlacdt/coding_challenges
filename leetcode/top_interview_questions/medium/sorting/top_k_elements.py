# coding: utf-8

"""Given a non-empty array of integers, return the k most frequent
elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]

Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where
n is the array's size.

"""

from typing import List
from collections import Counter
from operator import itemgetter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        pairs = [(key, val) for key, val in c.items()]
        sortedPairs = sorted(pairs, key=lambda x: x[1], reverse=True)[:k]
        return [p[0] for p in sortedPairs]


def test():
    sol = Solution()

    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    actual = sol.topKFrequent(nums, k)
    expected = [1, 2]
    assert actual == expected

    nums = [1]
    k = 1
    actual = sol.topKFrequent(nums, k)
    expected = [1]
    assert actual == expected

    nums = [3, 0, 1, 0]
    k = 1
    actual = sol.topKFrequent(nums, k)
    expected = [0]
    assert actual == expected

    nums = [4, 1, -1, 2, -1, 2, 3]
    k = 2
    actual = sol.topKFrequent(nums, k)
    expected = [-1, 2]
    assert actual == expected
