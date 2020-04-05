"""Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]

Explanation: Intervals [1,4] and [4,5] are considered overlapping.

"""

from typing import List
from collections import namedtuple


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        if len(intervals) == 1:
            return intervals
        sortedIntervals = sorted(intervals)
        results = [sortedIntervals[0]]

        for i in range(1, len(sortedIntervals)):
            interval = sortedIntervals[i]
            if self.doOverlap(interval, results[-1]):
                low1, high1 = results[-1]
                low2, high2 = interval
                results[-1] = [min(low1, low2), max(high1, high2)]
            else:
                results.append(interval)

        return results

    def doOverlap(self, interval1, interval2):
        low1, high1 = interval1
        low2, high2 = interval2

        # check containing
        if (low1 < low2 and high1 > high2) or (low2 < low2 and high2 > high1):
            return True

        # check overlapping
        if (low1 >= low2 and low1 <= high2) or (high1 >= low2 and high1 <= high2):
            return True
        return False

    def merge2(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        merged = []
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                # no overlap
                merged.append(interval)
            else:
                # overlap exist, merge 2 intervals
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged


def test1():
    sol = Solution()
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    actual = sol.merge(intervals)
    actual2 = sol.merge2(intervals)
    expected = [[1, 6], [8, 10], [15, 18]]
    assert actual == expected
    assert actual2 == expected


def test2():
    sol = Solution()
    intervals = [[1, 4], [4, 5]]
    actual = sol.merge(intervals)
    actual2 = sol.merge2(intervals)
    expected = [[1, 5]]
    assert actual == expected
    assert actual2 == expected


Case = namedtuple("Case", ["input", "expected"])


def testOverlapping():
    sol = Solution()
    cases = [
        Case([[1, 3], [2, 5]], True),
        Case([[0, 10], [4, 7]], True),
        Case([[1, 4], [5, 7]], False),
    ]

    for c in cases:
        int1, int2 = c.input
        actual = sol.doOverlap(int1, int2)
        assert actual == c.expected
