"""Given a stream of elements too large to store in memory, pick a
random element from the stream with uniform probability.

"""

import random


def pick(stream):
    random_element = None
    for i, e in enumerate(stream):
        if random.randint(1, i + 1) == 1:
            random_element = e

    return random_element


def test():
    arr = [i for i in range(100)]
    actual = pick(arr)
    assert actual or actual == 0
