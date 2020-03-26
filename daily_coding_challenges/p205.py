"""Good morning! Here's your coding interview problem for today.

This problem was asked by IBM.

Given an integer, find the next permutation of it in absolute
order. For example, given 48975, the next permutation would be 49578.

See:
https://www.geeksforgeeks.org/find-next-greater-number-set-digits/

"""


from collections import namedtuple


def toList(num):
    current = num
    arr = []
    while num:
        current = num % 10
        arr.append(current)
        num = num // 10
    return arr


def toNumber(lst):
    result = 0
    for i in range(len(lst)):
        result += lst[i]*(10**i)
    return result


def nextPermutation(num):
    arr = toList(num)
    if len(arr) == 1 or arr == list(sorted(arr)):
        raise RuntimeError("Length of 1 cannot have permutations or the highest value permutation has not successor")
    i = 1
    while True:
        if arr[i-1] < arr[i]:
            i += 1
            continue
        else:
            break
    # now i stands at the breaking index
    arr[i], arr[i-1] = arr[i-1], arr[i]
    result = list(sorted(arr[i-1::-1])) + arr[i:]
    print("result: {}".format(result))
    return toNumber(result)


def testToList():
    num = 48957
    actual = toList(num)
    expected = [7,5,9,8,4]
    assert actual == expected


def testToNumber():
    lst = [7,5,9,8,4]
    actual = toNumber(lst)
    expected = 48957
    assert actual == expected


def test():
    Case = namedtuple("Case", ["input", "expected"])
    cases = [
        Case(48975, 49578),
        Case(123, 132),
        Case(132, 213),
        Case(198765432, 213456789)
    ]
    for c in cases:
        actual = nextPermutation(c.input)
        assert actual == c.expected, "Case: {}".format(c)
