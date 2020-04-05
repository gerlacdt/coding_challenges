"""Given a string, find the length of the longest substring without
repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:


Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:


Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        charIndices = {}
        startIndex = 0
        for i, c in enumerate(s):
            if c in charIndices.keys():
                # jump to the start index for the next unique word
                startIndex = max(charIndices[c] + 1, startIndex)
            maxLen = max(maxLen, i - startIndex + 1)
            charIndices[c] = i
        return maxLen


def test():
    sol = Solution()
    word = "abcabcbb"
    actual = sol.lengthOfLongestSubstring(word)
    expected = 3
    assert actual == expected

    word = "bbbbb"
    actual = sol.lengthOfLongestSubstring(word)
    expected = 1
    assert actual == expected

    word = "pwwkew"
    actual = sol.lengthOfLongestSubstring(word)
    expected = 3
    assert actual == expected

    word = "tmmzuxt"
    actual = sol.lengthOfLongestSubstring(word)
    expected = 5
    assert actual == expected
