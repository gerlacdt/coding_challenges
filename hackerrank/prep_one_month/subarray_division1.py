"""

https://www.hackerrank.com/challenges/one-month-preparation-kit-the-birthday-bar/problem

"""

from collections import namedtuple


def birthday(s, d, m):
    birthdays = []
    for i in range(len(s)):
        tmpTotals = [s[i]]
        if m == 1 and s[i] == d:
            birthdays.append([s[i]])
        for j in range(i + 1, len(s)):
            tmpTotals.append(s[j])
            if sum(tmpTotals) > d:
                break
            elif len(tmpTotals) == m and sum(tmpTotals) == d:
                birthdays.append(tmpTotals)
                break

    return len(birthdays)


Case = namedtuple("Case", ["s", "d", "m", "expected"])


def test():
    cases = [Case([2, 2, 1, 3, 2], 4, 2, 2)]
    for c in cases:
        actual = birthday(c.s, c.d, c.m)
        assert actual == c.expected
