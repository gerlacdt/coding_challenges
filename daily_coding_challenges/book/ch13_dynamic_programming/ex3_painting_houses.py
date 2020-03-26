"""A builder is looking to build a row of n houses that can be of k
different colors. She has a goal of minimizing cost while ensuring
that no two neighboring houses are of the same color.

Given an n by k matrix where entry at the ith wor and jth column
represents the cost to build the ith house with the jth color, return
the minimum cost required.

"""


def houses(matrix):
    n = len(matrix)
    k = len(matrix[0])
    # otherwise there are not enough colors to paint houses without conflicts
    assert k > 1

    table = [matrix[0][:]]
    for i in range(1, n):
        row = matrix[i]
        minprices = [0] * k
        for color, _ in enumerate(row):
            minprices[color] = min(
                table[i - 1][color] + row[j] for j in range(k) if j != color
            )
        table.append(minprices)
    return min(table[-1])


def sampleSolution(matrix):
    k = len(matrix[0])
    solution_row = [0] * k

    for r, row in enumerate(matrix):
        new_row = []
        for c, val in enumerate(row):
            new_row.append(min(solution_row[i] for i in range(k) if i != c) + val)
        solution_row = new_row
    return min(solution_row)


def test():
    matrix = [[10, 5, 5], [5, 10, 3], [2, 1, 1], [1, 2, 1]]
    actual = houses(matrix)
    actual1 = sampleSolution(matrix)
    expected = 10
    assert actual == expected
    assert actual1 == expected
