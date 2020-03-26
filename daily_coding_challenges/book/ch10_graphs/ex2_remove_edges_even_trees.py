"""Your are given a tree with an even number of nodes. Consider each
connection between parent and child to be an "edge". You would like to
remove some of these edges, such that the disconnected subtrees that
remain each have an even number of nodes.


For example, suppose your input is the following tree:


     1
   /  \
  2    3
     /  \
    4    5
   /|\
  6 7 8

In this case, if we remove the edge (3,4), both resulting subtrees
will be even.


Write a function that returns the maximum number of edges you can
remove while still satisfying this requirement.

"""


def countDescendents(graph, start):
    descendents = {}

    def helper(node):
        num_descendents = 0
        for child in graph[node]:
            num_descendents += helper(child)
        descendents[node] = num_descendents
        return num_descendents + 1

    helper(start)
    return descendents


def edgesToRemove(graph, start):
    descendents = countDescendents(graph, start)
    return [
        (key, val) for key, val in descendents.items() if key != start and val % 2 != 0
    ]


def testDescendents():
    graph = {1: [2, 3], 2: [], 3: [4, 5], 4: [6, 7, 8], 5: [], 6: [], 7: [], 8: []}
    start = 1
    actual = countDescendents(graph, start)
    expected = {2: 0, 6: 0, 7: 0, 8: 0, 4: 3, 5: 0, 3: 5, 1: 7}
    assert actual == expected


def test():
    graph = {1: [2, 3], 2: [], 3: [4, 5], 4: [6, 7, 8], 5: [], 6: [], 7: [], 8: []}
    start = 1
    actual = edgesToRemove(graph, start)
    expected = 2
    assert len(actual) == expected
