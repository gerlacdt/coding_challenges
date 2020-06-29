"""Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.

Each of the digits 1-9 must occur exactly once in each column.

Each of the the digits 1-9 must occur exactly once in each of the 9
3x3 sub-boxes of the grid.

Empty cells are indicated by the character '.'.

The given board contain only digits 1-9 and the character '.'.

You may assume that the given Sudoku puzzle will have a single unique solution.

The given board size is always 9x9.

"""

from typing import List
from heapq import heappush, heappop


def makeBlockLookup():
    blocks = []
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            b = []
            for i2 in range(i, i + 3):
                for j2 in range(j, j + 3):
                    b.append((i2, j2))
            blocks.append(b)

    table = {}
    for block in blocks:
        for cell in block:
            table[cell] = set(block)
    return table


BLOCK_TABLE = makeBlockLookup()


def isValid(assignment, cell, val):
    row, col = cell
    # check horizontal
    if val in assignment[row]:
        return False
    # check vertical
    for i in range(len(assignment)):
        if val == assignment[i][col]:
            return False

    # check block
    for cell in BLOCK_TABLE[cell]:
        i, j = cell
        if val == assignment[i][j]:
            return False
    return True


def isSolution(assignment):
    return all([all(row) for row in assignment])


def nextFreeCell(assignment):
    """Naive selection of the next cell to process."""
    for i, row in enumerate(assignment):
        for j, val in enumerate(row):
            if not assignment[i][j]:
                return i, j
    return None


def minimumNextFreeCell(assignment):
    """Optimized selection of the next cell to process. Use the most
restricted cell in order to ensure faster backtracking. The most
restricted cell is the cell which can hold the fewest values.

    """
    allValues = set(range(1, 10))
    heap = []
    for i, row in enumerate(assignment):
        for j, val in enumerate(row):
            if not assignment[i][j]:
                # get horizontal values
                rowVals = set(assignment[i])

                # get vertical values
                colVals = set([assignment[i][j] for i in range(len(assignment))])

                # get block values
                blockVals = set([assignment[i][j] for i, j in BLOCK_TABLE[(i, j)]])
                possibleVals = allValues - rowVals - colVals - blockVals
                heappush(heap, (len(possibleVals), (i, j)))
    return None if not heap else heappop(heap)[1]


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        assignment = toIntBoard(board)

        def helper():
            if isSolution(assignment):
                # leetcode wants in-place solution
                toResult(assignment, board)
                return assignment

            # cell = nextFreeCell(assignment)
            cell = minimumNextFreeCell(assignment)
            i, j = cell
            for val in range(1, 10):
                if isValid(assignment, cell, val):
                    # do move
                    assignment[i][j] = val
                    result = helper()
                    if result:
                        return result
                    # undo move
                    assignment[i][j] = 0
            return None

        return helper()


def toResult(assignment, board):
    for i, row in enumerate(assignment):
        for j, col in enumerate(assignment):
            board[i][j] = str(assignment[i][j])


def toBoard(s: str):
    lines = s.splitlines()
    board = []
    for l in lines:
        row = []
        for c in l:
            row.append(int(c))
        board.append(row)
    return board


def toIntBoard(lists):
    board = []
    for l in lists:
        row = []
        for c in l:
            if c == ".":
                row.append(0)
            else:
                row.append(int(c))
        board.append(row)
    return board


def toString(board):
    s = ""
    for i, row in enumerate(board):
        if i % 3 == 0 and i != 0:
            s += "-----------------------------------\n"
        for j, val in enumerate(row):
            if j % 3 == 0 and j != 0:
                s += " | "
            s += " {} ".format(str(val))
        s += "\n"
    return s


def testSolve():
    s = """530070000
600195000
098000060
800060003
400803001
700020006
060000280
000419005
000080079"""

    sol = Solution()
    actual = sol.solveSudoku(toBoard(s))
    expected = [
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 9],
    ]

    assert actual == expected


def testSolve2():
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]

    sol = Solution()
    sol.solveSudoku(board)
    expected = [
        ["5", "3", "4", "6", "7", "8", "9", "1", "2"],
        ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
        ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
        ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
        ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
        ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
        ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
        ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
        ["3", "4", "5", "2", "8", "6", "1", "7", "9"],
    ]
    assert board == expected


def testToBoard():
    s = """0123
4567
8901
"""
    actual = toBoard(s)
    expected = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 0, 1]]
    assert actual == expected


def testToString():
    s = """530070000
600195000
098000060
800060003
400803001
700020006
060000280
000419005
000080079"""

    board = toBoard(s)
    actual = toString(board)
    print("\n{}".format(actual))


def testIsSolution():
    board = [[1, 2, 3], [4, 5, 6]]
    assert isSolution(board) == True

    board = [[1, 2, 3], [4, 0, 6]]
    assert isSolution(board) == False


def testNextFreeCell():
    board = [[1, 2, 3], [4, 5, 6]]
    assert nextFreeCell(board) == None

    board = [[1, 2, 3], [4, 0, 6]]
    assert nextFreeCell(board) == (1, 1)

    board = [[1, 2, 3], [4, 1, 6], [1, 2, 0]]
    assert nextFreeCell(board) == (2, 2)


def testBlockLookup():
    actual = makeBlockLookup()
    expected = set(
        [(0, 6), (0, 7), (0, 8), (1, 6), (1, 7), (1, 8), (2, 6), (2, 7), (2, 8)]
    )

    for cell in expected:
        assert actual[cell] == expected


def testIsValid():
    s = """530070000
600195000
098000060
800060003
400803001
700020006
060000280
000419005
000080079"""

    board = toBoard(s)
    actual = isValid(board, (1, 1), 8)
    assert actual == False

    actual = isValid(board, (1, 1), 5)
    assert actual == False

    actual = isValid(board, (1, 1), 6)
    assert actual == False

    actual = isValid(board, (1, 1), 4)
    assert actual == True
