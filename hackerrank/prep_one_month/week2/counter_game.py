"""

https://www.hackerrank.com/challenges/one-month-preparation-kit-counter-game/problem

"""

import math
from collections import namedtuple


def isPowerOfTwo(n):
    log2 = math.log2(n)
    return math.ceil(log2) == math.floor(log2)


def togglePlayer(player):
    return "Richard" if player == "Louise" else "Louise"


def counterGame(n):
    if n == 1:
        return "Richard"
    result = n
    currentPlayer = "Louise"
    while True:
        if isPowerOfTwo(result):
            result /= 2
        else:
            result -= 2 ** math.floor(math.log2(result))
        if result == 1:
            return currentPlayer
        currentPlayer = togglePlayer(currentPlayer)
    return None


Case = namedtuple("Case", ["n", "expected"])


def test():
    cases = [Case(132, "Louise"), Case(1, "Richard")]
    for c in cases:
        actual = counterGame(c.n)
        assert actual == c.expected, "Case: {}".format(c.n)
