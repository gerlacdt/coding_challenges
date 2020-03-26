"""Tower of Hanoi

Write a function that prints out all the steps necessary to complete
the Tower of Hanoi. You should assume that the rods are numbered, with
the first rod being 1, the second(auxiliary) rod being 2, and the
last (goal)rod being 3.

For example, with n = 3, we can do this in 7 moves:

Move 1 to 3
Move 1 to 2
Move 3 to 2
Move 1 to 3
Move 2 to 1
Move 2 to 3
Move 1 to 3
"""


def tower_of_hanoi(N=3):
    result = []

    def helper(n, src, auxiliary, target):
        if n > 0:
            helper(n - 1, src, target, auxiliary)
            result.append((src, target))
            helper(n - 1, auxiliary, src, target)

    helper(N, 1, 2, 3)
    return result


def test():
    actual = tower_of_hanoi()
    expected = [(1, 3), (1, 2), (3, 2), (1, 3), (2, 1), (2, 3), (1, 3)]
    assert actual == expected

    for move in expected:
        fromm, to = move
        print("Move {} to {}".format(fromm, to))
