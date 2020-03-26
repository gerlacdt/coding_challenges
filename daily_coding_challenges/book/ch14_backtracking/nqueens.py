"""

Place n queens on board so that no queen threaten each other.

"""


def nqueens(n=8, board=[]):
    if n == len(board):
        return 1
    count = 0
    for i in range(n):
        board.append(i)
        if is_valid(board):
            count += nqueens(n, board)
        board.pop()
    return count


def is_valid(board):
    x, y = len(board) - 1, board[-1]
    for i in range(len(board) - 1):
        other_x, other_y = i, board[i]

        # conflict at at x-axis, queens are in the same row
        if y == other_y:
            return False

        # conflict at diagonal
        if abs(x - other_x) == abs(y - other_y):
            return False

    return True


def test():
    actual = nqueens()
    expected = 92
    assert actual == expected

    actual = nqueens(4)
    expected = 2
    assert actual == expected
