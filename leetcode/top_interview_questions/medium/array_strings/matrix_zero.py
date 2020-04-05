"""Given a m x n matrix, if an element is 0, set its entire row and
column to 0. Do it in-place.

Example 1:
Input:
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output:
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]


Example 2:
Input:
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output:
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]

Follow up:

A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?

"""

from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])
        zero_rows = set()
        zero_columns = set()

        # collect zero rows and columns
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_columns.add(j)

        # set zeros rows
        for i in range(n):
            if i in zero_rows:
                for j2 in range(m):
                    matrix[i][j2] = 0

        # set zero columns
        for j in range(m):
            if j in zero_columns:
                for i2 in range(n):
                    matrix[i2][j] = 0

        return None


def test():
    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    sol = Solution()
    sol.setZeroes(matrix)
    expected = [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
    assert matrix == expected

    matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    sol.setZeroes(matrix)
    expected = [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
    assert matrix == expected
