# coding: utf-8

"""The n-queens puzzle is the problem of placing n queens on an n×n
chessboard such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.

Example:

Input: 4 Output: 2

Explanation: There are two distinct solutions to the 4-queens puzzle
as shown below.

[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]

"""

from collections import namedtuple


class Solution:
    def totalNQueens(self, n: int) -> int:
        solutions = []
        assignment = []

        def helper():
            nonlocal assignment
            if len(assignment) == n:
                solutions.append(assignment)
                return

            for i in range(n):
                # check if next assignment is valid
                if isValid(assignment, (i, len(assignment))):
                    # do move
                    assignment.append(i)
                    helper()
                    # undo move
                    assignment.pop()

        helper()
        return len(solutions)


def isValid(assignment, point):
    newRow, newCol = point
    for col, row in enumerate(assignment):
        # check horizontal
        if row == newRow:
            return False

        # check diagonal
        if newRow + newCol == row + col:
            return False
        if newRow - newCol == row - col:
            return False

    # skip checking vertical because we extend assingment always by
    # one free column

    # all checks passed
    return True


Case = namedtuple("Case", ["n", "expected"])


def test():
    cases = [
        Case(4, 2),
        Case(5, 10),
        Case(6, 4),
        Case(7, 40),
        Case(8, 92),
        Case(9, 352),
    ]
    sol = Solution()
    for c in cases:
        actual = sol.totalNQueens(c.n)
        assert actual == c.expected
