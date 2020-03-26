"""A Markov chain can be thought of as a descritpiton of how likely
some events are to follow others. More mathematically, it describes
the probabilities associated with a given state transitioning to any
other state.

For example, let's say the transition probabilities are as follows:

see test

This indicates that if we begin with state a, after one step there is
90% chance the state will continue to bea, a 7.5% chance the state
will change to b, and a 2.5% chance the state will change to c.

Suppose you are given a starting state start, a list of transition
probabilities such as the one above, and a number of steps
num_steps. Run the associated Markov chain starting from start for
num_steps steps and compute the number of times each state is visited.

For num_steps=5000, one instance of running this particular Markov chain might produce:
{"a": 3012, "b":1656, "c":332}

"""

from random import random
from collections import defaultdict


def select(probabilities, node):
    return random()


def createTable(probabilities):
    table = defaultdict(list)
    for item in probabilities:
        src, dest, p = item
        if not table[src]:
            table[src].append((dest, p))
        else:
            _, last_p = table[src][-1]
            table[src].append((dest, p + last_p))
    return table


def markovChain(probabilities, start, num_steps=5000):
    stats = defaultdict(int)
    table = createTable(probabilities)
    current = start
    stats[current] += 1
    for _ in range(num_steps):
        r = random()
        for item in table[current]:
            val, acc = item
            if r < acc:
                current = val
                stats[current] += 1
                break
    return stats


def test():
    ps = [
        ("a", "a", 0.9),
        ("a", "b", 0.075),
        ("a", "c", 0.025),
        ("b", "a", 0.15),
        ("b", "b", 0.8),
        ("b", "c", 0.05),
        ("c", "a", 0.25),
        ("c", "b", 0.25),
        ("c", "c", 0.5),
    ]

    actual = markovChain(ps, "a", 5000)
    assert actual["a"] > 2900
    assert actual["b"] > 1500
    assert actual["c"] > 200
