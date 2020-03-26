"""Given a string containing just the characters '(', ')', '{', '}',
'[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:
Input: "()"
Output: true

Example 2:
Input: "()[]{}"
Output: true

Example 3:
Input: "(]"
Output: false

Example 4:
Input: "([)]"
Output: false

Example 5:
Input: "{[]}"
Output: true

"""

from collections import namedtuple


OPENINGS = set(["[", "(", "{"])
CLOSINGS = set (["]", ")", "}"])

PAREN_MAP = {
    "]": "[",
    ")": "(",
    "}": "{",
}


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in OPENINGS:
                stack.append(c)
            elif c in CLOSINGS:
                if not stack:
                    return False
                if PAREN_MAP[c] != stack[-1]:  # match kind of closing parenthesis with opening one
                    return False
                stack.pop()
            else:
                raise RuntimeError("Invalid string: {}, contains unkown char: {} ".format(s, c))
        return True if not stack else False


def test():
    s = Solution()
    Case = namedtuple("Case", ["input", "expected"])
    cases = [Case("()", True), Case("()[]{}", True), Case("(]", False),
             Case("([)]", False), Case("{[]}", True)]
    for c in cases:
        result = s.isValid(c.input)
        assert result == c.expected
