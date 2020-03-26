"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Amazon.

Given n numbers, find the greatest common denominator between them.

For example, given the numbers [42, 56, 14], return 14.

"""

from collections import namedtuple


def gcd(a, b):
    if a < b:
        a, b = b, a
    modulo = a % b
    if modulo == 0:
        return b
    return gcd(b, modulo)


def all_gcd(numbers):
    assert len(numbers) > 1
    result = gcd(numbers[0], numbers[1])
    for i in numbers[2:]:
        result = gcd(result, i)
    return result


def test():
    Case = namedtuple('Case', ['a', 'b', 'expected'])
    gcd_test_cases = [Case(32, 6, 2), Case(6, 2, 2),
                      Case(8, 3, 1), Case(23, 6, 1),
                      Case(3, 8, 1), Case(49, 56, 7),
                      Case(9, 9, 9), Case(5, 3, 1)]

    for t in gcd_test_cases:
        result = gcd(t.a, t.b)
        assert result == t.expected

    numbers = [42, 56, 14]
    result = all_gcd(numbers)
    expected = 14
    assert result == expected

    numbers = [8, 32, 128, 7, 64, 512]
    result = all_gcd(numbers)
    expected = 1
    assert result == expected

    numbers = [8, 32, 128, 64, 512]
    result = all_gcd(numbers)
    expected = 8
    assert result == expected
