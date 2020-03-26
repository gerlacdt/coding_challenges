"""Good morning! Here's your coding interview problem for today.

This problem was asked by Snapchat.

Given a list of possibly overlapping intervals, return a new list of
intervals where all overlapping intervals have been merged.

The input list is not necessarily ordered in any way.

For example, given [(1, 3), (5, 8), (4, 10), (20, 25)], you should
return [(1, 3), (4, 10), (20, 25)].

"""

from collections import namedtuple


def merge(interval1, interval2):
    """Merges the given two intervals."""
    min1, max1 = interval1
    min2, max2 = interval2
    return (min(min1, min2), max(max1, max2))


def isOverlapping(interval1, interval2):
    """Returns true if given intervals are overlapping. Otherwise returns
false. An interval is a tuple with 2 elements.
    """
    min1, max1 = interval1
    min2, max2 = interval2
    if (min1 < max2 and min1 > min2) or (min2 < max1 and min2 > min1):
        return True
    return None


def mergeIntervals(arrs):
    """Returns merged overlapped intervals of given array. An interval is
a 2-element tuple which describes a range. Tuple with overlapping
ranges will get merged to one tuple.
    """
    lst = sorted(arrs)
    result = []
    i = 0
    while i < len(lst):
        j = i
        tmp = lst[j]
        while (j+1 < len(lst) and isOverlapping(tmp, lst[j+1])):
            # print("tmp: {}, lst[{}]: {}".format(tmp, j+1, lst[j+1]))
            tmp = merge(tmp, lst[j+1])
            # print("after merge: tmp: {}".format(tmp))
            j += 1
        i = j+1
        result.append(tmp)
    return result


def test():
    Case = namedtuple('Case', ['input1', 'expected'])
    cases = [Case([(1, 3), (5, 8), (4, 10), (20, 25)], [(1, 3), (4, 10), (20, 25)]),
             Case([(1, 3), (2, 4), (5, 7), (6, 8)], [(1, 4), (5, 8)]),
             Case([(1, 3), (2, 5), (4, 10), (9, 15)], [(1, 15)]),
             Case([(6, 8), (1, 9), (2, 4), (4, 7)], [(1, 9)])]

    for c in cases:
        result = mergeIntervals(c.input1)
    assert result == c.expected
