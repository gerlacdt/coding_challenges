"""Given n pairs of parentheses, write a function to generate all
combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

"""

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        results = []

        def helper(val, left, right):
            print("{} {} {}".format(val, left, right))
            if left == n and right == n:
                results.append(val)
                return
            if left < n:
                helper(val + "(", left + 1, right)
            if left > right:
                helper(val + ")", left, right + 1)

        helper("", 0, 0)
        return results


def test():
    sol = Solution()
    actual = sol.generateParenthesis(3)
    expected = ["((()))", "(()())", "(())()", "()(())", "()()()"]
    assert sorted(actual) == sorted(expected)
