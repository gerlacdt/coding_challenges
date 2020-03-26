"""Given a string, determine if it is a palindrome, considering only
alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid
palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true

Example 2:

Input: "race a car"
Output: false

"""

from collections import namedtuple


class Solution:
    def isPalindrome(self, s: str) -> bool:
        letters = "abcdefghijklmnopqrstuvwxyz"
        letters += str.upper(letters)
        letters += "0123456789"

        s2 = "".join([str.lower(c) for c in s if c in letters])
        i = 0
        j = len(s2) - 1
        while i < j:
            if s2[i] != s2[j]:
                return False
            else:
                i += 1
                j -= 1
        return True


def test():
    sol = Solution()
    Case = namedtuple('Case', ['input1', 'expected'])
    cases = [Case(("A man, a plan, a canal: Panama"), True),
             Case(("race a car"), False),
             Case(("abba"), True),
             Case(("aba"), True),
             Case(("0P"), False)]

    for c in cases:
        result = sol.isPalindrome(c.input1)
        assert result == c.expected
