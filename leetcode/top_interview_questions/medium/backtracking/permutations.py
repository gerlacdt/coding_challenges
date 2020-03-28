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
        def helper(head, tail):
            if not tail:
                return [head]
            results = []
            for i in range(len(tail)):
                results.extend(helper(head + [tail[i]], tail[:i] + tail[i + 1 :]))
            return results

        return helper([], nums)


def test():
    nums = [1, 2, 3]
    sol = Solution()
    actual = sol.permute(nums)
    expected = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    print(actual)
    assert actual == expected
