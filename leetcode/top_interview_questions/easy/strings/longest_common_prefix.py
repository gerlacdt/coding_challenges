"""Write a function to find the longest common prefix string amongst
an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"


Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.

"""

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        prefix = []
        shortest = min(strs, key=lambda x: len(x))
        for i in range(len(shortest)):
            if isPrefix(i, strs):
                prefix.append(strs[0][i])
            else:
                break
        return "".join(prefix)


def isPrefix(index, words):
    assert words
    assert index >= 0
    prefix = words[0][index]
    for w in words:
        if w[index] != prefix:
            return False
    return True


def test():
    sol = Solution()
    input1 = ["flower", "flow", "flight"]
    expected = "fl"
    result = sol.longestCommonPrefix(input1)
    assert result == expected

    input1 = ["dog", "racecar", "car"]
    expected = ""
    result = sol.longestCommonPrefix(input1)
    assert result == expected

    input1 = []
    expected = ""
    result = sol.longestCommonPrefix(input1)
    assert result == expected
