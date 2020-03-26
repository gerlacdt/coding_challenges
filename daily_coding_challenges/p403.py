"""Good morning! Here's your coding interview problem for today.

This problem was asked by Two Sigma.

Using a function rand5() that returns an integer from 1 to 5
(inclusive) with uniform probability, implement a function rand7()
that returns an integer from 1 to 7 (inclusive).

"""


from random import randint
from collections import defaultdict


def rand5():
    return randint(1, 5)


def rand7():
    i = rand5()
    j = rand5()
    table = [
        [1, 2, 3, 4, 5],
        [6, 7, 1, 2, 3],
        [4, 5, 6, 7, 1],
        [2, 3, 4, 5, 6],
        [7, None, None, None, None],
    ]

    while not table[i - 1][j - 1]:
        # do sth.
        i = rand5()
        j = rand5()
    return table[i - 1][j - 1]


def test():
    frequencies = defaultdict(int)
    for i in range(10000):
        # actual = rand7()
        actual = rand7()
        frequencies[actual] += 1
        assert actual >= 1 and actual <= 7
    print(frequencies)
