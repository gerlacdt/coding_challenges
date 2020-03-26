"""For a set of characters C and an integer k, a De Bruijn sequence is
a cyclic sequence in which every possible k-length string of
characters in C occurs exactly once.

For example, suppose C - {0, 1} and k = 3. Then our sequence should
contain the substrings {'000', '001', '010', '011', '100', '101',
'110', '111'}, and one possible solution would be 00010111.


Create an algorithm that find a De Bruijn sequence for a given C and
k.

"""

from itertools import product


def make_graph(C, k):
    vertices = product(C, repeat=k - 1)
    edges = {}
    for v in vertices:
        edges["".join(v)] = ["".join(v[1:]) + char for char in C]
    return edges


def find_eulerian_cycle(graph, start="01"):
    cycle = []
    before = after = []
    while graph:
        if cycle:
            start = next(vertex for vertex in cycle if vertex in graph)
            index = cycle.index(start)
            before = cycle[:index]
            after = cycle[index + 1 :]
        cycle = [start]
        prev = start
        while True:
            curr = graph[prev].pop()
            if not graph[prev]:
                graph.pop(prev)
            cycle.append(curr)
            if curr == start:
                break
            prev = curr
        cycle = before + cycle + after
    return cycle


def debruijn(C, k):
    graph = make_graph(C, k)
    cycle = find_eulerian_cycle(graph)
    return cycle


def test():
    C = set(["0", "1"])
    k = 3
    actual = debruijn(C, k)
    expected = ["01", "11", "11", "10", "01", "10", "00", "00", "01"]
    expected2 = ["01", "10", "00", "00", "01", "11", "11", "10", "01"]
    assert actual == expected or actual == expected2
