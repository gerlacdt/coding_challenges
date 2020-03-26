"""
Shuffle a k-items deck.
"""

from random import randint
from collections import defaultdict
import pprint


def shuffle(k):
    arr = [i for i in range(1, k + 1)]
    result = []
    for _ in range(k):
        index = randint(0, len(arr) - 1)
        result.append(arr[index])
        arr.pop(index)
    return result


def shuffleWithSwaps(k):
    arr = [i for i in range(1, k + 1)]
    for i in range(k):
        index = randint(i, k - 1)
        arr[i], arr[index] = arr[index], arr[i]
    return arr


def statistics(n, k, fn=shuffle):
    stats = defaultdict(int)
    for _ in range(n):
        result = fn(k)
        stats[tuple(result)] += 1
    return stats


def testShuffle():
    k = 3
    actual = shuffle(k)
    expected = k  # no duplicates should exist
    assert len(set(actual)) == expected


def testShuffleWithSwaps():
    k = 3
    actual = shuffleWithSwaps(k)
    expected = k
    assert len(set(actual)) == expected


def testStatistics():
    stats = statistics(100000, 3)
    pprint.pprint(stats)


def testStatisticsWithSwaps():
    stats = statistics(100000, 3, shuffleWithSwaps)
    pprint.pprint(stats)
