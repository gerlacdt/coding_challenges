"""Given a set of distinct integers, nums, return all possible
subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

"""

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """Solution with bit masking"""
        bits = 2 ** len(nums)
        results = []
        for i in range(bits):
            items = []
            for j in range(len(nums)):
                if i & (1 << j) > 0:
                    items.append(nums[j])
            results.append(items)

        return results

    def subsets2(self, nums: List[int]) -> List[List[int]]:
        """Solution with backtracking"""

        def helper(head, tail):
            if not tail:
                return [head]
            results = []
            results.extend(helper(head + [tail[0]], tail[1:]))
            results.extend(helper(head, tail[1:]))
            return results

        return helper([], nums)


def test():
    nums = [1, 2, 3]
    sol = Solution()
    actual = sol.subsets(nums)
    actual2 = sol.subsets2(nums)
    expected = [[3], [1], [2], [1, 2, 3], [1, 3], [2, 3], [1, 2], []]
    assert sorted(actual) == sorted(expected)
    assert sorted(actual2) == sorted(expected)
