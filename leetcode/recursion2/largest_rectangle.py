"""Given n non-negative integers representing the histogram's bar
height where the width of each bar is 1, find the area of largest
rectangle in the histogram.


Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].


The largest rectangle is shown in the shaded area, which has area = 10
unit.


Example:

Input: [2,1,5,6,2,3]
Output: 10

"""

from collections import namedtuple
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        globalMax = 0
        stack: List[int] = []
        i = 0
        while i < len(heights):
            # print("stack: {}, max: {}, i: {}".format(stack, globalMax, i))
            if not stack or heights[stack[-1]] < heights[i]:
                stack.append(i)
                i += 1
            else:
                currentMax = stack.pop()
                area = heights[currentMax] * ((i - stack[-1] - 1) if stack else i)
                globalMax = max(globalMax, area)

        # print("stack: {}, max: {}, i: {}".format(stack, globalMax, i))
        while stack:
            currentMax = stack.pop()
            area = heights[currentMax] * ((i - stack[-1] - 1) if stack else i)
            globalMax = max(globalMax, area)

        return globalMax

    def largestRectangleArea2(self, heights: List[int]) -> int:
        """Time Complexity O(n^2)"""
        if not heights:
            return 0
        table = heights[:]
        for i in range(len(heights)):
            localmax = heights[i]
            localVals = [heights[i]]
            for j in range(i + 1, len(heights)):
                localVals.append(heights[j])
                localmax = max(localmax, min(localVals) * len(localVals))
            table[i] = localmax
        return max(table)


Case = namedtuple("Case", ["heights", "expected"])


def test():
    cases = [
        Case([2, 1, 5, 6, 2, 3], 10),
        Case([0, 0], 0),
        Case([1], 1),
        Case([1, 1, 1, 1], 4),
        Case([5, 4, 1, 2], 8),
    ]
    sol = Solution()
    for c in cases:
        actual = sol.largestRectangleArea(c.heights)
        actual2 = sol.largestRectangleArea2(c.heights)
        assert actual == c.expected, "Case: {}".format(c.heights)
        assert actual2 == c.expected, "Case: {}".format(c.heights)
