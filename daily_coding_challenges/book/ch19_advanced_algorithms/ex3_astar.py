"""
TODO
"""

from heapq import heappop, heappush


def manhatten_distance(src, dest):
    src_y, src_x = src
    dest_y, dest_x = dest
    return abs(src_y - dest_y) + abs(src_x - dest_x)


def heuristicFn(board):
    table = {
        1: (0, 0),
        2: (0, 1),
        3: (0, 2),
        4: (1, 0),
        5: (1, 1),
        6: (1, 2),
        7: (2, 0),
        8: (2, 1),
        0: (2, 2),
    }
    result = 0
    for y, row in enumerate(board):
        for x, col in enumerate(row):
            val = board[y][x]
            result += manhatten_distance((y, x), table[val])
    return result


GOAL = ((1, 2, 3), (4, 5, 6), (7, 8, 0))


def isGoal(board):
    return True if GOAL == board else False


def findEmptyIndex(board):
    for y, row in enumerate(board):
        for x, col in enumerate(row):
            if col == 0:
                return (y, x)
    return None


def printBoard(board):
    for row in board:
        for col in row:
            print(col, end="")
        print()


UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)
DIRECTIONS = [UP, DOWN, LEFT, RIGHT]


def isValid(newEmptyPos):
    y, x = newEmptyPos
    return True if y < 3 and y > -1 and x < 3 and x > -1 else False


def clone(board):
    n = len(board)
    b = [[0 for _ in range(n)] for _ in range(n)]
    for y, row in enumerate(board):
        for x, col in enumerate(row):
            b[y][x] = board[y][x]
    return b


def successorsNinePuzzle(board):
    empty = findEmptyIndex(board)
    empty_row, empty_col = empty
    results = []
    for d in DIRECTIONS:
        newEmptyPos = tuple([sum(pos) for pos in zip(empty, d)])
        newEmpty_row, newEmpty_col = newEmptyPos
        if isValid(newEmptyPos):
            clonedBoard = clone(board)
            # swap empty with value
            clonedBoard[empty_row][empty_col], clonedBoard[newEmpty_row][
                newEmpty_col
            ] = (
                clonedBoard[newEmpty_row][newEmpty_col],
                clonedBoard[empty_row][empty_col],
            )
            results.append((tuple([tuple(row) for row in clonedBoard])))
    return results


def createPath(parents, state):
    current = state
    path = []
    while current:
        path.append(current)
        current = parents[current]
    return list(reversed(path))


def astar(start, successors, h_func, cost_func=lambda x, y: 1):
    frontier = [(h_func(start), start)]
    parents = {}
    parents[start] = None
    path_costs = {}
    path_costs[start] = 0

    while frontier:
        f, state = heappop(frontier)
        if h_func(state) == 0:
            return state, createPath(parents, state)
        for state_succ in successors(state):
            g = path_costs[state] + cost_func(state, state_succ)
            if state_succ not in path_costs or path_costs[state_succ] > g:
                heappush(frontier, (h_func(state_succ) + g, state_succ))
                parents[state_succ] = state
                path_costs[state_succ] = g
    return None


def testIsGoal():
    board = ((1, 2, 3), (4, 5, 6), (7, 8, 0))
    actual = isGoal(board)
    expected = True
    assert actual == expected

    board = ((1, 2, 3), (4, 5, 6), (7, 0, 8))
    actual = isGoal(board)
    expected = False
    assert actual == expected


def testManhattenDistance():
    src = (1, 1)
    dest = (4, 4)
    actual = manhatten_distance(src, dest)
    expected = 6
    assert actual == expected


def testHeuristicFunction():
    board = ((1, 2, 3), (4, 5, 6), (7, 8, 0))
    actual = heuristicFn(board)
    expected = 0
    assert actual == expected

    board = ((1, 2, 3), (4, 0, 6), (7, 8, 5))
    actual = heuristicFn(board)
    expected = 4
    assert actual == expected

    board = ((1, 2, 3), (4, 5, 6), (7, 0, 8))
    actual = heuristicFn(board)
    expected = 2
    assert actual == expected


def testFindEmptyIndex():
    board = ((1, 2, 3), (4, 5, 6), (7, 8, 0))
    actual = findEmptyIndex(board)
    expected = (2, 2)
    assert actual == expected

    board = ((1, 2, 3), (4, 0, 6), (7, 8, 5))
    actual = findEmptyIndex(board)
    expected = (1, 1)
    assert actual == expected


def testIsValid():
    pos = (1, 1)
    actual = isValid(pos)
    expected = True
    assert actual == expected

    pos = (1, 3)
    actual = isValid(pos)
    expected = False
    assert actual == expected

    pos = (1, -1)
    actual = isValid(pos)
    expected = False
    assert actual == expected


def testPrint():
    board = ((1, 2, 3), (4, 5, 6), (7, 8, 0))
    print()
    printBoard(board)


def testAstar():
    board = ((1, 2, 3), (4, 5, 6), (7, 8, 0))
    actual, path = astar(board, successorsNinePuzzle, heuristicFn)
    expected = GOAL
    assert actual == expected

    board = ((1, 2, 3), (4, 5, 6), (7, 0, 8))
    actual, path = astar(board, successorsNinePuzzle, heuristicFn)
    expected = GOAL
    assert actual == expected

    board = ((1, 2, 3), (4, 0, 5), (7, 8, 6))
    actual, path = astar(board, successorsNinePuzzle, heuristicFn)
    expected = GOAL
    assert actual == expected
    print()
    for p in path:
        printBoard(p)
        print()


def testHardAstar():
    board = ((1, 2, 3), (4, 0, 6), (7, 8, 5))
    actual = astar(board, successorsNinePuzzle, heuristicFn)
    expected = None
    assert actual == expected
