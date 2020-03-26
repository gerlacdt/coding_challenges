"""Play the game of Nim.

Given a list of non-zero starting values [a,b,c] and assuming optimal
play, determine whether the first player has a forced win.

"""


def update(heaps, pile, items):
    heaps = list(heaps)
    heaps[pile] -= items
    return tuple(heaps)


def get_moves(heaps):
    moves = []
    for pile, count in enumerate(heaps):
        for i in range(1, count + 1):
            moves.append(update(heaps, pile, i))
    return moves


def nim(heaps):
    print("nim({})".format(heaps))
    if heaps == (0, 0, 0):
        print("result: {}".format(True))
        return True

    moves = get_moves(heaps)
    result = any([not nim(move) for move in moves])
    print("result: {}".format(result))
    return result


def test():
    heaps = (0, 1, 0)
    actual = nim(heaps)
    expected = False
    assert actual == expected
    print("")

    heaps = (0, 1, 1)
    actual = nim(heaps)
    expected = True
    assert actual == expected
    print("")

    heaps = (1, 1, 1)
    actual = nim(heaps)
    expected = False
    assert actual == expected
    print("")
