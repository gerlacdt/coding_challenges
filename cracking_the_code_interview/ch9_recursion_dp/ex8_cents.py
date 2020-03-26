"""Given an infinite number of quarters (25 cents), dimes (10 cents),
nickels (5 cents) and pennies (1 cent), wirte code to calculate the
number of ways representing n cents.

"""

from collections import namedtuple


def makeChange(amount):
    "This solution is from SICP chapter 1"
    COINS = [1, 5, 10, 25]

    def helper(amount, kindOfCoin):
        if amount == 0:
            return 1
        elif amount < 0 or kindOfCoin < 0:
            return 0
        else:
            return helper(amount, kindOfCoin-1) + helper(amount-COINS[kindOfCoin], kindOfCoin)

    return helper(amount, 3)


def makeChange2(n):

    def helper(amount, denoms, index):
        if index >= len(denoms) - 1:
            return 1
        denomAmount = denoms[index]
        ways = 0
        limit = amount // denomAmount
        for i in range(limit+1):
            amountRemaining = amount - i*denomAmount
            ways += helper(amountRemaining, denoms, index+1)
        return ways

    denoms = [25, 10, 5, 1]
    return helper(n, denoms, 0)


def test():

    Case = namedtuple("Case", ["input", "expected"])
    cases = [
        Case(4, 1),
        Case(5, 2),
        Case(10, 4),
        Case(50, 49),
        Case(100, 242),
    ]
    for c in cases:
        actual = makeChange(c.input)
        actual2 = makeChange2(c.input)
        assert actual == c.expected, "Case: {}".format(c)
        assert actual2 == c.expected, "Case: {}".format(c)
