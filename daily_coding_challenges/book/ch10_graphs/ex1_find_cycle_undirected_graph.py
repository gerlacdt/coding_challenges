"""Given an undirectd graph. Find out if their is a cycle.

"""


class Graph:
    def __init__(self):
        self.data = {}

    def addEdge(self, src, target):
        if src not in self.data:
            self.data[src] = []
        self.data[src].append(target)

        if target not in self.data:
            self.data[target] = []
        self.data[target].append(src)

    def __str__(self):
        return "{}".format(self.data)


def hasCycle(graph):
    visited = set()

    def helper(node, parent):
        visited.add(node)
        for neighbor in graph.data[node]:
            if neighbor not in visited:
                helper(neighbor, node)
            else:
                if neighbor != parent:
                    return True

    for n, neighbors in graph.data.items():
        if n not in visited:
            if helper(n, None):
                return True

    return False


def testWithCycle():
    graph = Graph()
    graph.addEdge(1, 2)
    graph.addEdge(2, 3)
    graph.addEdge(3, 4)
    graph.addEdge(4, 1)
    graph.addEdge(5, 6)
    actual = hasCycle(graph)
    expected = True

    assert actual == expected


def testNoCycle():
    graph = Graph()
    graph.addEdge(1, 2)
    graph.addEdge(2, 3)
    graph.addEdge(3, 4)
    graph.addEdge(5, 6)
    actual = hasCycle(graph)
    expected = False

    assert actual == expected
