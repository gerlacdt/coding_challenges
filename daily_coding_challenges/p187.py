"""Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

You are given given a list of rectangles represented by min and max x-
and y-coordinates. Compute whether or not a pair of rectangles overlap
each other. If one rectangle completely covers another, it is
considered overlapping.

For example, given the following rectangles:

{
    "top_left": (1, 4),
    "dimensions": (3, 3) # width, height
},
{
    "top_left": (-1, 3),
    "dimensions": (2, 1)
},
{
    "top_left": (0, 5),
    "dimensions": (4, 3)
}
return true as the first and third rectangle overlap each other.

"""


class Rectangle:

    def __init__(self, topLeft, dimensions):
        self.topLeft = topLeft
        self.dimensions = dimensions
        self.lowRight = (topLeft[0]+dimensions[0]-1, topLeft[1]+dimensions[1]-1)
        self.xrange = tuple(sorted([topLeft[0], self.lowRight[0]]))
        self.yrange = tuple(sorted([topLeft[1], self.lowRight[1]]))

    def intersects(self, other):
        if (other.xrange[0] <= self.xrange[0] <= other.xrange[1] or
            other.xrange[0] <= self.xrange[1] <= other.xrange[1]):
            return True
        return False


def overlap(rectangles):
    interset = set()
    for r in rectangles:
        for x in range(r.topLeft[0], r.topLeft[0] + r.dimensions[0]):
            for y in range(r.topLeft[1], r.topLeft[1] + r.dimensions[1]):
                if (x, y) in interset:
                    return True # one coordinate overlaps
                interset.add((x, y))
    return False


def overlap2(rectangles):
    for i in range(len(rectangles)):
        for j in range(i+1, len(rectangles)):
            if rectangles[i].intersects(rectangles[j]):
                return True
    return False


def test():
    r1 = Rectangle((1, 4), (3, 3))
    r2 = Rectangle((-1, 3), (2, 1))
    r3 = Rectangle((0, 5), (4, 3))
    rectangles = [r1, r2, r3]
    result = overlap(rectangles)
    assert result
    assert result == overlap2(rectangles)

    r1 = Rectangle((0,0), (3, 3))
    r2 = Rectangle((4,4), (3, 3))
    rectangles = [r1,  r2]
    result = overlap(rectangles)
    assert not result
    assert result == overlap2(rectangles)


def test2():
    r1 = Rectangle((1, 4),  (3, 3))
    r2 = Rectangle((-1, 3),  (2, 1))
    r3 = Rectangle((0, 5),  (4, 3))
    assert not r1.intersects(r2)
    assert r1.intersects(r3)
    assert not r2.intersects(r1)
    assert r3.intersects(r1)

    r4 = Rectangle((0, 0),  (3, 3))
    r5 = Rectangle((5, 0),  (3, 3))
    assert not r4.intersects(r5)
