"""Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given two rectangles on a 2D graph, return the area of their
intersection. If the rectangles don't intersect, return 0.

For example, given the following rectangles:

{
    "top_left": (1, 4),
    "dimensions": (3, 3) # width, height
}
and

{
    "top_left": (0, 5),
    "dimensions": (4, 3) # width, height
}
return 6.

"""


class Rectangle:
    def __init__(self, topLeft, dim):
        self.topLeft = topLeft
        self.dim = dim


def intersection(area1, area2):
    points1 = {(area1.topLeft[0] + i, area1.topLeft[1] + j) for i in range(area1.dim[0]) for j in range(area1.dim[1])}
    points2 = {(area2.topLeft[0] + i, area2.topLeft[1] + j) for i in range(area2.dim[0]) for j in range(area2.dim[1])}
    return len(points1 & points2)


def test():
    rec1 = Rectangle((1, 4), (3, 3))
    rec2 = Rectangle((0, 5), (4, 3))
    result = intersection(rec1, rec2)
    expected = 6
    assert result == expected

    rec1 = Rectangle((0,0), (4, 4))
    rec2 = Rectangle((0, 1), (4, 4))
    result = intersection(rec1, rec2)
    expected = 12
    assert result == expected
