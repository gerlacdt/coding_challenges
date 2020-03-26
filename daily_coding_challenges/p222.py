"""Good morning! Here's your coding interview problem for today.

This problem was asked by Quora.

Given an absolute pathname that may have . or .. as part of it, return
the shortest standardized path.

For example, given "/usr/bin/../bin/./scripts/../", return "/usr/bin/".

"""

import pytest


def shortestPathname(path):
    words = path.split("/")
    result = []
    for w in words:
        if w == "..":
            result.pop()
        elif w == "." or not w:
            continue
        else:
            result.append(w)
    shortestPath = "/".join(result)
    if len(shortestPath) > 0:
        return "/" + "/".join(result) + "/"
    else:
        return "/"


def test():
    path = "/usr/bin/../bin/./scripts/../"
    expected = "/usr/bin/"
    actual = shortestPathname(path)
    assert actual == expected

    path = "/usr/bin/../../../bin/"
    with pytest.raises(IndexError) as excinfo:
        actual = shortestPathname(path)
        print(actual)
    assert str(excinfo.value) == "pop from empty list"

    path = "/usr/bin/../../"
    expected = "/"
    actual = shortestPathname(path)
    assert actual == expected
