"""Say you have an array for which the ith element is the price of a
given stock on day i.

If you were only permitted to complete at most one transaction (i.e.,
buy one and sell one share of the stock), design an algorithm to find
the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

"""

from typing import List
import sys


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """Find the lowest valley and the largest peak. Then you have the
maxprofit.
        """
        minPrice = sys.maxsize
        maxProfit = 0
        for i in range(len(prices)):
            if prices[i] < minPrice:
                minPrice = prices[i]
            if maxProfit < prices[i] - minPrice:
                maxProfit = prices[i] - minPrice
        return maxProfit


def test():
    s = Solution()
    result = s.maxProfit([7, 1, 5, 3, 6, 4])
    expected = 5
    assert result == expected

    result = s.maxProfit([7, 6, 4, 3, 1])
    expected = 0
    assert result == expected

    result = s.maxProfit([])
    expected = 0
    assert result == expected
