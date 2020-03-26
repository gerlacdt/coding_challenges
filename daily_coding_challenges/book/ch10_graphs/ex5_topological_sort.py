"""We are given a Hashmap associating each courseId kye with a list of
courseIds values, which tells that the prerequisites of courseId are
courseIds. Return a sorted ordering of courses such that we can
complete the curriculum.

Return null if there is no such ordering.


For example:

{
 "CS300": ["CS100", "CS200"],
 "CS200": ["CS100"],
 "CS100": [],
}

should return:

["CS100", "CS200", "CS300"]

"""

from collections import deque


def reverseEdges(graph):
    reversedGraph = {}
    for key, neighbors in graph.items():
        if key not in reversedGraph:
            reversedGraph[key] = []
        for n in neighbors:
            if n not in reversedGraph:
                reversedGraph[n] = []
            if key not in reversedGraph[n]:
                reversedGraph[n].append(key)
                reversedGraph[n].sort()
    return reversedGraph


def dfs(graph, startNodes):
    discovered = set()
    result = deque()

    def helper(node):
        nonlocal result
        for neighbor in graph[node]:
            if neighbor not in discovered:
                discovered.add(neighbor)
                helper(neighbor)
        result.appendleft(node)

    for node in startNodes:
        if node not in discovered:
            discovered.add(node)
            helper(node)
    return list(result)


def topologicalSort(graph):
    reversedGraph = reverseEdges(graph)
    # find start nodes
    startNodes = []
    for key, neighbors in graph.items():
        if not neighbors:
            startNodes.append(key)
    return dfs(reversedGraph, startNodes)


def testReversedEdges():
    graph = {"CS300": ["CS100", "CS200"], "CS200": ["CS100"], "CS100": []}
    actual = reverseEdges(graph)
    expected = {"CS100": ["CS200", "CS300"], "CS200": ["CS300"], "CS300": []}
    assert actual == expected


def test():
    graph = {"CS300": ["CS100", "CS200"], "CS200": ["CS100"], "CS100": []}
    actual = topologicalSort(graph)
    expected = ["CS100", "CS200", "CS300"]
    assert actual == expected


def testClothes():
    graph = {
        "underwear": ["trousers"],
        "trousers": ["jacket", "shoes"],
        "shirt": ["sweatshirt"],
        "sweatshirt": ["jacket"],
        "socks": ["shoes"],
        "jacket": ["shoes"],
    }
    actual = topologicalSort(reverseEdges(graph))
    expected = [
        "socks",
        "shirt",
        "sweatshirt",
        "underwear",
        "trousers",
        "jacket",
        "shoes",
    ]
    assert actual == expected
