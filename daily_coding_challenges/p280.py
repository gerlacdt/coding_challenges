"""Good morning! Here's your coding interview problem for today.

This problem was asked by Pandora.

Given an undirected graph, determine if it contains a cycle.

Attention for undirected graphs you need to exclude direct parents in
nyou cycle-detection algorithm.

"""

from collections import defaultdict


class DirectectedGraph:
    def __init__(self):
        self.graph = defaultdict(set)

    def addEdge(self, start, end):
        self.graph[start].add(end)
        if end not in self.graph:
            self.graph[end] = set()


def successors(graph, node):
    return [n for n in graph.graph[node]]


WHITE = 0
GRAY = 1
BLACK = 2


def hasCycle(graph):
    colors = dict()
    visited = set()
    cycle = False

    def helper(node):
        nonlocal cycle
        if node in visited:
            return
        colors[node] = GRAY
        visited.add(node)
        succs = successors(graph, node)
        for s in succs:
            if s not in visited:
                helper(s)
            elif colors[s] == GRAY:
                cycle = True
            else:
                raise RuntimeError(
                    "Different color expected: node:{} color: {}".format(s, colors[s])
                )
        colors[node] = BLACK

    for n in graph.graph.keys():
        colors[n] = WHITE
    for n in graph.graph.keys():
        helper(n)
    return cycle


def test():
    graph = DirectectedGraph()
    graph.addEdge(1, 2)
    graph.addEdge(2, 3)
    graph.addEdge(3, 4)
    graph.addEdge(3, 5)
    graph.addEdge(4, 1)
    actual = hasCycle(graph)
    expected = True
    assert actual == expected

    graph = DirectectedGraph()
    graph.addEdge(1, 2)
    graph.addEdge(2, 3)
    graph.addEdge(3, 4)
    graph.addEdge(3, 5)
    actual = hasCycle(graph)
    expected = False
    assert actual == expected


class UndirectedGraph:
    def __init__(self):
        self.graph = defaultdict(set)

    def addEdge(self, start, end):
        self.graph[start].add(end)
        self.graph[end].add(start)


def isCycleUndirected(graph):
    visited = set()
    stack = set()
    cycle = False

    def helper(node, parent):
        nonlocal cycle
        if node in visited:
            return
        stack.add(node)
        visited.add(node)
        succs = successors(graph, node)
        for s in succs:
            if s in stack and s != parent:
                cycle = True
                return
            if s not in visited:
                helper(s, node)
        stack.remove(node)

    for n in graph.graph.keys():
        helper(n, None)
    return cycle


def testUndirected():
    graph = UndirectedGraph()
    graph.addEdge(1, 2)
    graph.addEdge(2, 3)
    graph.addEdge(3, 4)
    graph.addEdge(3, 5)
    graph.addEdge(4, 1)
    actual = isCycleUndirected(graph)
    expected = True
    assert actual == expected

    graph = UndirectedGraph()
    graph.addEdge(1, 2)
    graph.addEdge(2, 3)
    graph.addEdge(3, 4)
    actual = isCycleUndirected(graph)
    expected = False
    assert actual == expected
