"""Connect 4 is a game where opponents take turns dropping red or
black discs into a 7x6 vertically suspended grid. The game ends either
when one player creates a line of four consecutive discs of their
color (horizontally, vertically, diagonally), or when there is no more
spots left in the grid.

nDesign and implement Connect 4.

"""

from collections import namedtuple
import pytest


class Game:
    def __init__(self):
        # board size
        self.n = 7
        self.m = 6
        self.board = [[0 for _ in range(self.m)] for _ in range(self.n)]
        self.steps = self.n * self.m

    def move(self, player, coords):
        row, col = coords

        if self._isOver():
            return None, None  # no player wins, game is over

        # make move
        if self.board[row][col] != 0:
            raise RuntimeError("Invalid move, field already occupied: {}", (row, col))
        self.board[row][col] = player
        self.steps -= 1
        # print("{}".format(toString(self.board)))

        if self._isWinner(player, coords):
            return player, None  # player wins, game is over

        return None, True  # no player won till now, continue game

    def _isWinner(self, player, coords):
        x, y = coords
        # check row
        row = self.board[x]
        if self._fourConsecutive(player, row):
            return True

        # check column
        column = [self.board[i][y] for i in range(self.n)]
        if self._fourConsecutive(player, column):
            return True

        # check downwards diagonal
        # (x + 1, y + 1) or (x - 1, y - 1)
        diagonal = []
        while x > 0 and y > 0:
            x -= 1
            y -= 1
            diagonal.append(self.board[x][y])
        diagonal.reverse()
        x, y = coords  # reset x,y
        diagonal.append(self.board[x][y])

        while x < self.n - 1 and y < self.m - 1:
            x += 1
            y += 1
            diagonal.append(self.board[x][y])

        # print("downwards diagonal: {}".format(diagonal))
        if self._fourConsecutive(player, diagonal):
            return True

        # check upwards diagonal
        # (x+1, y-1) or (x-1, y+1)
        diagonal = []
        x, y = coords  # reset x,y
        while x > 0 and y < self.m - 1:
            x -= 1
            y += 1
            diagonal.append(self.board[x][y])
        diagonal.reverse()
        x, y = coords  # reset x,y
        diagonal.append(self.board[x][y])
        while x < self.n - 1 and y > 0:
            x += 1
            y -= 1
            diagonal.append(self.board[x][y])

        # print("upwards diagonal: {}".format(diagonal))
        if self._fourConsecutive(player, diagonal):
            return True

        return False

    def _fourConsecutive(self, player, lst):
        if len(lst) < 4:
            return False
        count = 0
        for p in lst:
            if p == player:
                count += 1
            else:
                count = 0
            if count >= 4:
                return True
        return False

    def _isOver(self):
        return True if self.steps == 0 else False


Case = namedtuple("Case", ["args", "expected"])


def testFourConsecutive():
    game = Game()
    cases = [
        Case((1, [0, 1, 1, 1, 1, 0]), True),
        Case((1, [0, 1, 2, 1, 1, 1, 2]), False),
        Case((1, [0, 1, 1, 1]), False),
        Case((1, [0, 2, 1, 1, 1, 2, 1, 1, 1, 1]), True),
    ]
    for c in cases:
        player, lst = c.args
        actual = game._fourConsecutive(player, lst)
        assert actual == c.expected, "Case: {}".format(c)


def testIsWinner():
    game = Game()
    cases = [
        Case((toBoard(FOUR_IN_A_ROW_BOARD), 1, (2, 4)), True),
        Case((toBoard(FOUR_IN_A_COLUMN_BOARD), 1, (4, 2)), True),
        Case((toBoard(FOUR_IN_A_DOWNWARDS_DIAGONAL_BOARD), 1, (3, 3)), True),
        Case((toBoard(FOUR_IN_A_UPWARDS_DIAGONAL_BOARD), 1, (3, 1)), True),
        Case((toBoard(NO_FOUR_BOARD), 1, (1, 1)), False),
    ]

    for c in cases:
        board, player, coords = c.args
        game.board = board
        actual = game._isWinner(player, coords)
        assert actual == c.expected, "Case: {}".format(c)


def testMove():
    game = Game()
    cases = [
        Case((toBoard(FULL_BOARD), 1, (6, 5), 0), (None, None)),
        Case((toBoard(THREE_IN_A_COLUMN_BOARD), 1, (4, 2), 25), (1, None)),
        Case((toBoard(PLAYER_2_WINS_BOARD), 2, (2, 3), 25), (2, None)),
        Case((toBoard(NO_PLAYER_WINS_BOARD), 1, (5, 3), 25), (None, True)),
    ]

    for c in cases:
        board, player, coords, steps = c.args
        game.board = board
        game.steps = steps
        actual = game.move(player, coords)
        assert actual == c.expected, "Case: {}".format(c)


def testInvalidMove():
    game = Game()
    board, player, coords = toBoard(FULL_BOARD), 1, (6, 4)
    game.board = board
    with pytest.raises(RuntimeError) as excinfo:
        game.move(player, coords)


def testBoard():
    s = """000000
000000
011110
000000
000000
000000
000000"""
    board = toBoard(s)
    assert toString(board) == s


def toBoard(s):
    lines = str.splitlines(s)
    board = [[0 for _ in range(6)] for _ in range(7)]
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            board[i][j] = int(c)
    return board


def toString(board):
    s = ""
    for row in board:
        for field in row:
            s += str(field)
        s += "\n"
    return s[:-1]


FOUR_IN_A_ROW_BOARD = """000000
000000
111100
000000
000000
000000
000000"""


FOUR_IN_A_COLUMN_BOARD = """000000
001000
001000
001000
001000
000000
000000"""

THREE_IN_A_COLUMN_BOARD = """000000
001000
001000
001000
000000
000000
000000"""

FOUR_IN_A_DOWNWARDS_DIAGONAL_BOARD = """000000
010000
001000
000100
000010
000000
000000"""

FOUR_IN_A_UPWARDS_DIAGONAL_BOARD = """000010
000100
001000
010000
000000
000000
000000"""

NO_FOUR_BOARD = """000000
211120
210000
010000
000000
000000
000000"""

FULL_BOARD = """121212
212121
121212
212121
121212
212121
121210"""

PLAYER_2_WINS_BOARD = """111000
111000
222000
010000
010000
010000
000000"""

NO_PLAYER_WINS_BOARD = """111000
111000
222000
010000
010000
010000
000000"""


EMPTY_BOARD = """000000
000000
000000
000000
000000
000000
000000"""
