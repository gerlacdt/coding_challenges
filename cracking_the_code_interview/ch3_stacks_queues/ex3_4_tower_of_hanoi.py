"""
Tower of hanoi.
"""


def hanoi(n, from2, to, spare):
    moves = []

    def helper(n, from2, to, spare):
        if n <= 0:
            return None
        helper(n-1, from2, spare, to)
        moves.append((from2, to))
        print("Move {} to {}".format(from2, to))
        helper(n-1, spare, to, from2)
    helper(n, from2, to, spare)
    return moves


def test():
    # from=1, to=3, spare=2
    moves = hanoi(3, 1, 3, 2)
    expected = [(1, 3), (1,2), (3, 2), (1, 3),
                (2, 1), (2, 3), (1, 3)]
    assert moves == expected
