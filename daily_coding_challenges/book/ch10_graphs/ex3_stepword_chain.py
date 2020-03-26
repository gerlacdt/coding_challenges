"""Given a start word, an end word, and a dictionary of valid
words,find the shortest transformation sequence from start to end such
that only one letter is changed at each step of the sequence, and each
transformed word exists in the dictionary. If there is no possible
transformation, return null. Each word in the dictionary has the same
length as start and end and is lowercase.

For example, given start = "dog", end = "cat", and dictionary =
{"dot", "dop", "dat", "cat"}, return ["dog", "dot", "dat", "cat"]

Given start = "dog", end = "cat", and dictionary = {"dot", "tod",
"dat", "dar"}, return null as tehre is no possible transformation from
"dot" to "cat".

"""

from collections import defaultdict, deque


class Graph:
    def __init__(self):
        self.data = defaultdict(set)

    def addEdge(self, src, dest):
        self.data[src].add(dest)
        self.data[dest].add(src)


def bfs(graph, start, end):
    frontier = deque([start])
    visited = set()
    parents = defaultdict(set)
    found = False
    while frontier:
        node = frontier.popleft()
        visited.add(node)
        for child in graph[node]:
            if child not in visited:
                frontier.append(child)
                parents[child] = node
                if child == end:
                    found = True
                    break
    if not found:
        return None
    # path is found, construct path from parents
    current = end
    path = deque([])
    while current:
        path.appendleft(current)
        current = parents[current]
    return list(path)


def createGraph(dictionary):
    length = len(dictionary)
    d = list(dictionary)
    graph = Graph()
    for i in range(length - 1):
        for j in range(i + 1, length):
            w1, w2 = d[i], d[j]
            diffCount = 0
            for k in range(len(w1)):
                if w1[k] != w2[k]:
                    diffCount += 1
            if diffCount == 1:
                graph.addEdge(w1, w2)
    return graph.data


def findStepwordChain(start, end, dictionary):
    graph = createGraph(dictionary)
    return bfs(graph, start, end)


def testCreateGraph():
    dictionary = {"dog", "dot", "dop", "dat", "cat"}
    actual = createGraph(dictionary)
    expected = {
        "dog": set(["dot", "dop"]),
        "dot": set(["dog", "dop", "dat"]),
        "dop": set(["dog", "dot"]),
        "dat": set(["dot", "cat"]),
        "cat": set(["dat"]),
    }
    assert actual == expected


def test():
    dictionary = {"dog", "dot", "dop", "dat", "cat"}
    start = "dog"
    end = "cat"
    actual = findStepwordChain(start, end, dictionary)

    # because the graph contains neighors as edges, the BFS search is
    # not deterministic. So we check here for both possible valid
    # paths
    expected1 = ["dog", "dot", "dat", "cat"]
    expected2 = ["dog", "dop", "dot", "dat", "cat"]
    assert actual == expected1 or actual == expected2


def testNegative():
    dictionary = {"dog", "dot", "tod", "dat", "dar"}
    start = "dog"
    end = "cat"
    actual = findStepwordChain(start, end, dictionary)
    assert not actual
