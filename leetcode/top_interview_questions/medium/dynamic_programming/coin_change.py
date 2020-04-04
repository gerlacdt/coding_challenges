"""You are given coins of different denominations and a total amount
of money amount. Write a function to compute the fewest number of
coins that you need to make up that amount. If that amount of money
cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1


Example 2:

Input: coins = [2], amount = 3
Output: -1

Note:
You may assume that you have an infinite number of each kind of coin.

"""

from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        table = [-1] * (amount + 1)
        table[0] = 0
        for i in range(amount + 1):
            validCoins = [
                table[i - c] for c in coins if (i - c >= 0 and table[i - c] >= 0)
            ]
            if validCoins:
                table[i] = min(validCoins) + 1
        return table[-1]


def test1():
    sol = Solution()
    coins = [2, 5]
    amount = 16
    actual = sol.coinChange(coins, amount)
    expected = 5
    assert actual == expected


def test2():
    sol = Solution()
    coins = [2, 5]
    amount = 10
    actual = sol.coinChange(coins, amount)
    expected = 2
    assert actual == expected


def test3():
    sol = Solution()
    coins = [1, 2, 5]
    amount = 11
    actual = sol.coinChange(coins, amount)
    expected = 3
    assert actual == expected


def test4():
    sol = Solution()
    coins = [2]
    amount = 3
    actual = sol.coinChange(coins, amount)
    expected = -1
    assert actual == expected


def test5():
    sol = Solution()
    coins = [1, 2, 5]
    amount = 100
    actual = sol.coinChange(coins, amount)
    expected = 20
    assert actual == expected
