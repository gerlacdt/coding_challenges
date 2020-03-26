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
from collections import namedtuple


class Solution:
    def generateParenthesis(self, N: int) -> List[str]:
        ans = []

        def backtrack(S = '', left = 0, right = 0):
            if len(S) == 2 * N:
                ans.append(S)
                return
            if left < N:
                backtrack(S+'(', left+1, right)
            if right < left:
                backtrack(S+')', left, right+1)

        backtrack()
        return ans


def test():
    s = Solution()
    Case = namedtuple("Case", ["input", "expected"])
    cases = [
        Case(0, [""]),
        Case(1, ["()"]),
        Case(2, ['(())', '()()']),
        Case(3, ['((()))', '()(())', '(())()', '(()())', '()()()']),
        Case(4, ['(((())))', '((()()))', '((())())', '((()))()', '(()(()))', '(()()())', '(()())()', '(())(())', '(())()()', '()((()))', '()(()())', '()(())()', '()()(())', '()()()()']),
    ]

    for c in cases:
        actual = s.generateParenthesis(c.input)
        assert list(sorted(actual)) == list(sorted(c.expected)), "Case: {}".format(c)
