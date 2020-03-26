"""Queens problem:

Print all way of arranging eight queens on an 8x8 chess board so that
none attack each other. Consider vertical, horizonal and diagonal line.

"""

from collections import namedtuple

Point = namedtuple("Point", ["X", "Y"])


def isValid(q1, q2):
    result = False
    if q1.X == q2.X or q1.Y == q2.Y or abs(q1.X - q2.X) == abs(q1.Y - q2.Y):
        result = False
    else:
        result = True
    return result


def successors(board, dim):
    results = []
    for y in range(dim):
        if not board:
            results.append([Point(0, y)])
        else:
            if all([isValid(p, Point(len(board), y)) for p in board]):
                results.append(board[:] + [Point(len(board), y)])
    return results


def nqueens(n=8):
    results = []

    def helper(index, board):
        if index >= n:
            return
        for succ in successors(board, n):
            if len(succ) == n:
                results.append(succ)
            else:
                helper(index+1, succ)

    helper(0, [])
    return results


def test():
    actual = nqueens(8)
    expected = 92
    assert len(actual) == expected


def testSucc():
    board = [Point(0, 1), Point(X=1, Y=3)]
    actual = successors(board, 4)
    expected = [[Point(X=0, Y=1), Point(X=1, Y=3), Point(X=2, Y=0)]]
    assert actual == expected


# solution from aima with backtracking


def isAttacked(s1, s2):
    """Returns true if the two given queens placements attack each
other. Otherwise returns false."""
    x1, y1 = s1
    x2, y2 = s2

    if x1 == x2:
        return True

    if y1 == y2:
        return True

    if abs(x1 - x2) == abs(y1 - y2):
        return True

    return False


# backtracking for constraint satisfaction problems (csp)
# 8-queens
def nqueensBacktracking(assignment=[], N=8):
    results = []

    def helper(assignment, N):
        if len(assignment) == N:  # 8 queens problem
            return assignment

        # from current assignment select new column to place (x, y)
        if not assignment:
            x = -1
        else:
            x, _ = assignment[-1]

        for y in range(8):
            a = (x+1, y)
            valid = all([not isAttacked(a, q) for q in assignment])
            if valid:
                assignment.append(a)
                result = helper(assignment[:], N)  # shallow-copy assignment necessary
                if result:
                    # return result  # break if we found single result and return it
                    results.append(assignment) # collect all results
                assignment = assignment[:-1]  # undo last assignment
        return None

    helper(assignment, N)
    return results


def testBacktracking():
    actual = nqueensBacktracking()
    expected = 92
    assert len(actual) == expected
