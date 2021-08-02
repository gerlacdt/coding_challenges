"""

https://www.hackerrank.com/challenges/one-month-preparation-kit-zig-zag-sequence/problem

"""


def findZigZagSequence(a, n):
    a.sort()
    mid = int((n + 1) / 2) - 1  # changed
    a[mid], a[n - 1] = a[n - 1], a[mid]

    st = mid + 1
    ed = n - 2  # changed
    while st <= ed:
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed - 1  # changed
    return a


def test():
    actual = findZigZagSequence([1, 2, 3, 4, 5, 6, 7], 7)
    expected = [1, 2, 3, 7, 6, 5, 4]
    assert actual == expected
