"""Given a 2d grid map of '1's (land) and '0's (water), count the
number of islands. An island is surrounded by water and is formed by
connecting adjacent lands horizontally or vertically. You may assume
all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1

Example 2:

Input:
11000
11000
00100
00011

Output: 3

"""

from typing import List


def toGrid(string: str):
    lines = string.splitlines()
    return lines


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        ones = self.findOneIndices(grid)
        counter = 0
        for p in ones:
            if p not in visited:
                visited.add(p)
                self.dfs(p, grid, visited)
                counter += 1
        return counter

    def findOneIndices(self, grid):
        ones = set()
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                if val == "1":
                    ones.add((i, j))
        return ones

    def dfs(self, start, grid, visited):
        for succ in self.successors(start, grid):
            if succ not in visited:
                visited.add(succ)
                self.dfs(succ, grid, visited)

    def successors(self, point, grid):
        max_row = len(grid) - 1
        max_col = len(grid[0]) - 1
        row, col = point

        def isValid(tup):
            return (
                True
                if row >= 0
                and row <= max_row
                and col >= 0
                and col <= max_col
                and grid[row][col] == "1"
                else False
            )

        # works too but not so nice!

        # row, col = point
        # max_row = len(grid) - 1
        # max_col = len(grid[0]) - 1
        # succs = []
        # if row + 1 <= max_row and row + 1 >= 0 and grid[row + 1][col] == "1":
        #     succs.append((row + 1, col))
        # if row - 1 <= max_row and row - 1 >= 0 and grid[row - 1][col] == "1":
        #     succs.append((row - 1, col))
        # if col + 1 <= max_col and col + 1 >= 0 and grid[row][col + 1] == "1":
        #     succs.append((row, col + 1))
        # if col - 1 <= max_col and col - 1 >= 0 and grid[row][col - 1] == "1":
        #     succs.append((row, col - 1))

        return [
            x
            for x in [tuple([sum(item) for item in zip(point, d)]) for d in DIRECTIONS]
            if isValid(x)
        ]


UP = (1, 0)
DOWN = (-1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)
DIRECTIONS = [UP, DOWN, LEFT, RIGHT]


def test1():
    grid = """11110
11010
11000
00000
"""
    sol = Solution()
    actual = sol.numIslands(toGrid(grid))
    expected = 1
    assert actual == expected


def test2():
    grid = """11000
11000
00100
00011
"""
    sol = Solution()
    actual = sol.numIslands(toGrid(grid))
    expected = 3
    assert actual == expected
