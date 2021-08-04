""""

https://www.hackerrank.com/challenges/one-month-preparation-kit-sparse-arrays/problem

"""

from collections import namedtuple


def matchingStrings(strings, queries):
    hits = []

    for q in queries:
        total = 0
        for s in strings:
            if s == q:
                total += 1
        hits.append(total)

    return hits


Case = namedtuple("Case", ["strings", "queries", "expected"])


def test():
    cases = [
        Case(["ab", "ab", "abc"], ["ab", "abc", "bc"], [2, 1, 0]),
        Case(["aba", "baba", "aba", "xzxb"], ["aba", "xzxb", "ab"], [2, 1, 0]),
    ]
    for c in cases:
        actual = matchingStrings(c.strings, c.queries)
        assert actual == c.expected
