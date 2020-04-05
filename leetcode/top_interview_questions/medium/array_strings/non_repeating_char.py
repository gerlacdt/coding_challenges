"""Given a string, find the first non-repeating character in it and
return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.

"""

from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts = Counter(s)

        # find minimum
        for i, c in enumerate(s):
            if counts[c] == 1:
                return i
        return -1


def test():
    input1 = "leetcode"
    input2 = "loveleetcode"
    sol = Solution()

    result1 = sol.firstUniqChar(input1)
    result2 = sol.firstUniqChar(input2)

    expected1 = 0
    expected2 = 2

    assert result1 == expected1
    assert result2 == expected2
