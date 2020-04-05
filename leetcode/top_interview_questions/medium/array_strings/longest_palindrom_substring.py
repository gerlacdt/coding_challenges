"""Given a string s, find the longest palindromic substring in s. You
may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:

Input: "cbbd"
Output: "bb"

"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        max_index = len(s) - 1
        result = s[0]
        for i in range(1, len(s)):
            # check odd palindrome, start from i and expand
            low = high = i
            while low >= 0 and high <= max_index and s[low] == s[high]:
                result = (
                    s[low : high + 1]
                    if len(result) < len(s[low : high + 1])
                    else result
                )
                low -= 1
                high += 1

            # check even palindrome, start from i and i - 1 and expand
            low = i - 1
            high = i
            while low >= 0 and high <= max_index and s[low] == s[high]:
                result = (
                    s[low : high + 1]
                    if len(result) < len(s[low : high + 1])
                    else result
                )
                low -= 1
                high += 1

        return result


def test():
    sol = Solution()
    word = "babad"
    actual = sol.longestPalindrome(word)
    expected = set(["bab", "aba"])
    assert actual in expected

    word = "accbaabccb"
    actual = sol.longestPalindrome(word)
    expected = "ccbaabcc"
    assert actual == expected

    word = "a"
    actual = sol.longestPalindrome(word)
    expected = "a"
    assert actual == expected

    word = "ac"
    actual = sol.longestPalindrome(word)
    expected = "a"
    assert actual == expected

    word = "bb"
    actual = sol.longestPalindrome(word)
    expected = "bb"
    assert actual == expected
