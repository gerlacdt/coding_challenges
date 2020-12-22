"""You are given coins of different denominations and a total amount
of money. Write a function to compute the number of combinations that
make up that amount. You may assume that you have infinite number of
each kind of coin.



Example 1:

Input: amount = 5, coins = [1, 2, 5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1

Example 2:

Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.

Example 3:

Input: amount = 10, coins = [10]
Output: 1

https://leetcode.com/problems/coin-change-2/

"""

from typing import List, Dict, Tuple
from collections import namedtuple


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        cache: Dict[Tuple[int, Tuple[int]], int] = {}

        def helper(rest, restCoins):

            if rest == 0:
                return 1
            elif rest < 0 or not restCoins:
                return 0
            elif (rest, restCoins) in cache:
                return cache[(rest, restCoins)]
            else:
                result = 0
                result += helper(rest - restCoins[0], restCoins) + helper(
                    rest, restCoins[1:]
                )
                cache[(rest, restCoins)] = result
                return result

        coins.sort(reverse=True)
        return helper(amount, tuple(coins))

    def change2(self, amount: int, coins: List[int]) -> int:
        dp = [0 for _ in range(amount + 1)]
        dp[0] = 1
        for c in coins:
            for i in range(c, amount + 1):
                dp[i] += dp[i - c]
        return dp[-1]


Case = namedtuple("Case", ["amount", "coins", "expected"])


def test():
    sol = Solution()
    cases = [
        Case(0, [], 1),
        Case(5, [5, 2, 1], 4),
        Case(4, [5, 2, 1], 3),
        Case(3, [2], 0),
        Case(10, [10], 1),
        Case(100, [50, 25, 10, 5, 1], 292),
        Case(500, [3, 5, 7, 8, 9, 10, 11], 35502874),
    ]
    for c in cases:
        actual = sol.change(c.amount, c.coins)
        assert actual == c.expected, f"{c.amount} {c.coins}"

        actual2 = sol.change2(c.amount, c.coins)
        assert actual2 == c.expected, f"{c.amount} {c.coins}"
