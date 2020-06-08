"""Given a NxN matrix, the task is to print it elements in a diagonal
pattern:

Example 1:

1 2 3
4 5 6
7 8 9

Output:

[1,2,4,7,5,3,6,8,9]


see: https://www.geeksforgeeks.org/print-matrix-diagonal-pattern/

"""


def toggle(direction):
    if direction == "UP":
        return "DOWN"
    elif direction == "DOWN":
        return "UP"
    raise RuntimeError("Invalid direction given")


class Solution:
    def traverse(self, matrix):
        assert len(matrix) == len(matrix[0])  # should be a square matrix
        result = []
        direction = "UP"
        i = 0
        j = 0
        N = len(matrix) - 1

        while i != N or j != N:
            # print("i: {} j: {} direction: {}".format(i, j, direction))
            # print("val: {}".format(matrix[i][j]))
            result.append(matrix[i][j])
            if direction == "UP" and i == 0 and j != N:
                j += 1
                direction = toggle(direction)
            elif direction == "DOWN" and j == 0 and i != N:
                i += 1
                direction = toggle(direction)
            elif direction == "DOWN" and i == N:
                j += 1
                direction = toggle(direction)
            elif direction == "UP" and j == N:
                i += 1
                direction = toggle(direction)
            elif direction == "DOWN":
                i += 1
                j -= 1
            elif direction == "UP":
                i -= 1
                j += 1
            else:
                raise RuntimeError("Invalid case, something went wrong.")

        result.append(matrix[i][j])
        return result


def test3Matrix():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    sol = Solution()
    actual = sol.traverse(matrix)
    expected = [1, 2, 4, 7, 5, 3, 6, 8, 9]
    assert actual == expected


def test4Matrix():
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    sol = Solution()
    actual = sol.traverse(matrix)
    expected = [1, 2, 5, 9, 6, 3, 4, 7, 10, 13, 14, 11, 8, 12, 15, 16]
    assert actual == expected


def test2Matrix():
    matrix = [[1, 2], [3, 4]]
    sol = Solution()
    actual = sol.traverse(matrix)
    expected = [1, 2, 3, 4]
    assert actual == expected
