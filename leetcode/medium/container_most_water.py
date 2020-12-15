"""Given n non-negative integers a1, a2, ..., an , where each
represents a point at coordinate (i, ai). n vertical lines are drawn
such that the two endpoints of the line i is at (i, ai) and (i,
0). Find two lines, which, together with the x-axis forms a container,
such that the container contains the most water.

Notice that you may not slant the container.

Example 1:

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49

Explanation: The above vertical lines are represented by array
[1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue
section) the container can contain is 49.

Example 2:

Input: height = [1,1]
Output: 1

Example 3:

Input: height = [4,3,2,1,4]
Output: 16

Example 4:

Input: height = [1,2,1]
Output: 2


https://leetcode.com/problems/container-with-most-water/

"""

from collections import namedtuple
from typing import List


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxHeight = 0
        l = 0
        r = len(heights) - 1
        while l < r:
            currentHeight = min(heights[l], heights[r]) * (r - l)
            maxHeight = max(maxHeight, currentHeight)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return maxHeight

    def maxArea2(self, heights: List[int]) -> int:
        maxTotal = 0
        for i, current in enumerate(heights):
            maxTmp = 0
            for j in range(i + 1, len(heights)):
                containerHeight = min(current, heights[j])
                maxTmp = max(maxTmp, containerHeight * (j - i))
            maxTotal = max(maxTotal, maxTmp)
        return maxTotal


Case = namedtuple("Case", ["height", "expected"])


def test():
    sol = Solution()
    cases = [
        Case([1, 1], 1),
        Case([4, 3, 2, 1, 4], 16),
        Case([1, 2, 1], 2),
        Case([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
    ]

    for c in cases:
        actual = sol.maxArea(c.height)
        actual2 = sol.maxArea(c.height)
        assert actual == c.expected
        assert actual2 == c.expected
