"""
20.1 Ghost

Page 238

"""

# build Trie

IS_WORD = "#"


class Trie:
    def __init__(self, words):
        self.root = {}
        self._build(words)

    def _build(self, words):
        for w in words:
            self._insert(w)

    def _insert(self, word):
        current = self.root
        for c in word:
            if c in current:
                current = current[c]
            else:
                current[c] = {}
                current = current[c]
        current[IS_WORD] = True

    def find(self, prefix):
        current = self.root
        for c in prefix:
            if c not in current:
                return None
            current = current[c]
        return current

    def __repr__(self):
        return "{}".format(self.root)


# check if for winning beginning character


def is_winning(trie, prefix):
    node = trie.find(prefix)
    if IS_WORD in node:
        return False
    else:
        moves = [prefix + c for c in node.keys()]
        if any(is_winning(trie, move) for move in moves):
            return False
        else:
            return True


def play_ghost(words):
    winner_chars = []
    trie = Trie(words)
    for letter in trie.root.keys():
        if is_winning(trie, letter):
            winner_chars.append(letter)
    return winner_chars


def testBuildTrie():
    words = ["cat", "cadaver"]
    actual = Trie(words)
    expected = {
        "c": {"a": {"t": {"#": True}, "d": {"a": {"v": {"e": {"r": {"#": True}}}}}}}
    }
    assert actual.root == expected


def testFindTrie():
    words = ["cat", "cadaver"]
    trie = Trie(words)
    actual = trie.find("ca")
    expected = {"d": {"a": {"v": {"e": {"r": {"#": True}}}}}, "t": {"#": True}}
    assert actual == expected

    actual = trie.find("cat")
    expected = {"#": True}
    assert actual == expected


def testGhost():
    words = ["cat", "calf", "dog", "bear"]
    actual = play_ghost(words)
    expected = ["c", "b"]
    assert actual == expected
