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

"""


def getVertical(matrix, n):
    assert n >= 0
    assert n < len(matrix[0])
    return [matrix[i][n] for i in range(len(matrix))]


class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        def binary_search(nums, low, high):
            if low > high:
                return None
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                return binary_search(nums, low, mid - 1)
            return binary_search(nums, mid + 1, high)

        result = None
        for row in matrix:
            result = binary_search(row, 0, len(row) - 1)
            if result or result == 0:
                return True

        return False


def test1():
    sol = Solution()
    matrix = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30],
    ]

    target = 5
    actual = sol.searchMatrix(matrix, target)
    expected = True
    assert actual == expected

    target = 20
    actual = sol.searchMatrix(matrix, target)
    expected = False
    assert actual == expected

    target = 0
    actual = sol.searchMatrix([], target)
    expected = False
    assert actual == expected
