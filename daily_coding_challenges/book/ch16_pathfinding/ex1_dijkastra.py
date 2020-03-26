"""A network consists of nodes labeled 0 to n. You are given a list of
edges (a,b,t), describing the time t in seconds it takes for a message
to be sent from node a to node b. Whenever a node receives a message,
it immediately  passes the message on to a neighboring node, if possible.

Assumunig all nodes are connected, determine how long it will take for
every node to receive a message that begins at node 0.  """

from collections import defaultdict
from heapq import heappop, heappush


def createGraph(edges):
    graph = defaultdict(list)
    for e in edges:
        orig, dest, cost = e
        graph[orig].append((dest, cost))
    return graph


def successors(graph, node):
    total_cost, key = node
    succs = []
    for s in graph[key]:
        key, cost = s
        succs.append((cost + total_cost, key))
    return succs


def findRoute(edges, start):
    graph = createGraph(edges)
    frontier = [(0, start)]
    costs = {start: 0}
    parents = {start: None}
    while frontier:
        _, key = node = heappop(frontier)
        succs = successors(graph, node)
        for s in succs:
            cost, succ_key = s
            # relax
            if succ_key not in costs or cost < costs[succ_key]:
                heappush(frontier, s)
                costs[succ_key] = cost
                parents[succ_key] = key
    # print("costs: {}".format(costs))
    # print("parents: {}".format(parents))
    return max(costs.values())


def testFindRoute():
    # n = 5
    edges = [
        (0, 1, 5),
        (0, 2, 3),
        (0, 5, 4),
        (1, 3, 8),
        (2, 3, 1),
        (3, 5, 10),
        (3, 4, 5),
    ]

    actual = findRoute(edges, 0)
    expected = 9
    assert actual == expected


def testCreateGraph():
    edges = [
        (0, 1, 5),
        (0, 2, 3),
        (0, 5, 4),
        (1, 3, 8),
        (2, 3, 1),
        (3, 5, 10),
        (3, 4, 5),
    ]
    actual = createGraph(edges)
    expected = {
        0: [(1, 5), (2, 3), (5, 4)],
        1: [(3, 8)],
        2: [(3, 1)],
        3: [(5, 10), (4, 5)],
    }
