"""Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given a set of points (x, y) on a 2D cartesian plane, find the two
closest points. For example, given the points
[(1, 1), (-1, -1), (3,4), (6, 1), (-1, -6), (-4, -3)], return [(-1, -1), (1, 1)]
"""

# TODO use divide-and-conquer to reduce time complexity

import sys


def cityblock_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def findClosest(points):
    localMin = (sys.maxsize, None)
    n = len(points)
    for i in range(n - 1):
        for j in range(i + 1, n):
            p1, p2 = points[i], points[j]
            distance = cityblock_distance(p1, p2)
            if distance < localMin[0]:
                localMin = (distance, [p1, p2])
    return sorted(localMin[1])


def test():
    points = [(1, 1), (-1, -1), (3, 4), (6, 1), (-1, -6), (-4, -3)]
    actual = findClosest(points)
    expected = sorted([(-1, -1), (1, 1)])
    assert actual == expected
