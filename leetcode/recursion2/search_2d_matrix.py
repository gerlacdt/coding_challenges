"""Write an efficient algorithm that searches for a value in an m x n
matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
Example:

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.


see:
https://leetcode.com/explore/learn/card/recursion-ii/470/divide-and-conquer/2872/discuss/694432/python-divide-and-conquer

"""


class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix:
            return False
        n = len(matrix)
        m = len(matrix[0])
        i = 0
        j = m - 1
        while i < n and j >= 0:
            val = matrix[i][j]
            if val == target:
                return True
            if val > target:
                j -= 1
            else:
                i += 1
        return False


def test():
    sol = Solution()
    matrix = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30],
    ]

    actual = sol.searchMatrix(matrix, 5)
    expected = True
    assert actual == expected

    actual2 = sol.searchMatrix(matrix, 20)
    expected2 = False
    assert actual2 == expected2

    matrix = []
    expected3 = False
    actual3 = sol.searchMatrix(matrix, 0)
    assert actual3 == expected3
