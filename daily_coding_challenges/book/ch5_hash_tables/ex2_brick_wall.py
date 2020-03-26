"""A wall consists of several rows of bricks of various integer
lengths and uniform heights. Your goal is to find a vertical line
going from the top to the bottom of the wall that cuts through the
fewest number of bricks. If the line goes through the edge between two
bricks, this does not count as a cut.

For example, suppose the input is as follows, where values in each row
represent the lengths of bricks in that row:

[
[3,5,1,1],
[2,3,3,2],
[5,5],
[4,4,2],
[1,3,3,3],
[1,1,6,1,1],
]

This would look like this:

a row has width 10, there are 6 rows.
        this column is best:
        |
        v

   |    |||
  |  |  | |
     |    |
    |   | |
 |  |  |  |
 ||     |||

"""


from collections import defaultdict


def brickWalls(rows):
    results = defaultdict(list)
    # find out the max with of the wall
    # expected that all rows have the same width
    maxrange = max([sum(r) for r in rows])
    for i, row in enumerate(rows):
        index = 0
        for width in row:
            index += width
            results[index].append(i)

    # do not consider end of wall because it does not count as a cut
    maxresult = max([len(lst) for key, lst in results.items() if key != maxrange])

    # result is where most of the bricks end or share a column
    # to calculate how many bricks are crossed we need the total
    # amount of rows subtracted by the rows which do not result in a
    # vertical cut
    return len(rows) - maxresult


def test():
    rows = [
        [3,5,1,1],
        [2,3,3,2],
        [5,5],
        [4,4,2],
        [1,3,3,3],
        [1,1,6,1,1],
    ]

    actual = brickWalls(rows)
    expected = 2
    assert actual == expected

    rows = [
        [3,5,1,1],
        [2,3,3,2],
        [5,3,2],
        [4,4,2],
        [1,3,4,2],
        [1,1,6,1,1],
    ]

    actual = brickWalls(rows)
    expected = 0
    assert actual == expected
