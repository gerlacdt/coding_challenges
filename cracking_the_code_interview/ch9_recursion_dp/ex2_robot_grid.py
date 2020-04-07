# coding: utf-8

"""A robot sits on a grid on (0,0) on a X,Y grid.  How many possible
way can a robot take to get from (0,0) to (X,Y) The robot can go two
directions: DOWN and RIGHT.

Bonus: What about if some spots are blocked and cannot be used?

"""

from typing import List
from collections import namedtuple


# X-axis and Y-axis is like in the real world (NOT like in an array)
DIRECTIONS = UP, DOWN, LEFT, RIGHT = (0, -1), (0, 1), (-1, 0), (1, 0)


def move(pos, direction):
    return tuple(sum(p) for p in zip(pos, direction))


def robotGrid(pos):
    if pos[0] < 0 or pos[1] < 0:
        return 0
    if pos[0] == 0 and pos[1] == 0:
        return 1
    else:
        return robotGrid(move(pos, UP)) + robotGrid(move(pos, LEFT))
    return robotGrid(pos)


# dp solution


def parseGrid(content):
    lines = content.splitlines()
    arr = []
    for i, l in enumerate(lines):
        arr.append([True if int(n) == 0 else False for n in l])
    return arr


def dpRobotGrid(grid):
    nrows = len(grid)
    ncols = len(grid[0])
    table = [[1 if i == 0 or j == 0 else 0 for i in range(ncols)] for j in range(nrows)]

    # dp algorithm
    for row in range(0, nrows):
        for col in range(0, ncols):
            if not grid[row][col]:
                table[row][col] = 0
            elif row > 0 and col > 0:
                table[row][col] = table[row - 1][col] + table[row][col - 1]

            # these cases are needed for blocked fields
            # contiguous fieds of blocked field get resetted to 0
            elif row > 0:
                table[row][col] = table[row - 1][col]
            elif col > 0:
                table[row][col] = table[row][col - 1]

    # return last element in table. It contains the number of all
    # possible ways to (X,Y) from (0,0)
    return table[nrows - 1][ncols - 1]


Case = namedtuple("Case", ["input", "expected"])


def test():
    cases = [
        Case((0, 0), 1),
        Case((1, 1), 2),
        Case((2, 1), 3),
        Case((2, 2), 6),
        Case((2, 3), 10),
    ]
    for c in cases:
        actual = robotGrid(c.input)
        assert actual == c.expected


def testDp():
    grid11 = "0"
    grid22 = """00
00"""
    grid32 = """00
00
00"""
    grid33 = """000
000
000"""
    grid34 = """0000
0000
0000"""
    cases = [
        Case(parseGrid(grid11), 1),
        Case(parseGrid(grid22), 2),
        Case(parseGrid(grid32), 3),
        Case(parseGrid(grid33), 6),
        Case(parseGrid(grid34), 10),
    ]
    for c in cases:
        actual = dpRobotGrid(c.input)
        assert actual == c.expected, "case: {}".format(c)


def testWithBlocking():

    test1 = """0000
0000
0000
0000"""

    test2 = """0000
0100
0010
0000"""

    test3 = """000
010
010
000"""

    test4 = """010
000
010
000"""

    test5 = """010
010
010
"""

    grid = parseGrid(test1)
    actual = dpRobotGrid(grid)
    assert actual == 20

    grid = parseGrid(test2)
    actual = dpRobotGrid(grid)
    assert actual == 4

    grid = parseGrid(test3)
    actual = dpRobotGrid(grid)
    assert actual == 2

    grid = parseGrid(test4)
    actual = dpRobotGrid(grid)
    assert actual == 2

    grid = parseGrid(test5)
    actual = dpRobotGrid(grid)
    assert actual == 0
