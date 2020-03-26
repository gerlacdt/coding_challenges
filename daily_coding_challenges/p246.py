"""Good morning! Here's your coding interview problem for today.

This problem was asked by Dropbox.

Given a list of words, determine whether the words can be chained to
form a circle. A word X can be placed in front of another word Y in a
circle if the last character of X is same as the first character of Y.

For example, the words ['chair', 'height', 'racket', touch', 'tunic']
can form the following circle: chair --> racket --> touch --> height
--> tunic --> chair.

"""


def successors(path, leftWords):
    if not leftWords:
        return []
    succs = []
    lastWord = path[-1]
    for w in leftWords:
        if lastWord[-1] == w[0]:
            p = path[:] + [w]
            copyLeftWords = leftWords[:]
            copyLeftWords.remove(w)
            succs.append((p, copyLeftWords))
    return succs


def isCircle(words):
    visited = set()

    def helper(path, leftWords, isgoal):
        nonlocal visited
        if isgoal(path):
            return path
        # print("visited {} path {} leftWords {}".format(visited, path, leftWords))
        for s in successors(path, leftWords):
            p, leftWords = s
            if p[-1] not in visited:
                visited.add(p[-1])
                result = helper(p, leftWords, isgoal)
                if result:
                    return result
        return None

    for w in words:
        # reset visited for next start word
        visited = set([w])

        def isgoal(path):
            if len(path) == len(words) and successors(path, [w]):
                return True
            return False

        leftWords = words[:]
        leftWords.remove(w)
        result = helper([w], leftWords, isgoal)
        if result:
            return True
    return False


def test():
    words = ["chair", "height", "racket", "touch", "tunic"]
    actual = isCircle(words)
    expected = True
    assert actual == expected

    words = ["ab", "bc", "cd"]
    actual = isCircle(words)
    expected = False
    assert actual == expected

    words = ["ab", "bc", "cd", "cc", "da"]
    actual = isCircle(words)
    expected = True
    assert actual == expected

    words = ["axb", "bxc", "cxd", "dxa", "dxe", "exd"]
    actual = isCircle(words)
    expected = True
    assert actual == expected

    words = ["ijk", "kji", "abc", "cba"]
    actual = isCircle(words)
    expected = False
    assert actual == expected


def testSuccs():
    words = ["ab", "bc", "bd"]
    path = ["foob"]
    actual = successors(path, words)
    expected = [(['foob', 'bc'], ['ab', 'bd']), (['foob', 'bd'], ['ab', 'bc'])]
    assert actual == expected
