"""Find index to remove to make the given string a palindrome. Return
index, in case the string is already a palindrome return -1.

"""

from collections import namedtuple


def palindromeIndex(s):
    if s == s[::-1]:
        return -1
    n = len(s)
    for i in range(n // 2):
        if s[i] != s[n - 1 - i]:
            if s[i : n - 1 - i] == s[i : n - 1 - i][::-1]:
                return n - 1 - i
            elif s[i + 1 : n - i] == s[i + 1 : n - i][::-1]:
                return i
    raise RuntimeError("invalid input")


Case = namedtuple("Case", ["s", "expected"])


def test():
    cases = [Case("aaab", 3), Case("baa", 0), Case("aaa", -1)]

    for c in cases:
        actual = palindromeIndex(c.s)
        assert actual == c.expected, "{}".format(c.s)
