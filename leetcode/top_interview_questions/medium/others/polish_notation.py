"""Evaluate the value of an arithmetic expression in Reverse Polish
Notation.

Valid operators are +, -, *, /. Each operand may be an integer or
another expression.

Note:

Division between two integers should truncate toward zero.  The given
RPN expression is always valid. That means the expression would always
evaluate to a result and there won't be any divide by zero operation.

Example 1:

Input: ["2", "1", "+", "3", "*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
Example 2:

Input: ["4", "13", "5", "/", "+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
Example 3:

Input: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
Output: 22
Explanation:
  ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22

"""

from collections import namedtuple
from typing import List
import operator


def mydiv(a, b):
    if a // b < 0 and a % b != 0:
        return (a // b) + 1
    return a // b


OPTABLE = {
    "/": mydiv,
    "*": operator.mul,
    "+": operator.add,
    "-": operator.sub,
}


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        result: List[int] = []
        for elem in tokens:
            if elem in "+-*/":
                a, b = result.pop(), result.pop()
                result.append(OPTABLE[elem](b, a))
                continue
            result.append(int(elem))  # for internal result use integers
        return result[0]


Case = namedtuple("Case", ["tokens", "expected"])


def testEval():
    sol = Solution()
    cases = [
        Case(["2", "1", "+", "3", "*"], 9),
        Case(["4", "13", "5", "/", "+"], 6),
        Case(["4", "2", "/"], 2),
        Case(["4", "2", "*"], 8),
        Case(["4", "1", "-"], 3),
        Case(["-2", "-3", "+"], -5),
        Case(["-2", "-3", "*"], 6),
        Case(
            ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"], 22,
        ),
    ]
    for c in cases:
        actual = sol.evalRPN(c.tokens)
        assert actual == c.expected, "Case: {}".format(c)
