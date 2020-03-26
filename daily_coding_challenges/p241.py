"""Good morning! Here's your coding interview problem for today.

This problem was asked by Palantir.

In academia, the h-index is a metric used to calculate the impact of a
researcher's papers. It is calculated as follows:

A researcher has index h if at least h of her N papers have h
citations each. If there are multiple h satisfying this formula, the
maximum is chosen.

For example, suppose N = 5, and the respective citations of each paper
are [4, 3, 0, 1, 5]. Then the h-index would be 3, since the researcher
has 3 papers with at least 3 citations.

Given a list of paper citations of a researcher, calculate their
h-index.

"""


def hIndex(arr):
    n = len(arr)
    hmax = 0  # there are not negative citations
    arr = sorted(arr)
    for i in range(n):
        if n - i >= arr[i]:
            hmax = arr[i]
    return hmax


def test():
    arr = [4, 3, 0, 1, 5]
    actual = hIndex(arr)
    expected = 3
    assert actual == expected

    arr = [4, 3, 0, 1, 5, 5, 5]
    actual = hIndex(arr)
    expected = 4
    assert actual == expected

    arr = [4, 5, 5, 0, 1, 5, 5, 5]
    actual = hIndex(arr)
    expected = 5
    assert actual == expected
