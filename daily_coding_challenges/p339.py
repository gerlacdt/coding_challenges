"""Good morning! Here's your coding interview problem for today.

This problem was asked by Microsoft.

Given an array of numbers and a number k, determine if there are three
entries in the array which add up to the specified number k. For
example, given [20, 303, 3, 4, 25] and k = 49, return true as 20 + 4 +
25 = 49.

"""


def sum2(numbers, k):
    rests = set()
    for num in numbers:
        rest = k - num
        if num in rests:
            return sorted([rest, k - rest])
        rests.add(rest)
    return None


def sum3(numbers, k):
    for i in range(len(numbers)):
        rest = k - numbers[i]
        result = sum2(numbers[:i] + numbers[i + 1 :], rest)
        if result:
            return sorted([numbers[i], result[0], result[1]])
    return None


def test():
    numbers = [20, 303, 3, 4, 25]
    k = 49
    actual = sum3(numbers, k)
    expected = [4, 20, 25]
    assert actual == expected


def test2():
    numbers = [1, 2, 3, 4, 5, 6, 7]
    k = 16
    actual = sum3(numbers, k)
    expected = [3, 6, 7]
    assert actual == expected


def testNegative():
    numbers = [1, 4, 5, 6, 7]
    k = 3
    actual = sum3(numbers, k)
    expected = None
    assert actual == expected


def test2sum():
    numbers = [20, 303, 3, 4, 25]
    k = 45
    actual = sum2(numbers, k)
    expected = [20, 25]
    assert actual == expected
