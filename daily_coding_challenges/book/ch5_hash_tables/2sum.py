"""Given a list of numbers and a number k, return whether any two
numbers from the list add up to k.

For example, given [10,15,3,7] and k=17, we should return True, since
10 + 7 = 17
"""


def two_sum(arr, k):
    seen = set()
    for v in arr:
        if v in seen:
            return True
        seen.add(k-v)
    return False


def test():
    arr = [10, 15, 3, 7]
    actual = two_sum(arr, 17)
    assert actual

    arr = [5]
    actual = two_sum(arr, 10)
    assert not actual
