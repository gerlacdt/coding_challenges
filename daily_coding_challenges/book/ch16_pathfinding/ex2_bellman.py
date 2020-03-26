"""Given a table of exchange rates. Determine whether there is a
possible arbitrage opportunity. Find if there is some sequence of
trades you can make, starting with some amount X of any currency, so
that you can end up with some amount greater than X of that currency.

"""

import sys
import math


def toEdges(graph):
    edges = []
    for key, neighbors in graph.items():
        for n in neighbors:
            dest, cost = n
            edges.append((key, dest, cost))
    return edges


def currencyToEdges(graph):
    edges = []
    for key, neighbors in graph.items():
        for n in neighbors:
            dest, cost = n
            # we only handle sums for cost calculation but for currency exchange we need multiplication
            # log2 has the property: log2(a*b) = log2(a) + log2(b)
            # negate log2 to ensure that weights are positive
            currency_cost = -math.log2(cost)
            edges.append((key, dest, currency_cost))
    return edges


def bellman_ford(graph, start, convertEdges=toEdges):
    edges = convertEdges(graph)
    costs = {}
    parents = {}
    # init relax data structures
    for key in graph.keys():
        costs[key] = sys.maxsize
        parents[key] = None
    costs[start] = 0

    for i in range(len(graph) - 1):
        for edge in edges:
            orig, dest, weight = edge
            # relax
            if costs[dest] > costs[orig] + weight:
                costs[dest] = costs[orig] + weight
                parents[dest] = orig

    # iterate one more time, check if current minimums hold. Otherwise
    # there is a negative cycle
    for edge in edges:
        orig, dest, weight = edge
        if costs[dest] > costs[orig] + weight:
            return costs, parents, True
        return costs, parents, False


def testCurrency():
    graph = {
        "USD": [("GBP", 0.77), ("INR", 71.71), ("EUR", 0.87)],
        "GBP": [("USD", 1.30), ("INR", 93.55), ("EUR", 1.14)],
        "INR": [("USD", 0.014), ("GBP", 0.011), ("EUR", 0.012)],
        "EUR": [("USD", 1.14), ("GBP", 0.88), ("INR", 81.95)],
    }  # NO negative cycle
    costs, parents, hasCycle = bellman_ford(graph, "USD", currencyToEdges)
    assert not hasCycle

    graph = {
        "USD": [("GBP", 0.77), ("INR", 71.71), ("EUR", 0.87)],
        "GBP": [("USD", 1.30), ("INR", 93.55), ("EUR", 1.14)],
        "INR": [("USD", 0.014), ("GBP", 0.011), ("EUR", 0.012)],
        "EUR": [
            ("USD", 1.2),
            ("GBP", 0.88),
            ("INR", 81.95),
        ],  # negative cycle EUR -> USD
    }
    costs, parents, hasCycle = bellman_ford(graph, "USD", currencyToEdges)
    assert hasCycle

    graph = {"USD": [("EUR", 2)], "EUR": [("USD", 0.6)]}
    costs, parents, hasCycle = bellman_ford(graph, "USD", currencyToEdges)
    assert hasCycle


def testBellman():
    graph = {
        "s": [("t", 6), ("y", 7)],
        "t": [("x", 5), ("z", -4), ("y", 8)],
        "y": [("x", -3), ("z", 9)],
        "x": [("t", -2)],
        "z": [("s", 2), ("x", 7)],
    }
    costs, parents, hasCycle = bellman_ford(graph, "s")

    assert costs == {"s": 0, "t": 2, "y": 7, "x": 4, "z": -2}
    assert parents == {"s": None, "t": "x", "y": "s", "x": "y", "z": "t"}
    assert not hasCycle


def testHasCycle():
    # d -> a is negative but does not create a negative cycle
    graph = {"a": [("b", 2)], "b": [("c", 2)], "c": [("d", 2)], "d": [("a", -4)]}
    costs, parents, hasCycle = bellman_ford(graph, "a")
    assert costs == {"a": 0, "b": 2, "c": 4, "d": 6}
    assert parents == {"a": None, "b": "a", "c": "b", "d": "c"}
    assert not hasCycle

    # d -> a creates a negative cycle
    graph = {"a": [("b", 2)], "b": [("c", 2)], "c": [("d", 2)], "d": [("a", -7)]}
    costs, parents, hasCycle = bellman_ford(graph, "a")
    assert hasCycle
