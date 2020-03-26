"""Good morning! Here's your coding interview problem for today.

This problem was asked by Twitter.

A classroom consists of N students, whose friendships can be
represented in an adjacency list. For example, the following descibes
a situation where 0 is friends with 1 and 2, 3 is friends with 6, and
so on.

{0: [1, 2],
 1: [0, 5],
 2: [0],
 3: [6],
 4: [],
 5: [1],
 6: [3]}

Each student can be placed in a friend group, which can be defined as
the transitive closure of that student's friendship relations. In
other words, this is the smallest set such that no student in the
group has any friends outside this group. For the example above, the
friend groups would be {0, 1, 2, 5}, {3, 6}, {4}.

Given a friendship list such as the one above, determine the number of
friend groups in the class.

"""


def successors(graph, node, visited):
    return [n for n in graph[node] if n not in visited]


def findConnectedComponents(graph):
    frontier = list(graph.keys())
    current = set()
    components = []
    visited = set()
    while frontier:
        node = frontier.pop()
        if node not in visited:
            current.add(node)
            visited.add(node)
            succs = successors(graph, node, visited)
            if not succs:
                components.append(current)
                current = set()
            else:
                frontier.extend(succs)
    return components


def test():
    graph = {0: [1, 2], 1: [0, 5], 2: [0], 3: [6], 4: [], 5: [1], 6: [3]}
    actual = findConnectedComponents(graph)
    expected = [{3, 6}, {0, 1, 2, 5}, {4}]
    assert actual == expected
