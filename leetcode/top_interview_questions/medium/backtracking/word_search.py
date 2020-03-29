"""Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent
cell, where "adjacent" cells are those horizontally or vertically
neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.

"""

from typing import List


class State:
    def __init__(self, fields, path):
        self.fields = fields
        self.path = path

    def __str__(self):
        return "{} {}".format(self.fields, self.path)


class Solution:
    def exist(self, board: List[List[str]], goal: str) -> bool:
        state = State([], "")

        def backtrack(currentPos):
            nonlocal state
            if state.path == goal:
                return True
            # move
            for position in self.successors(board, currentPos):
                i, j = position
                # check is successor state is valid
                if (
                    board[i][j] == goal[len(state.path)]  # new char matches goal index
                    and position not in state.fields  # fields may be used only once
                ):
                    state.fields.append(position)
                    state.path = state.path + board[i][j]
                    result = backtrack(position)
                    if result:
                        return True

            # undo move
            state.fields.pop()
            state.path = state.path[:-1]
            return False

        for i in range(len(board)):
            state = State([], "")
            for j in range(len(board[0])):
                c = board[i][j]
                if c == goal[0]:
                    state = State([(i, j)], c)
                    result = backtrack((i, j))
                    if result:
                        return True
        return False

    def successors(self, board, position):
        i, j = position
        max_rows = len(board) - 1
        max_cols = len(board[0]) - 1
        results = []
        if i + 1 <= max_rows and i + 1 >= 0:
            results.append((i + 1, j))

        if i - 1 <= max_rows and i - 1 >= 0:
            results.append((i - 1, j))

        if j + 1 <= max_cols and j + 1 >= 0:
            results.append((i, j + 1))

        if j - 1 <= max_cols and j - 1 >= 0:
            results.append((i, j - 1))

        return results


def test():
    sol = Solution()
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    goal = "ABCCED"
    actual = sol.exist(board, goal)
    expected = True
    assert actual == expected

    goal = "SEE"
    actual = sol.exist(board, goal)
    expected = True
    assert actual == expected

    goal = "ABCB"
    actual = sol.exist(board, goal)
    expected = False
    assert actual == expected

    board = [["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]]
    goal = "ABCESEEEFS"
    actual = sol.exist(board, goal)
    expected = True
    assert actual == expected
