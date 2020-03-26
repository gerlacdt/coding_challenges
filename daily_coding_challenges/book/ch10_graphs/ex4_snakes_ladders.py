"""Snakes and Ladders is a game played on a 10x10 board. The goal of
which is get from square 1 to square 100. On each turn players will
roll a six-sided die and move forward a number of spaces equal to the
result. If they land on a square that represents a snake or a ladder,
they will be transported ahead or behind, respectively, to a new
square.

Find the smallest number of turns it takes to play snakes and ladders.

Example:

snakes = {17: 13, 52: 29, 57: 40, 62: 22, 88: 18, 95: 51, 97: 79}
ladders = {3: 21, 8: 30, 28: 84, 58: 77, 75: 86, 80: 100, 90: 91}

"""

from collections import defaultdict, deque


def createGraph(snakes, ladders, N=100):
    d = defaultdict(set)
    for i in range(1, N + 1):
        for j in range(1, 7):
            if i + j <= N:
                if i + j in snakes:
                    d[i].add(snakes[i + j])
                elif i + j in ladders:
                    d[i].add(ladders[i + j])
                else:
                    d[i].add(i + j)
    return d


def bfs(graph, start=1, goal=100):
    frontier = deque([start])
    discovered = set([start])
    parents = {start: None}
    found = False
    while frontier:
        node = frontier.popleft()
        if node == goal:
            found = True
            break
        for child in graph[node]:
            if child not in discovered:
                frontier.append(child)
                discovered.add(child)
                parents[child] = node

    if not found:
        return None

    # construct path
    current = goal
    path = []
    while current:
        path.append(current)
        current = parents[current]
    return list(reversed(path))


def testCreateGraph():
    snakes = {7: 1, 11: 3}
    ladders = {6: 10}
    graph = createGraph(snakes, ladders, 18)
    # print(graph)


def test():
    snakes = {17: 13, 52: 29, 57: 40, 62: 22, 88: 18, 95: 51, 97: 79}
    ladders = {3: 21, 8: 30, 28: 84, 58: 77, 75: 86, 80: 100, 90: 91}
    graph = createGraph(snakes, ladders)
    actual = bfs(graph)
    expected = [1, 21, 22, 84, 89, 94, 100]
    assert actual == expected


def testHard():
    snakes = {17: 13, 52: 29, 57: 40, 62: 22, 88: 18, 95: 51, 97: 79}
    ladders = {3: 21, 8: 30, 28: 84, 58: 77, 75: 86, 80: 100, 90: 91, 9: 99}
    graph = createGraph(snakes, ladders)
    actual = bfs(graph)
    expected = [1, 4, 99, 100]
    assert actual == expected
