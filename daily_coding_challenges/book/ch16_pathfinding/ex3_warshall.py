"""The transitive closure of a graph is a measure of which vertices
are reachable from other vertices. It can be represented as a matrix
M, where M[i][j] == 1 if there is a path between vertices i and j, and
otherwise 0.

For example, see testClosure()

"""


def toTransitiveClosure(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == float("inf"):
                matrix[i][j] = 0
            if matrix[i][j] > 0:
                matrix[i][j] = 1
            if i == j:
                matrix[i][j] = 1


def warshall(graph):
    # initialize base case, consider existing edges
    n = len(graph)
    d = [[0 if i == j else float("inf") for j in range(n)] for i in range(n)]
    for i, values in graph.items():
        for v in values:
            j, cost = v
            d[i][j] = cost

    for k in range(1, n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    return d


def closure(graph):
    matrix = warshall(graph)
    toTransitiveClosure(matrix)
    return matrix


def testClosure():
    graph = {0: [(1, 1), (3, 1)], 1: [(2, 1)], 2: [], 3: []}
    actual = closure(graph)
    expected = [[1, 1, 1, 1], [0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
    assert actual == expected


def testWarshall():
    graph = {
        0: [(1, 3), (2, 8), (4, -4)],
        1: [(3, 1), (4, 7)],
        2: [(1, 4)],
        3: [(0, 2), (2, -5)],
        4: [(3, 6)],
    }

    actual = warshall(graph)
    expected = [
        [0, 1, -3, 2, -4],
        [3, 0, -4, 1, 7],
        [7, 4, 0, 5, 11],
        [2, -1, -5, 0, 6],
        [8, 5, 1, 6, 0],
    ]

    assert actual == expected
