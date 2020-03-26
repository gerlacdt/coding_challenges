"""You are given a string of length n and an integer k. The string
can be manipulated by taking one of the first k letters and moving it
to the end of the string.

Write a program to determine the lexicographically smallest string
that can be created after an unlimited number of moves.

"""


def smallestRotation(word, k=1):
    if k == 1:
        minimum = word
        n = len(word)
        for i in range(n):
            if word[i:] + word[:i] < minimum:
                minimum = word[i:] + word[:i]
        return minimum
    else:
        # for k > 1, it is possible to sort the array. Hence the
        # sorted array is the smallest rotation
        return "".join(sorted(word))


def test():
    word = "BCABDADAB"
    actual = smallestRotation(word)
    expected = "ABBCABDAD"
    assert actual == expected

    word = "BCABDADAB"
    actual = smallestRotation(word, 2)
    expected = "".join(sorted(word))
    assert actual == expected

    word = "bcdefa"
    expected = "abcdef"
    actual = smallestRotation(word)
    assert actual == expected

    word = ""
    expected = ""
    actual = smallestRotation(word)
    assert actual == expected

    word = ""
    expected = ""
    actual = smallestRotation(word, 3)
    assert actual == expected
