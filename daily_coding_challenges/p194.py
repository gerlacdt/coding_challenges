"""Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Suppose you are given two lists of n points, one list p1, p2, ..., pn
on the line y = 0 and the other list q1, q2, ..., qn on the line y =
1. Imagine a set of n line segments connecting each point pi to
qi. Write an algorithm to determine how many pairs of the line
segments intersect.

"""

from collections import namedtuple


def intersectWithInclusion(seg1, seg2):
    if seg1[1] <= seg2[0] or seg2[1] <= seg1[0]:
        return False
    return True


def intersect(seg1, seg2):
    if ((seg1[0] > seg2[0] and seg1[0] < seg2[1]) or
        (seg1[1] > seg2[0] and seg1[1] < seg2[1])):
        return True
    return False


def countIntersections(ps, qs, intersectfn=intersect):
    if len(ps) != len(qs):
        raise RuntimeError("Number of elements of qs and ps must be equal")
    segments = []
    for seg in zip(ps, qs):
        if seg[0] > seg[1]:
            segments.append((seg[1], seg[0]))
        else:
            segments.append(seg)
    segments = sorted(segments)

    counter = 0
    for i in range(len(ps)-1):
        seg = segments[i]
        for j in range(i+1, len(ps)):
            seg2 = segments[j]
            if intersectfn(seg, seg2):
                counter += 1
    return counter


def test():
    Case = namedtuple("Case", ["input", "expected"])
    cases = [
        Case(((1, 4, 5), (4, 2, 3)), 2),
        Case(((1, 4, 5), (2, 3, 4)), 0)
    ]
    for c in cases:
        s1, s2 = c.input
        actual = countIntersections(s1, s2)
        assert actual == c.expected, "Case: {}".format(c)


def testWithInclusion():
    Case = namedtuple("Case", ["input", "expected"])
    cases = [
        Case(((1, 4, 5), (4, 2, 3)), 3),
        Case(((1, 4, 5), (2, 3, 4)), 0)
    ]
    for c in cases:
        s1, s2 = c.input
        actual = countIntersections(s1, s2, intersectWithInclusion)
        assert actual == c.expected, "Case: {}".format(c)


def testIntersect():
    Case = namedtuple("Case", ["input", "expected"])
    cases = [Case(((0, 5), (-1, 3)), True),
             Case(((1, 3), (3, 5)), False),
             Case(((2, 5), (-1, 1)), False),
             Case(((0, 3), (0, 5)), True),
             Case(((1, 4), (2, 4)), False)  # one segments include the other one
    ]
    for c in cases:
        s1, s2 = c.input
        actual = intersect(s1, s2)
        assert actual == c.expected, "Case: {}".format(c)


def testIntersectWithInclusion():
    Case = namedtuple("Case", ["input", "expected"])
    cases = [Case(((0, 5), (-1, 3)), True),
             Case(((1, 3), (3, 5)), False),
             Case(((2, 5), (-1, 1)), False),
             Case(((0, 3), (0, 5)), True),
             Case(((1, 4), (2, 4)), True)  # one segments include the other one
    ]
    for c in cases:
        s1, s2 = c.input
        actual = intersectWithInclusion(s1, s2)
        assert actual == c.expected, "Case: {}".format(c)
