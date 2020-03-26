"""Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Boggle is a game played on a 4 x 4 grid of letters. The goal is to
find as many words as possible that can be formed by a sequence of
adjacent letters in the grid, using each cell at most once. Given a
game board and a dictionary of valid words, implement a Boggle solver.

"""


def successors(position, board, visited):
    """Return neighbors for the given board position. Consider positions
out of the board range and already visited fields. These fields are
removed from the successors result set.

    """
    row, col = position
    succs = []
    for r in range(row-1, row+2):
        for c in range(col-1, col+2):
            if r < 0 or c < 0 or r > len(board) - 1 or c > len(board[0]) - 1 or visited[r][c]:
                continue
            else:
                succs.append((r, c))
    return succs


def boggle(board, dictionary):
    """Use backtracking/DFS to find all possible solution. Solutions/words
can have duplicates, so use a set in order to get rid of them.
Actually backtracking only happens if all successors/neighbors are
visited or are out of the board range.

    """
    result = set()
    visited = [[None for row in board] for col in board[0]]

    def helper(assignment, position):
        nonlocal visited
        row, col = position
        # make move
        assignment.append(board[row][col])
        visited[row][col] = True

        # isGoal()
        if "".join(assignment) in dictionary:
            result.add("".join(assignment))

        # call recursively
        for succ in successors(position, board, visited):
            helper(assignment[:], succ)

        # unmake move
        visited[row][col] = False
        assignment.pop()

    for row in range(len(board)):
        for col in range(len(board[0])):
            helper([], (row, col))
    return result


def test():
    dictionary = {"GEEKS", "FOR", "QUIZ", "GO"}
    board = [['G', 'I', 'Z'],
             ['U', 'E', 'K'],
             ['Q', 'S', 'E']]

    actual = boggle(board, dictionary)
    expected = set(["GEEKS", "QUIZ"])
    assert actual == expected
