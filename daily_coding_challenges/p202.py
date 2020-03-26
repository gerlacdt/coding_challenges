"""Good morning! Here's your coding interview problem for today.

This problem was asked by Palantir.

Write a program that checks whether an integer is a palindrome. For
example, 121 is a palindrome, as well as 888. 678 is not a
palindrome. Do not convert the integer into a string.

"""


from collections import namedtuple


def toDigits(n):
    current = n
    lst = []
    while current:
        lst.append(current % 10)
        current = current // 10
    return list(reversed(lst))


def isPalindrome(num: int) -> bool:
    lst = toDigits(num)
    i = 0
    j = len(lst) - 1
    while i <= j:
        if lst[i] == lst[j]:
            i += 1
            j -= 1
            continue
        else:
            return False
    return True


def test():
    Case = namedtuple("Case", ["input", "expected"])
    cases = [Case(888, True),
             Case(121, True),
             Case(678, False),
             Case(1, True),
             Case(12, False),
             Case(125521, True),
             Case(12521, True),
    ]
    for c in cases:
        actual = isPalindrome(c.input)
        assert actual == c.expected, "Case: {}".format(c)


def testToDigits():
    actual = toDigits(1234)
    expected = [1, 2, 3, 4]
    assert actual == expected

    actual = toDigits(1)
    expected = [1]
    assert actual == expected
