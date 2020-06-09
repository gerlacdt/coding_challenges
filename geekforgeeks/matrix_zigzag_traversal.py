"""
Given a 2d matrix,, print all elements of the given matrix in a diagonal order.

Example 1:

1     2     3     4
5     6     7     8
9     10    11    12
13    14    15    16
17    18    19    20

Output:

 1
 5     2
 9     6     3
 13    10     7     4
 17    14    11     8
 18    15    12
 19    16
 20

see: https://www.geeksforgeeks.org/zigzag-or-diagonal-traversal-of-matrix/
"""


class Solution:
    def zigzag(self, matrix):
        result = []
        N = len(matrix) - 1
        M = len(matrix[0]) - 1

        # loop rows down
        for i in range(N + 1):
            j = 0
            # loop diagonal up
            while i >= 0 and j <= M:
                result.append(matrix[i][j])
                i -= 1
                j += 1

        # loop through columns of last row
        for j in range(1, M + 1):
            i = N
            # loop diagonal up
            while i >= 0 and j <= M:
                result.append(matrix[i][j])
                i -= 1
                j += 1

        return result


def test():
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    sol = Solution()
    actual = sol.zigzag(matrix)
    expected = [1, 5, 2, 9, 6, 3, 13, 10, 7, 4, 14, 11, 8, 15, 12, 16]
    assert actual == expected
