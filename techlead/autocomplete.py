"""Implement an autocomplete function. Given a dictionary as a list of
words and a prefix. Find all possible completions for this given
prefix.

"""


class TrieNode:
    def __init__(self, val, isWord):
        self.val = val
        self.isWord = isWord

    def __repr__(self):
        return "{}".format(self.val)


def buildTrie(words):
    root = TrieNode({}, False)
    for w in words:
        current = root
        for c in w:
            if c not in current.val:
                current.val[c] = TrieNode({}, False)
            current = current.val[c]
        current.isWord = True
    return root


def findPrefix(prefix, root):
    current = root
    for c in prefix:
        if c not in current.val:
            # do not bail out because it is used in autocompletion function
            return TrieNode({}, False)
        current = current.val[c]
    return current


def findWords(prefix, node):
    results = []

    def helper(current, path):
        if current.isWord:
            results.append(prefix + path)
        for c in current.val:
            helper(current.val[c], path + c)

    helper(node, "")
    return results


def autocomplete(prefix, words):
    # build a trie
    trie = buildTrie(words)

    # find node in trie for the last char of prefix
    node = findPrefix(prefix, trie)

    # traverse from found node all possible paths down the trie with DFS
    completions = findWords(prefix, node)

    return completions


def test():
    words = ["dog", "dark", "cat", "door", "dodge"]
    prefix = "do"
    actual = autocomplete(prefix, words)
    expected = ["dog", "door", "dodge"]
    assert actual == expected


def testBuildTrie():
    words = ["dog", "dark", "cat", "door", "dodge"]
    actual = buildTrie(words)
    expected = "{'d': {'o': {'g': {}, 'o': {'r': {}}, 'd': {'g': {'e': {}}}}, 'a': {'r': {'k': {}}}}, 'c': {'a': {'t': {}}}}"
    assert str(actual) == expected


def testFindPrefix():
    words = ["dog", "dark", "cat", "door", "dodge"]
    trie = buildTrie(words)
    actual = findPrefix("do", trie)
    expected = "{'g': {}, 'o': {'r': {}}, 'd': {'g': {'e': {}}}}"
    assert str(actual) == expected


def testFindWords():
    words = ["dog", "dark", "cat", "door", "dodge"]
    trie = buildTrie(words)
    actual = findWords("", trie)
    expected = set(["dog", "dark", "cat", "door", "dodge"])
    assert set(actual) == expected
