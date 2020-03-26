"""
River Sizes

You are given a two-dimensional array (matrix) of potentially
unequal height and width containing only 0s and 1s. Each 0 represents
land, and each 1 represents part of a river. A river consists of any
number of 1s that are either horizontally or vertically adjacent (but
not diagonally adjacent). The number of adjacent 1s forming a river
determine its size. Write a function that returns an array of the
sizes of all rivers represented in the input matrix. Note that these
sizes do not need to be in any particular order.


Sample input:

[
 [1,0,0,1,0],
 [1,0,1,0,0],
 [0,0,1,0,1],
 [1,0,1,0,1],
 [1,0,1,1,0],
]

Sample output:

[1,2,2,2,5]
"""


def successors(node, table, visited):
    nrows = len(table) - 1
    ncols = len(table[0]) - 1
    row, col, size = node
    succ1 = succ2 = succ3 = succ4 = None
    if row+1 <= nrows and table[row+1][col] == 1 and (row+1, col) not in visited:
        succ1 = (row+1, col, 1+size if table[row+1][col] else size)
    if row-1 >= 0 and table[row-1][col] == 1 and (row-1, col) not in visited:
        succ2 = (row-1, col, 1+size if table[row-1][col] else size)
    if col+1 <= ncols and table[row][col+1] == 1 and (row, col+1) not in visited:
        succ3 = (row, col+1, 1+size if table[row][col+1] else size)
    if col-1 >= 0 and table[row][col-1] == 1 and (row, col-1) not in visited:
        succ4 = (row, col-1, 1+size if table[row][col-1] else size)
    return list(filter(lambda s: s, [succ1, succ2, succ3, succ4]))


def riverSizes(table):
    nrows = len(table)
    ncols = len(table[0])
    frontier = [(r, c, 1)
                for r in range(nrows)
                for c in range(ncols) if table[r][c] == 1]
    frontier.reverse()
    result = []
    visited = set()
    while frontier:
        node = frontier.pop()
        row, col, size = node
        if (row, col) not in visited:
            visited.add((row, col))
            if table[row][col] == 1:
                succs = successors(node, table, visited)
                if not succs:
                    result.append(size)
                for s in succs:
                    srow, scol, _ = s
                    if (srow, scol) not in visited:
                        frontier.append(s)
            else:
                continue
    return list(sorted(result))


def test():
    table = [
        [1,0,0,1,0],
        [1,0,1,0,0],
        [0,0,1,0,1],
        [1,0,1,0,1],
        [1,0,1,1,0],
    ]
    actual = riverSizes(table)
    expected = [1,2,2,2,5]
    assert actual == expected

    table = [
        [1,1,1,0,0],
        [1,1,1,0,0],
        [1,1,1,0,0],
        [0,0,1,0,1],
    ]
    actual = riverSizes(table)
    expected = [1, 10]
    assert actual == expected
