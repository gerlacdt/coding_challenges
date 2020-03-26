"""Good morning! Here's your coding interview problem for today.

This problem was asked by Dropbox.

Given an undirected graph G, check whether it is bipartite. Recall
that a graph is bipartite if its vertices can be divided into two
independent sets, U and V, such that no edge connects vertices of the
same set.
"""


from collections import deque


def successors(node, graph):
    return graph[node]


def toggle(color):
    return "BLUE" if color == "RED" else "RED"


def isBipartite(graph: dict):
    visited = set()
    frontier = deque([])
    colors = dict()
    for key in graph.keys():
        frontier.append(key)
        if key not in colors:
            colors[key] = "BLUE"
        while frontier:
            node = frontier.popleft()
            if node not in visited:
                visited.add(node)
                succs = successors(node, graph)
                for s in succs:
                    if s in colors and colors[s] == colors[node]:
                        print("{} is {} and successor {} is {}".format(node, colors[node], s, colors[s]))
                        return False
                    else:
                        frontier.append(s)
                        colors[s] = toggle(colors[node])
            else:
                continue
    return True


def test():
    graph = {"b1": ["r1", "r2"],
             "r1": ["b1", "b2"],
             "b2": ["r1", "r2"],
             "r2": ["b1", "b2", "b3"],
             "b3": ["r2", "r3"],
             "r3": ["b3"]}
    actual = isBipartite(graph)
    assert actual

    graph = {
        "b1": ["r1"],
        "r1": ["b2"],
        "b2": ["b1"],
    }
    actual = isBipartite(graph)
    assert not actual

    graph = {"b1": ["r1", "r2"],
             "r1": ["b1", "b2"],
             "b2": ["r1", "r2"],
             "r2": ["b1", "b2", "b3"],
             "b3": ["r2", "r3"],
             "r3": ["b3", "r2"],
    }
    actual = isBipartite(graph)
    assert not actual
