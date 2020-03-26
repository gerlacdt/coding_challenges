"""Implement the "paint fill" function. Give a screen, a point (X,Y)
with a color and a new color. Fill in the surrounding area and replace
all points of the old color with the new color.

Hint: DFS

"""


COLORS = ["RED", "GREEN", "BLUE"]


def neighbors(point):
    x, y = point
    return [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]


def paintfill(screen, point, color):
    x, y = point
    # visited = set()

    def helper(screen, point, oldColor, newColor):
        x, y = point  # for array screen it is [y][x] (y are rows, x are columns)
        if x < 0 or x >= len(screen[0]):
            return None
        if y < 0 or y >= len(screen):
            return None
        if screen[y][x] == oldColor:
            screen[y][x] = color
            for n in neighbors(point):
                # set not needed if you only recurse when you change the color a the current point
                # if n not in visited:
                #     visited.add(n)
                helper(screen, n, oldColor, newColor)

    return helper(screen, point, screen[y][x], color)


def test():
    screen = [
        ["RED", "RED", "RED", "GREEN", "GREEN"],
        ["BLUE", "BLUE", "RED", "GREEN", "GREEN"],
        ["BLUE", "BLUE", "RED", "RED", "RED"],
        ["BLUE", "BLUE", "RED", "RED", "RED"],
        ["BLUE", "BLUE", "RED", "RED", "RED"],
    ]
    expected  = [
        ["BLUE", "BLUE", "BLUE", "GREEN", "GREEN"],
        ["BLUE", "BLUE", "BLUE", "GREEN", "GREEN"],
        ["BLUE", "BLUE", "BLUE", "BLUE", "BLUE"],
        ["BLUE", "BLUE", "BLUE", "BLUE", "BLUE"],
        ["BLUE", "BLUE", "BLUE", "BLUE", "BLUE"],
    ]

    paintfill(screen, (2, 2), "BLUE")

    assert screen == expected
