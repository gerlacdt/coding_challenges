"""Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

You are given an M by N matrix consisting of booleans that represents
a board. Each True boolean represents a wall. Each False boolean
represents a tile you can walk on.

Given this matrix, a start coordinate, and an end coordinate, return
the minimum number of steps required to reach the end coordinate from
the start. If there is no possible path, then return null. You can
move up, left, down, and right. You cannot move through walls. You
cannot wrap around the edges of the board.

For example, given the following board:

[[f, f, f, f],
[t, t, f, t],
[f, f, f, f],
[f, f, f, f]]

and start = (3, 0) (bottom left) and end = (0, 0) (top left), the
minimum number of steps required to reach the end is 7, since we would
need to go through (1, 2) because there is a wall everywhere else on
the second row.
"""

from collections import deque

UP, DOWN, LEFT, RIGHT = (1, 0), (-1, 0), (0, -1), (0, 1)


def move(point, direction):
    """Returns a new point which is based on the given point moved to the given direction"""
    return tuple([sum(p) for p in zip(point, direction)])


input1 = [[False, False, False, False],
          [True, True, False, True],
          [False, False, False, False],
          [False, False, False, False]]


def successorFn(matrix, point):
    directions = (UP, DOWN, LEFT, RIGHT)
    m = len(matrix)
    n = len(matrix[0])

    positions = [move(point, d) for d in directions]

    def valid(point):
        y, x = point
        if y < 0 or y >= m:
            return False
        if x < 0 or x >= n or matrix[y][x]:
            return False
        if matrix[y][x]:
            return False
        return True

    return filter(valid, positions)


def bfs(matrix=input1, start=(3, 0), goal=(0, 0)):
    visited = set()
    frontier = deque([start])
    costs = {}
    costs[start] = 0
    while frontier:
        p = frontier.pop()
        if p == goal:
            return p, costs[p]
        succs = successorFn(matrix, p)
        for s in succs:
            if s not in frontier and s not in visited:
                frontier.appendleft(s)
                costs[s] = costs[p] + 1
        visited.add(p)
    return None


def test():
    result = bfs(input1, (3, 0), goal=(0, 0))
    expected = ((0, 0), 7)
    assert result == expected
