"""

https://www.hackerrank.com/challenges/one-month-preparation-kit-pangrams/problem

"""


from collections import namedtuple


def pangrams(s):
    letters = set("abcdefghijklmnopqrstuvwxyz")
    table = set()

    for c in s:
        c = str.lower(c)
        if c in letters:
            table.add(c)

    return "pangram" if len(table) == len(letters) else "not pangram"


Case = namedtuple("Case", ["s", "expected"])


def test():
    cases = [
        Case("The quick brown fox jumps over the lazy dog", "pangram"),
        Case("abcdefhi", "not pangram"),
    ]

    for c in cases:
        actual = pangrams(c.s)
        assert actual == c.expected
