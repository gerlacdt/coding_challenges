"""Given a dictionary with characters and their frequencies. Build a
huffmann tree. Provide an encode and decode function.

"""

from heapq import heappush, heappop


class Node:
    def __init__(self, val, weight, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.weight = weight

    def __lt__(self, other):
        return self.weight < other.weight

    def __repr__(self):
        return "{} ({} {})".format(self.val, self.left, self.right)


class Huffman:
    def __init__(self, dictionary):
        self.root = self._build(dictionary)

    def _build(self, dictionary):
        heap = []
        for character, frequency in dictionary.items():
            heappush(heap, Node(character, frequency))

        while len(heap) > 1:
            left = heappop(heap)
            right = heappop(heap)
            # merge minimal weight nodes together
            weight = left.weight + right.weight
            heappush(heap, Node(left.val + right.val, weight, left, right))
        return heap[0]

    def encode(self, s):
        result = []

        def helper(node, c, path):
            if not node.left and not node.right:
                return path
            if c in node.left.val:
                return helper(node.left, c, path + "0")
            elif c in node.right.val:
                return helper(node.right, c, path + "1")
            raise RuntimeError("Invalid character to encode: {}".format(c))

        for c in s:
            # encode single character with huffman tree
            result.append(helper(self.root, c, ""))
        return "".join(result)

    def decode(self, s):
        result = []

        def helper(node, s):
            if not node.left and not node.right:
                return node.val, s
            c = s[0]
            if c == "0":
                return helper(node.left, s[1:])
            elif c == "1":
                return helper(node.right, s[1:])
            raise RuntimeError("Invalid character to decode: {}".format(c))

        while s:
            c, s = helper(self.root, s)
            result.append(c)
        return "".join(result)


def testBuild():
    d = {"a": 8, "b": 3, "c": 1, "d": 1, "e": 1, "f": 1, "g": 1, "h": 1}
    huffman = Huffman(d)
    actual = huffman.root
    expected = "acfgdehb (a (None None) cfgdehb (cfgd (cf (c (None None) f (None None)) gd (g (None None) d (None None))) ehb (eh (e (None None) h (None None)) b (None None))))"
    assert str(actual) == expected


def testEncode():
    d = {"a": 8, "b": 3, "c": 1, "d": 1, "e": 1, "f": 1, "g": 1, "h": 1}
    huffman = Huffman(d)
    actual = huffman.encode("abba")
    expected = "01111110"
    assert actual == expected


def testDecode():
    d = {"a": 8, "b": 3, "c": 1, "d": 1, "e": 1, "f": 1, "g": 1, "h": 1}
    huffman = Huffman(d)
    actual = huffman.decode("01111110")
    expected = "abba"
    assert actual == expected


def testRountrip():
    d = {"a": 8, "b": 3, "c": 1, "d": 1, "e": 1, "f": 1, "g": 1, "h": 1}
    huffman = Huffman(d)
    actual = huffman.decode(huffman.encode("abba"))
    expected = "abba"
    assert actual == expected
