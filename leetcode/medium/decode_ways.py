"""A message containing letters from A-Z is being encoded to numbers
using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

The answer is guaranteed to fit in a 32-bit integer.

Example 1:

Input: s = "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).


Example 2:

Input: s = "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).


Example 3:

Input: s = "0"
Output: 0

Explanation: There is no character that is mapped to a number starting
with '0'. We cannot ignore a zero when we face it while decoding. So,
each '0' should be part of "10" --> 'J' or "20" --> 'T'.

Example 4:

Input: s = "1"
Output: 1

https://leetcode.com/problems/decode-ways/

"""

from collections import namedtuple


class Solution:
    def numDecodings(self, s: str) -> int:
        if s.startswith("0"):
            return 0
        dp = [0 for _ in range(len(s) + 1)]
        dp[0] = 1
        dp[1] = 1

        for i in range(2, len(s) + 1):
            dp[i] = 0
            if s[i - 1] > "0":
                dp[i] = dp[i - 1]
            if s[i - 2] == "1" or (s[i - 2] == "2" and s[i - 1] < "7"):
                dp[i] += dp[i - 2]

        return dp[len(s)]

    def numDecodingsRec(self, s: str) -> int:
        if s.startswith("0"):
            return 0

        def helper(n):
            if n == 0 or n == 1:
                return 1
            count = 0
            if s[n - 1] > "0":
                count = helper(n - 1)
            if s[n - 2] == "1" or (s[n - 2] == "2" and s[n - 1] < "7"):
                count += helper(n - 2)
            return count

        return helper(len(s))


Case = namedtuple("Case", ["s", "expected"])


def test():
    sol = Solution()
    cases = [
        Case("0", 0),
        Case("01", 0),
        Case("1", 1),
        Case("10", 1),
        Case("12", 2),
        Case("27", 1),
        Case("226", 3),
        Case("1234", 3),
        Case("1111", 5),
        Case("1234", 3),
        Case("2101", 1),
        # Case("111111111111111111111111111111111111111111111", 1836311903),
    ]
    for c in cases:
        actual = sol.numDecodingsRec(c.s)
        assert actual == c.expected, f"input: {c.s}"

        actual2 = sol.numDecodings(c.s)
        assert actual2 == c.expected, f"input: {c.s}"
