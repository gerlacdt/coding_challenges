"""


"""

from collections import namedtuple, Counter


def anagram(s):
    if len(s) % 2:
        return -1
    mid = len(s) // 2
    a = Counter(s[:mid])
    b = Counter(s[mid:])
    return mid - sum((a & b).values())


Case = namedtuple("Case", ["s", "expected"])


def test():
    cases = [Case("abccde", 2), Case("abc", -1), Case("xaxbbbxx", 1)]

    for c in cases:
        actual = anagram(c.s)
        assert actual == c.expected, "{}".format(c.s)
