"""Determine if a 9x9 Sudoku board is valid. Only the filled cells
need to be validated according to the following rules:

1. Each row must contain the digits 1-9 without repetition.

2. Each column must contain the digits 1-9 without repetition.

3. Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9
without repetition.

A partially filled sudoku which is valid.

The Sudoku board could be partially filled, where empty cells are
filled with the character '.'.

"""

from typing import List
from math import sqrt


def checkX(board) -> bool:
    for row in board:
        row2 = [v for v in row if v != "."]
        if len(row2) != len(set(row2)):
            return False
    return True


def checkY(board) -> bool:
    for j in range(len(board[0])):
        column = [board[i][j] for i in range(len(board))]
        column2 = [v for v in column if v != "."]
        if len(column2) != len(set(column2)):
            return False
    return True


def checkBlock(board) -> bool:
    # get block values
    blocksize = int(sqrt(len(board)))
    blocks = []
    tmpblocks = [[] for i in range(blocksize)]
    for i in range(len(board)):
        for j in range(len(board)):
            tmpblocks[j // blocksize].append(board[i][j])
        if i % 3 == 2:
            for b in tmpblocks:
                blocks.append(b)
            tmpblocks = [[] for i in range(blocksize)]
    # check blocks
    for b in blocks:
        b2 = [v for v in b if v != "."]
        if len(set(b2)) != len(b2):
            return False
    return True


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return checkX(board) and checkY(board) and checkBlock(board)


def test():
    input1 = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
              ["6", ".", ".", "1", "9", "5", ".", ".", "."],
              [".", "9", "8", ".", ".", ".", ".", "6", "."],
              ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
              ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
              ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
              [".", "6", ".", ".", ".", ".", "2", "8", "."],
              [".", ".", ".", "4", "1", "9", ".", ".", "5"],
              [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    expected1 = True
    input2 = [["8", "3", ".", ".", "7", ".", ".", ".", "."],
              ["6", ".", ".", "1", "9", "5", ".", ".", "."],
              [".", "9", "8", ".", ".", ".", ".", "6", "."],
              ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
              ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
              ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
              [".", "6", ".", ".", ".", ".", "2", "8", "."],
              [".", ".", ".", "4", "1", "9", ".", ".", "5"],
              [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    expected2 = False
    sol = Solution()

    result1 = sol.isValidSudoku(input1)
    result2 = sol.isValidSudoku(input2)
    assert result1 == expected1
    assert result2 == expected2
