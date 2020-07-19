"""A city's skyline is the outer contour of the silhouette formed by
all the buildings in that city when viewed from a distance. Now
suppose you are given the locations and height of all the buildings as
shown on a cityscape photo (Figure A), write a program to output the
skyline formed by these buildings collectively (Figure B).

Buildings Skyline Contour

The geometric information of each building is represented by a triplet
of integers [Li, Ri, Hi], where Li and Ri are the x coordinates of the
left and right edge of the ith building, respectively, and Hi is its
height. It is guaranteed that 0 <= Li, Ri <= INT_MAX, 0 < Hi <= INT_MAX,
and Ri - Li > 0. You may assume all buildings are perfect rectangles
grounded on an absolutely flat surface at height 0.

For instance, the dimensions of all buildings in Figure A are recorded
as: [ [2 9 10], [3 7 15], [5 12 12], [15 20 10], [19 24 8] ] .

The output is a list of "key points" (red dots in Figure B) in the
format of [ [x1,y1], [x2, y2], [x3, y3], ... ] that uniquely defines a
skyline. A key point is the left endpoint of a horizontal line
segment. Note that the last key point, where the rightmost building
ends, is merely used to mark the termination of the skyline, and
always has zero height. Also, the ground in between any two adjacent
buildings should be considered part of the skyline contour.

For instance, the skyline in Figure B should be represented as:[ [2
10], [3 15], [7 12], [12 0], [15 10], [20 8], [24, 0] ].

Notes:

The number of buildings in any input list is guaranteed to be in the range [0, 10000].
The input list is already sorted in ascending order by the left x position Li.
The output list must be sorted by the x position.
There must be no consecutive horizontal lines of equal height in the output skyline. For instance, [...[2 3], [4 5], [7 5], [11 5], [12 7]...] is not acceptable; the three
lines of height 5 should be merged into one in the final output as such: [...[2 3], [4 5], [12 7], ...]


https://leetcode.com/explore/learn/card/recursion-ii/507/beyond-recursion/3006

"""

from collections import namedtuple
from typing import List
from heapq import heappush, heapify


Event = namedtuple("Event", ["index", "height", "kind"])

START = "START_EVENT"
END = "END_EVENT"


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        result: List[List[int]] = []
        events = []
        for start, end, height in buildings:
            events.append(Event(start, height, START))
            events.append(Event(end, height, END))
        events.sort()

        heap: List = []
        currentHeight = 0
        for i, e in enumerate(events):
            index, height, kind = e
            if kind == START:
                heappush(heap, -height)
            elif kind == END:
                heap.remove(-height)
                heapify(heap)
            else:
                raise RuntimeError("Event Kind {} does not exist".format(kind))

            if len(events) > i + 1 and events[i + 1].index == index:
                # events are sorted by (index, height), so last event with the same index is the highest

                # if the next event is at the same index, don't calculate result yet
                continue
            else:
                possibleNewHeight = -heap[0] if heap else 0
                if currentHeight != possibleNewHeight:
                    currentHeight = possibleNewHeight
                    result.append([index, possibleNewHeight])

        return result

    def getSkyline2(self, buildings: List[List[int]]) -> List[List[int]]:
        """Divide-and-Conquer approach"""
        if not buildings:
            return []

        def helper(left, right):
            if left == right:
                l, r, height = buildings[left]
                return [[l, height], [r, 0]]
            mid = (left + right) // 2
            r1 = helper(left, mid)
            r2 = helper(mid + 1, right)
            return self._merge(r1, r2)

        return helper(0, len(buildings) - 1)

    def _merge(self, strip1, strip2):
        """Strip entries are 2-tuples (x-axis beginning value, height)"""
        height1 = height2 = 0
        i = j = 0
        result = []
        skyline = 0
        while i < len(strip1) and j < len(strip2):
            leftX, leftHeight = strip1[i]
            rightX, rightHeight = strip2[j]
            if leftX < rightX:
                height1 = leftHeight
                i += 1
                if skyline != max(height1, height2):
                    skyline = max(height1, height2)
                    result.append([leftX, skyline])

            elif leftX > rightX:
                height2 = rightHeight
                j += 1
                if skyline != max(height1, height2):
                    skyline = max(height1, height2)
                    result.append([rightX, skyline])
            else:
                height1 = leftHeight
                height2 = rightHeight
                i += 1
                j += 1
                if skyline != max(height1, height2):
                    skyline = max(height1, height2)
                    result.append([leftX, skyline])

        for k in range(i, len(strip1)):
            result.append(strip1[k])

        for k in range(j, len(strip2)):
            result.append(strip2[k])

        return result


Case = namedtuple("Case", ["buildings", "expected"])


def testSkyline():
    cases = [
        Case(
            [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]],
            [[2, 10], [3, 15], [7, 12], [12, 0], [15, 10], [20, 8], [24, 0]],
        ),
        Case([], []),
        Case([[0, 2, 3], [2, 5, 3]], [[0, 3], [5, 0]]),
        Case([[2, 9, 10], [9, 12, 15]], [[2, 10], [9, 15], [12, 0]]),
        Case([[1, 2, 1], [1, 2, 2], [1, 2, 3]], [[1, 3], [2, 0]]),
    ]
    sol = Solution()
    for c in cases:
        actual = sol.getSkyline(c.buildings)
        actual2 = sol.getSkyline2(c.buildings)
        assert actual == c.expected, "Case: {}".format(c.buildings)
        assert actual2 == c.expected, "Case: {}".format(c.buildings)


def testMerge():
    sol = Solution()
    strip1 = [[1, 11], [3, 13], [9, 0], [12, 7], [16, 0]]
    strip2 = [[14, 3], [19, 18], [22, 3], [23, 13], [29, 0]]
    actual = sol._merge(strip1, strip2)
    expected = [
        [1, 11],
        [3, 13],
        [9, 0],
        [12, 7],
        [16, 3],
        [19, 18],
        [22, 3],
        [23, 13],
        [29, 0],
    ]
    assert actual == expected
