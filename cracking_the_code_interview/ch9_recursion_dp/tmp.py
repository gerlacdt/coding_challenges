"""
REDO the n-queens problem.
"""


def isValid(this, other):
    # x-axis
    if this[0] == other[0]:
        return False

    # y-axis
    if this[1] == other[1]:
        return False

    # diagonal
    if abs(this[0] - other[0]) == abs(this[1] - other[1]):
        return False

    return True


def nqueens(assignment=[], N=8):
    results = []

    def helper(assignment, N):
        if len(assignment) == N:
            return assignment
        if not assignment:
            x = 0
        else:
            x, _ = assignment[-1]
        for y in range(N):
            newAssignment = (x+1, y)
            if all([isValid(newAssignment, a) for a in assignment]):
                assignment.append(newAssignment)
                r = helper(assignment[:], N)
                if r:
                    results.append(r)
                else:
                    assignment.pop()
        return None

    helper(assignment, N)
    return len(results)


def test():
    nresults = nqueens()
    assert nresults == 92
