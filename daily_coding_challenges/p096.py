"""Good morning! Here's your coding interview problem for today.

This problem was asked by Microsoft.

Given a number in the form of a list of digits, return all possible
permutations.

For example, given [1,2,3], return
[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]].

"""


def permutations(lst):
    if not lst:
        return [[]]
    else:
        result = []
        for i in range(len(lst)):
            h = lst[i]
            rest = lst[:i] + lst[i+1:]
            for p in permutations(rest):
                result.append([h] + p)
        return result


def test():
    input1 = [1, 2, 3]
    expected = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2],
                [3, 2, 1]]
    result = permutations(input1)
    assert result == expected

    input1 = []
    expected = [[]]
    result = permutations(input1)
    assert result == expected

    input1 = [1]
    expected = [[1]]
    result = permutations(input1)
    assert result == expected
