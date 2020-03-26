"""Implement an algorithm to print all valid (properly opened and
closed) combinations of n-pairs of parenthesis.


Input: n = 3

Output:
((())), (()()), (())(), ()(()), ()()()


Input: n = 2

Output:
(()), ()()

Input: n = 1

Output:
()
"""

from collections import namedtuple


def npairs(N):
    ans = []

    def backtrack(S="", left=0, right=0):
        if len(S) == 2 * N:
            ans.append(S)
            return
        if left < N:
            backtrack(S+"(", left+1, right)
        if right < left:
            backtrack(S+")", left, right+1)

    backtrack()
    return ans


def test():
    Case = namedtuple("Case", ["input", "expected"])
    cases = [Case(0, [""]),
             Case(1, ["()"]),
             Case(2, ["(())", "()()"]),
             Case(3, ["((()))", "()(())", "(())()", "(()())", "()()()"]),
             Case(4, ['(((())))', '((()()))', '((())())', '((()))()', '(()(()))', '(()()())', '(()())()', '(())(())', '(())()()', '()((()))', '()(()())', '()(())()', '()()(())', '()()()()']),
    ]

    for c in cases:
        actual = npairs(c.input)
        assert list(sorted(actual)) == list(sorted(c.expected)), "Case: {}".format(c)
