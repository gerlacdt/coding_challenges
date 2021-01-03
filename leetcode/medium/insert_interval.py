"""Given a set of non-overlapping intervals, insert a new interval
into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to
their start times.

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

Example 3:

Input: intervals = [], newInterval = [5,7]
Output: [[5,7]]

Example 4:

Input: intervals = [[1,5]], newInterval = [2,3]
Output: [[1,5]]

Example 5:

Input: intervals = [[1,5]], newInterval = [2,7]
Output: [[1,7]]


https://leetcode.com/problems/insert-interval/

"""

from collections import namedtuple
from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        result = [intervals[0]]
        merged = False

        for i in range(1, len(intervals)):
            if self._overlap(result[-1], newInterval) and not merged:
                result[-1] = self._merge(result[-1], newInterval)
                merged = True
            if self._overlap(result[-1], intervals[i]):
                result[-1] = self._merge(result[-1], intervals[i])
            else:
                result.append(intervals[i])

        if self._overlap(result[-1], newInterval) and not merged:
            result[-1] = self._merge(result[-1], newInterval)
            merged = True
        if not merged:
            # place newInterval in correct order
            index = len(result)
            for i, interval in enumerate(result):
                if newInterval[0] < interval[0]:
                    index = i
                    break
            result = result[:index] + [newInterval] + result[index:]

        return result

    def _overlap(self, a, b):
        if a[0] > b[0]:
            a, b = b, a
        if a[1] < b[0]:
            return False
        return True

    def _merge(self, a, b):
        if a[0] > b[0]:
            a, b = b, a
        return [a[0], b[1] if b[1] >= a[1] else a[1]]


Case = namedtuple("Case", ["intervals", "newInterval", "expected"])


def test():
    sol = Solution()
    cases = [
        Case([[1, 3], [6, 9]], [2, 5], [[1, 5], [6, 9]]),
        Case(
            [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]],
            [4, 8],
            [[1, 2], [3, 10], [12, 16]],
        ),
        Case([], [5, 7], [[5, 7]]),
        Case([[1, 5]], [2, 3], [[1, 5]]),
        Case([[1, 5]], [2, 7], [[1, 7]]),
        Case([[1, 5]], [6, 8], [[1, 5], [6, 8]]),
        Case([[1, 5]], [0, 0], [[0, 0], [1, 5]]),
        Case([[3, 5], [12, 15]], [6, 6], [[3, 5], [6, 6], [12, 15]]),
    ]
    for c in cases:
        actual = sol.insert(c.intervals, c.newInterval)
        assert actual == c.expected, f"{c.intervals} {c.newInterval}"
