"""Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2

Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an
empty string. This is consistent to C's strstr() and Java's indexOf().

"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """Used std-library str.index() function."""
        if not needle:
            return 0
        if needle in haystack:
            return haystack.index(needle)
        return -1

    def strStr2(self, haystack: str, needle: str) -> int:
        """Naive solution with O(nm) time complexity. Was not accepted in
leetcode for long inputs. Better solution is Knuth-Morris-Pratt (KMP)
with O(n). But do not think this is really expected for an 'easy'
task.
        """
        if not needle:
            return 0
        if len(needle) > len(haystack):
            return -1
        for i in range(len(haystack) - len(needle)):
            for j in range(len(needle)):
                if haystack[i+j] == needle[j]:
                    if j == len(needle) - 1:
                        return i
                else:
                    break
        return -1


def test():
    haystack = "hello"
    needle = "ll"

    sol = Solution()
    result = sol.strStr(haystack, needle)
    assert result == 2

    haystack = "aaaaa"
    needle = "bba"
    result = sol.strStr(haystack, needle)
    assert result == -1

    haystack = "aaaaa"
    needle = ""
    result = sol.strStr(haystack, needle)
    assert result == 0

    haystack = "mississippi"
    needle = "issipi"
    result = sol.strStr(haystack, needle)
    assert result == -1

    haystack = "mississippi"
    needle = "issip"
    result = sol.strStr(haystack, needle)
    assert result == 4
