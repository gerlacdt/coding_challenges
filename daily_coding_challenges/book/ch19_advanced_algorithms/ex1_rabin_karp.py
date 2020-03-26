"""Given a string and a pattern, find the starting indices of all
occurrences of the pattern in the string.. For example, given the
string 'abracadabra' and the pattern 'abr', you should return [0, 7]

"""


def toHash(c):
    return hash(c)


def find(string, pattern):
    if not pattern:
        return []
    n = len(string)
    k = len(pattern)

    resultHash = sum([toHash(c) for c in pattern])
    currentHash = sum([toHash(c) for c in string[:k]])
    result = []

    for i in range(n - k + 1):
        if currentHash == resultHash and string[i : i + k] == pattern:
            result.append(i)
        currentHash -= toHash(string[i])
        currentHash += toHash(string[i + k - 1])

    return result


def test():
    string = "abracadabra"
    pattern = "abr"
    actual = find(string, pattern)
    expected = [0, 7]
    assert actual == expected

    string = "aabaaa"
    pattern = "aa"
    actual = find(string, pattern)
    expected = [0, 3, 4]
    assert actual == expected

    string = "a"
    pattern = "a"
    actual = find(string, pattern)
    expected = [0]
    assert actual == expected

    string = "baabba"
    pattern = "ba"
    actual = find(string, pattern)
    expected = [0, 4]
    assert actual == expected
