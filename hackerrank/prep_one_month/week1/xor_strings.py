"""

https://www.hackerrank.com/challenges/one-month-preparation-kit-strings-xor/problem

"""


def strings_xor(s, t):
    res = ""
    for i in range(len(s)):
        if s[i] == t[i]:
            res += "0"
        else:
            res += "1"

    return res


def test():
    actual = strings_xor("0000", "1111")
    expected = "1111"
    assert actual == expected
