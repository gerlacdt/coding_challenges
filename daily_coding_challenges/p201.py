"""Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

You are given an array of arrays of integers, where each array
corresponds to a row in a triangle of numbers. For example, [[1], [2,
3], [1, 5, 1]] represents the triangle:

  1
 2 3
1 5 1

We define a path in the triangle to start at the top and go down one
row at a time to an adjacent value, eventually ending with an entry on
the bottom row. For example, 1 -> 3 -> 5. The weight of the path is
the sum of the entries.

Write a program that returns the weight of the maximum weight path.

"""


def getMaxPath(triangle):
    maxPath = 0

    def helper(p=(0, 0), weight=0):
        nonlocal maxPath
        y, x = p
        if x < 0 or y < 0:
            return weight
        elif y >= len(triangle) or x >= len(triangle[y]):
            return weight
        else:
            r1 = helper((y+1, x-1), weight+triangle[y][x])
            r2 = helper((y+1, x), weight+triangle[y][x])
            r3 = helper((y+1, x+1), weight+triangle[y][x])
            currentMax = max(r1, r2, r3)
            if currentMax > maxPath:
                maxPath = currentMax
            return currentMax

    helper()
    return maxPath


def test():
    arr = [[1], [2, 3], [1, 5, 1]]
    actual = getMaxPath(arr)
    expected = 9
    assert actual == expected

    arr = [[1], [2, 3], [7, 5, 1]]
    actual = getMaxPath(arr)
    expected = 11
    assert actual == expected

    arr = [[1], [2, 3], [1, 5, 1], [1, 1, 1, 6]]
    actual = getMaxPath(arr)
    expected = 11
    assert actual == expected

    arr = []
    actual = getMaxPath(arr)
    expected = 0
    assert actual == expected
