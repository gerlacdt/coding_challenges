"""You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Note:

You have to rotate the image in-place, which means you have to modify
the input 2D matrix directly. DO NOT allocate another 2D matrix and do
the rotation.

Example 1:

Given input matrix =
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]

Example 2:

Given input matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
],

rotate the input matrix in-place such that it becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]

"""


def transpose(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


def reverseRows(matrix):
    n = len(matrix)
    for y in range(n):
        for x in range(n // 2):
            matrix[y][x], matrix[y][n-x-1] = matrix[y][n-x-1], matrix[y][x]


class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        transpose(matrix)
        reverseColumns(matrix)


def test():
    input1 = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
    expected1 = [[7, 4, 1],
                 [8, 5, 2],
                 [9, 6, 3]]

    input2 =[[5, 1, 9, 11],
             [2, 4, 8, 10],
             [13, 3, 6, 7],
             [15, 14, 12, 16]]
    expected2 = [[15, 13, 2, 5],
                 [14, 3, 4, 1],
                 [12, 6, 8, 9],
                 [16, 7, 10, 11]]

    sol = Solution()
    sol.rotate(input1)
    sol.rotate(input2)

    assert input1 == expected1
    assert input2 == expected2
