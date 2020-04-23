"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given an N by N matrix, rotate it by 90 degrees clockwise.

For example, given the following matrix:

[[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]
you should return:

[[7, 4, 1],
 [8, 5, 2],
 [9, 6, 3]]

Follow-up: What if you couldn't use any extra space?

https://www.geeksforgeeks.org/rotate-a-matrix-by-90-degree-in-clockwise-direction-without-using-any-extra-space/?ref=rp
"""


class Solution:
    def rotate(self, matrix):
        n = len(matrix)
        result = [[0 for _ in range(n)] for _ in range(n)]

        for i in range(n):
            for j in range(n):
                result[j][n - i - 1] = matrix[i][j]
        return result

    def rotateInPlace(self, matrix):
        n = len(matrix)
        for i in range(n // 2):
            for j in range(i, n - i - 1):
                temp = matrix[i][j]
                matrix[i][j] = matrix[n - 1 - j][i]
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
                matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
                matrix[j][n - 1 - i] = temp
        return matrix


def test():
    sol = Solution()
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    actual = sol.rotate(matrix)
    actual2 = sol.rotateInPlace(matrix)
    expected = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    assert actual == expected
    assert actual2 == expected

    matrix = [[1, 2], [3, 4]]
    actual = sol.rotate(matrix)
    actual2 = sol.rotateInPlace(matrix)
    expected = [[3, 1], [4, 2]]
    assert actual == expected
    assert actual2 == expected
