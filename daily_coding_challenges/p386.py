"""Good morning! Here's your coding interview problem for today.

This problem was asked by Twitter.

Given a string, sort it in decreasing order based on the frequency of
characters. If there are multiple possible solutions, return any of
them.

For example, given the string tweet, return tteew. eettw would also be
acceptable.

"""

from collections import defaultdict


def sortFrequencyChar(word):
    d = defaultdict(int)
    for c in word:
        d[c] += 1

    lst = []
    for c, count in d.items():
        lst.append((count, c))

    return "".join(pair[0] * pair[1] for pair in sorted(lst, reverse=True))


def test():
    word = "tweet"
    actual = sortFrequencyChar(word)
    expected = "tteew"
    assert actual == expected
