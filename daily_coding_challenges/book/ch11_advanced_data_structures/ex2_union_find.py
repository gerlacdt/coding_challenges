"""
Union find data structure.
"""


class DisjointSet:
    def __init__(self, graph):
        self.count = len(graph)
        self.graph = graph
        self.parents = {key: key for key in graph.keys()}
        self.sizes = [1 for key in graph.keys()]
        for key, items in self.graph.items():
            for item in items:
                self.union(key, item)

    def union(self, a, b):
        r1, r2 = self.find(a), self.find(b)
        if r1 == r2:
            return
        if self.sizes[r1] < self.sizes[r2]:
            self.sizes[r2] += self.sizes[r1]
            self.parents[r1] = r2
        else:
            self.sizes[r1] += self.sizes[r2]
            self.parents[r2] = r1

        self.count -= 1

    def find(self, key):
        current = key
        p = self.parents[current]
        while current != p:
            tmp = self.parents[p]
            current = p
            p = tmp
        # path compression, assign key to the correct group
        # now it is easier to construct the node-sets which form the connected components
        self.parents[key] = p
        return p

    def getConnectedComponents(self):
        connectedComponents = {}
        for p in self.parents.values():
            if p not in connectedComponents:
                connectedComponents[p] = {
                    key for key, p1 in self.parents.items() if p1 == p
                }
        return connectedComponents


def test():
    graph = {0: [1, 2], 1: [0, 5], 2: [0], 3: [6], 4: [], 5: [1], 6: [3]}
    disjointSet = DisjointSet(graph)
    connectedComponents = disjointSet.getConnectedComponents()
    actual = disjointSet.count
    expected = 3
    expectedComponents = {0: {0, 1, 2, 5}, 3: {3, 6}, 4: {4}}
    assert actual == expected
    assert connectedComponents == expectedComponents


def connectedComponents(graph):
    components = []
    discovered = set()
    current = set()

    def dfs(node):
        discovered.add(node)
        current.add(node)
        for neighbor in graph[node]:
            if neighbor not in discovered:
                dfs(neighbor)

    for node in graph.keys():
        if node not in discovered:
            dfs(node)
            components.append(current)
            current = set()

    return components


def testConnectedComponents():
    graph = {0: [1, 2], 1: [0, 5], 2: [0], 3: [6], 4: [], 5: [1], 6: [3]}
    actual = connectedComponents(graph)
    expected = [{0, 1, 2, 5}, {3, 6}, {4}]
    assert actual == expected
