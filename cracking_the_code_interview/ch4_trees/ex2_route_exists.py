"""Given a directed graph. Find out if there exist a route between
two nodes x and y.

A graph is a dictionary with node as key and adjacent nodes as values.

"""

from collections import deque


def dfs(graph, s):
    q = deque([s])
    visited = set()
    while q:
        node = q.popleft()
        if node not in visited:
            visited.add(node)
        for c in graph[node]:
            if c not in visited:
                q.append(c)
    return visited


def route_exists(graph, start, end):
    "Depth-First Search from x and y to find y or x respectively."
    return end in dfs(graph, start)


def test():
    graph = {'a': ['b'], 'b': []}
    result = route_exists(graph, 'a', 'b')
    assert result

    graph = {'a': ['c'], 'b': [], 'c': []}
    result = route_exists(graph, 'a', 'b')
    assert not result

    graph = {'a': ['b'], 'b': ['a', 'c', 'd'], 'c': ['d', 'e'], 'd': [], 'e': []}
    result = route_exists(graph, 'a', 'e')
    assert result

    result = route_exists(graph, 'c', 'd')
    assert result

    result = route_exists(graph, 'd', 'f')
    assert not result
