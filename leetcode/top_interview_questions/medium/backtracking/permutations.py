"""Given a collection of distinct integers, return all possible
permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

"""

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        endResult = []

        def helper(head, tail):
            if not tail:
                endResult.append(head)
                return head
            for i in range(len(tail)):
                n = tail[i]
                helper(head + [n], tail[:i] + tail[i + 1 :])

        helper([], nums)
        return endResult


def test():
    nums = [1, 2, 3]
    sol = Solution()
    actual = sol.permute(nums)
    expected = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    print(actual)
    assert actual == expected
