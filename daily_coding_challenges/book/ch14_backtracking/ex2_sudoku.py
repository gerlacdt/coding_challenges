"""
Solve a given Sudoku puzzle.
"""


def isFull(board):
    for y in range(len(board)):
        for x in range(len(board[0])):
            if not board[y][x]:
                return False
    return True


def findNextField(board):
    for y in range(len(board)):
        for x in range(len(board[0])):
            if not board[y][x]:
                return y, x
    return None


def calcBlocks():
    blocks = []  # list of all existing blocks as index list
    for i in range(3):
        for j in range(3):
            block = set()
            for i2 in range(3):
                for j2 in range(3):
                    y = i2 + 3 * i
                    x = j2 + 3 * j
                    block.add((y, x))
            blocks.append(block)

    blockMap = {}
    for b in blocks:
        for index in b:
            blockMap[index] = b
    return blockMap


BLOCKS = calcBlocks()


def isValid(y, x, board):
    # check rows
    row = board[y]
    for i, val in enumerate(row):
        if i == x:
            continue
        if board[y][x] == val:
            return False

    # check columns
    for i, row in enumerate(board):
        if i == y:
            continue
        if board[y][x] == row[x]:
            return False

    # check blocks
    blockFields = BLOCKS[(y, x)]
    for field in blockFields:
        cy, cx = field
        if (cy, cx) == (y, x):
            continue
        if board[y][x] == board[cy][cx]:
            return False

    return True


def sudoku(board):
    if isFull(board):
        return board
    result = None
    y, x = findNextField(board)
    for val in range(1, 10):
        board[y][x] = val
        if isValid(y, x, board):
            result = sudoku(board)
            if result:
                return result
        board[y][x] = 0  # undo assignment
    return result


def printBoard(board):
    print()
    n = len(board)
    for i in range(n):
        if i % 3 == 0 and i != 0:
            print("")
            print("---------------------")
        else:
            print("")
        for j in range(n):
            if j % 3 == 0 and j != 0:
                print("| ", end="")
            print("{} ".format(board[i][j]), end="")
    print()


def test():
    board = [
        [2, 5, 0, 0, 3, 0, 9, 0, 1],
        [0, 1, 0, 0, 0, 4, 0, 0, 0],
        [4, 0, 7, 0, 0, 0, 2, 0, 8],
        [0, 0, 5, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 9, 8, 1, 0, 0],
        [0, 4, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 3, 6, 0, 0, 7, 2],
        [0, 7, 0, 0, 0, 0, 0, 0, 3],
        [9, 0, 3, 0, 0, 0, 6, 0, 4],
    ]
    actual = sudoku(board)
    expected = [
        [2, 5, 8, 7, 3, 6, 9, 4, 1],
        [6, 1, 9, 8, 2, 4, 3, 5, 7],
        [4, 3, 7, 9, 1, 5, 2, 6, 8],
        [3, 9, 5, 2, 7, 1, 4, 8, 6],
        [7, 6, 2, 4, 9, 8, 1, 3, 5],
        [8, 4, 1, 6, 5, 3, 7, 2, 9],
        [1, 8, 4, 3, 6, 9, 5, 7, 2],
        [5, 7, 6, 1, 4, 2, 8, 9, 3],
        [9, 2, 3, 5, 8, 7, 6, 1, 4],
    ]

    assert actual == expected
    printBoard(actual)
