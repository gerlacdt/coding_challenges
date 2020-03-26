"""You have a stack of boxes, with widths, heigths and depths. The
boxes can only be stacked on top of one another if each box in the
stack is strictly larger than the box above it width, height and
depth. Implement a method to build the tallest stack possible, where
the height of a stack is the sum of the heights of each box.
"""


from typing import List


class Box:
    def __init__(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth

    def isSmaller(self, other):
        if (self.width < other.width and self.height < other.height
            and self.depth < other.depth):
            return True
        return False

    def __str__(self):
        return "({} {} {})".format(self.width, self.height, self.depth)

    def __repr__(self):
        return "({} {} {})".format(self.width, self.height, self.depth)


def maxHeight(assignment: List[Box]):
    if not assignment:
        return 0
    # maxHeight is sum of all box heights
    return sum([b.height for b in assignment])


def findSuccessors(assignment: List[Box], boxes: List[Box]):
    """A successor is a pair of (newAssignment, leftBoxes)."""
    if not assignment:
        # one different box in all assignments (should be always possible)
        return [([b], boxes.copy() - set([b])) for b in boxes]
    else:
        successors = []
        lastBox = assignment[-1]
        for b in boxes:
            if b.isSmaller(lastBox):
                successors.append((assignment[:] + [b], boxes.copy() - set([b])))
        return successors


def findMaxStack(boxes):
    currentHeight = 0

    def helper(assignment, boxes):
        nonlocal currentHeight
        successors = findSuccessors(assignment, boxes)
        print("successors: {}".format(successors))

        if not successors:
            return assignment
        for s in successors:
            newAssignment, leftBoxes = s
            result = helper(newAssignment, leftBoxes)
            if maxHeight(result) > currentHeight:
                currentHeight = maxHeight(result)

        return None
    helper([], boxes)
    return currentHeight


def test():
    b1 = Box(1,1,1)
    b2 = Box(2,2,2)
    b3 = Box(3,3,3)
    boxes = set([b1, b2, b3])
    actual = findMaxStack(boxes)
    expected = 6
    assert actual == expected

    boxes = set([Box(1,1,1), Box(2,2,1), Box(1,2,2),
                 Box(3,2,2), Box(3,3,3), Box(4,3,3)
    ])
    actual = findMaxStack(boxes)
    expected = 6
    assert actual == expected
