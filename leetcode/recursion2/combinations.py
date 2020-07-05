"""
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""

from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        results: List = []

        def helper(assignment, rest):
            nonlocal results
            if not assignment and not rest:
                return
            elif not assignment:
                helper(rest[:1], rest[1:])
                helper([], rest[1:])
            else:
                if len(assignment) == k:
                    results.append(assignment)
                    return
                for i in range(len(rest)):
                    if i == len(rest) - 1:
                        helper(assignment + [rest[i]], [])
                    else:
                        helper(assignment + [rest[i]], rest[i + 1 :])

        helper([], list(range(1, n + 1)))
        return results

    def combine2(self, n: int, k: int) -> List[List[int]]:
        results = []

        def dfs(path, index):
            if len(path) == k:
                results.append(path)
                return
            for i in range(index, n + 1):
                dfs(path + [i], i + 1)

        dfs([], 1)
        return results


def test():
    sol = Solution()
    actual = sol.combine(4, 2)
    actual2 = sol.combine2(4, 2)
    expected = [
        [2, 4],
        [3, 4],
        [2, 3],
        [1, 2],
        [1, 3],
        [1, 4],
    ]
    assert sorted(actual) == sorted(expected)
    assert sorted(actual2) == sorted(expected)


def test1():
    sol = Solution()
    actual = sol.combine(4, 3)
    actual2 = sol.combine2(4, 3)
    expected = [
        [1, 2, 3],
        [1, 2, 4],
        [1, 3, 4],
        [2, 3, 4],
    ]
    assert sorted(actual) == sorted(expected)
    assert sorted(actual2) == sorted(expected)
