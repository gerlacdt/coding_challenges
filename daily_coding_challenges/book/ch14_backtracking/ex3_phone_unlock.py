"""One way to unlock you phone is by swiping in a specific patten
across a 1 - 9 keypad.

1 2 3
4 5 6
7 8 9

For a pattern to be valid, it must satisfy the following criteria:

- All of its keys must be distinct

- It must not connect two keys by jumping over a third key, unless
  that key has already been used.

For example:

4,2,1,7 is a valid pattern, whereas 2,1,7 is not.

Find the total number of valid unlock patterns of length n, where 1 <= n <= 9.

"""

from collections import namedtuple

KEYPAD = {
    1: [2, 4, 5],
    2: [1, 3, 4, 5, 6],
    3: [2, 5, 6],
    4: [1, 2, 4, 7, 8],
    5: [1, 2, 3, 4, 6, 7, 8, 9],
    6: [2, 3, 5, 8, 9],
    7: [4, 5, 8],
    8: [4, 5, 6, 7, 9],
    9: [5, 6, 8],
}


def isNeighbor(visited, num):
    last_num = visited[-1]
    direct_neighbors = set(KEYPAD[last_num])
    # direct neighbors
    if num in direct_neighbors:
        return True

    # indirect neighbors
    visited_neighbors = direct_neighbors & set(visited)
    for vn in visited_neighbors:
        if num in KEYPAD[vn]:
            return True

    return False


def isValid(assignment):
    if len(assignment) == 1:
        return True
    num = assignment[-1]
    visited = assignment[:-1]
    if num in visited:
        return False
    if isNeighbor(visited, num):
        return True
    return False


def backtracking(n, assignment=[]):
    if len(assignment) == n:
        return [assignment[:]]
    results = []
    for i in range(1, 10):
        assignment.append(i)
        if isValid(assignment):
            sol = backtracking(n, assignment)
            results.extend(sol)
        assignment.pop()
    return results


Case = namedtuple("Case", ["input", "expected"])


def testIsValid():
    cases = [Case([4, 2, 1, 7], True), Case([2, 1, 7], False)]
    for c in cases:
        actual = isValid(c.input)
        assert actual == c.expected


def test():
    cases = [Case(2, 39), Case(3, 214), Case(4, 1104)]
    for c in cases:
        actual = backtracking(c.input)
        assert len(actual) == c.expected
