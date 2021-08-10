"""

https://www.hackerrank.com/challenges/one-month-preparation-kit-grid-challenge/problem

"""

from collections import namedtuple


def gridChallenge(grid):
    for i, row in enumerate(grid):
        grid[i] = "".join(sorted(row))

    # check if columns are sorted ascending
    for col in range(len(grid[0])):
        arr = []
        for row in range(len(grid)):
            arr.append(grid[row][col])
        if arr != sorted(arr):
            return "NO"
    return "YES"


Case = namedtuple("Case", ["grid", "expected"])


def test():
    cases = [
        Case(["ebacd", "fghij", "olmkn", "trpqs", "xywuv"], "YES"),
        Case(["xyz", "abc"], "NO"),
    ]

    for c in cases:
        actual = gridChallenge(c.grid)
        assert actual == c.expected
