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
        currentLen = 0
        maxLen = 0
        charIndices = {}
        for i, c in enumerate(s):
            if c not in charIndices.keys():
                currentLen += 1
                charIndices[c] = i
                if maxLen < currentLen:
                    maxLen = currentLen
            else:
                oldIndex = charIndices[c]
                currentLen = i - oldIndex
                # adjust charIndices
                charIndices[c] = i
                toRemoveChars = []
                for key, val in charIndices.items():
                    if val < oldIndex:
                        toRemoveChars.append(key)
                for val in toRemoveChars:
                    charIndices.pop(val)

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
