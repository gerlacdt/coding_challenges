"""

https://www.hackerrank.com/challenges/one-month-preparation-kit-climbing-the-leaderboard/problem

"""

from collections import namedtuple


def climbingLeaderboard(ranked, player):
    pass


Case = namedtuple("Case", ["ranked", "player", "expected"])


def test():
    cases = [
        Case([100, 90, 90, 80], [70, 80, 105], [4, 3, 1]),
        Case([100, 100, 50, 40, 40, 20, 10], [5, 25, 50, 120], [6, 4, 2, 1]),
    ]
    for c in cases:
        actual = climbingLeaderboard(c.ranked, c.player)
        assert actual == c.expected, "Case: {} {}".format(c.ranked, c.player)
