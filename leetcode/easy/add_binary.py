"""Given two binary strings a and b, return their sum as a binary
string.

Example 1:

Input: a = "11", b = "1"
Output: "100"

Example 2:

Input: a = "1010", b = "1011"
Output: "10101"

"""

from collections import namedtuple


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        curry = False
        a, b = a[::-1], b[::-1]
        if len(a) < len(b):
            a, b = b, a
        i = 0
        while i < len(b):
            if a[i] == "0" and b[i] == "0":
                if not curry:
                    result.append("0")
                    curry = False
                else:
                    result.append("1")
                    curry = False
            elif a[i] == "1" and b[i] == "1":
                if not curry:
                    result.append("0")
                    curry = True
                else:
                    result.append("1")
                    curry = True
            else:
                if not curry:
                    result.append("1")
                    curry = False
                else:
                    result.append("0")
                    curry = True
            i += 1

        while i < len(a):
            if not curry:
                result.append(a[i])
                curry = False
            else:
                if a[i] == "0":
                    result.append("1")
                    curry = False
                else:
                    result.append("0")
                    curry = True
            i += 1

        if curry:
            result.append("1")

        return "".join(reversed(result))


Case = namedtuple("Case", ["a", "b", "expected"])


def test():
    cases = [Case("11", "1", "100"), Case("1010", "1011", "10101")]
    sol = Solution()
    for c in cases:
        actual = sol.addBinary(c.a, c.b)
        assert actual == c.expected
