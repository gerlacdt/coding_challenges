"""Given a m * n matrix mat of integers, sort it diagonally in ascending
order from the top-left to the bottom-right then return the sorted
array.

Example 1:

Input: mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
Output: [[1,1,1,1],[1,2,2,2],[1,2,3,3]]

"""

from typing import List


class Solution:
    def diagonalSort(self, matrix: List[List[int]]) -> List[List[int]]:
        N = len(matrix)
        M = len(matrix[0])
        result = [[0 for _ in range(M)] for _ in range(N)]

        # sort, begin at cols, e.g. (0,0), (0,1), (0,2)...
        for col in range(M):
            # collect diagonal
            i = 0
            j = col
            diagonal = []
            while i < N and j < M:
                diagonal.append(matrix[i][j])
                i += 1
                j += 1
            diagonal.sort(reverse=True)
            # put sorted diagonal back in matrix
            i = 0
            j = col
            while i < N and j < M:
                result[i][j] = diagonal.pop()
                i += 1
                j += 1

        # sort begin in rows, e.g. (1,0), (2,0), (3,0)...
        for row in range(1, N):
            i = row
            j = 0
            diagonal = []
            while i < N and j < M:
                diagonal.append(matrix[i][j])
                i += 1
                j += 1
            diagonal.sort(reverse=True)
            # put sorted diagonal back in matrix
            i = row
            j = 0
            while i < N and j < M:
                result[i][j] = diagonal.pop()
                i += 1
                j += 1

        return result


def test():
    matrix = [[3, 3, 1, 1], [2, 2, 1, 2], [1, 1, 1, 2]]
    sol = Solution()
    actual = sol.diagonalSort(matrix)
    expected = [[1, 1, 1, 1], [1, 2, 2, 2], [1, 2, 3, 3]]
    assert actual == expected


def test2():
    matrix = [[3, 3, 3, 3], [3, 2, 2, 2], [3, 2, 1, 1], [3, 2, 1, 0]]
    sol = Solution()
    actual = sol.diagonalSort(matrix)
    expected = [[0, 1, 2, 3], [1, 1, 2, 3], [2, 2, 2, 3], [3, 3, 3, 3]]
    assert actual == expected
