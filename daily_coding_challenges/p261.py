"""Good morning! Here's your coding interview problem for today.

This problem was asked by Amazon.

Huffman coding is a method of encoding characters based on their
frequency. Each letter is assigned a variable-length binary string,
such as 0101 or 111110, where shorter lengths correspond to more
common letters. To accomplish this, a binary tree is built such that
the path from the root to any leaf uniquely maps to a character. When
traversing the path, descending to a left child corresponds to a 0 in
the prefix, while descending right corresponds to 1.

Here is an example tree (note that only the leaf nodes have letters):

        *
      /   \
    *       *
   / \\     / \
  *   a   t   *
 /             \
c               s
With this encoding, cats would be represented as 0000110111.

Given a dictionary of character frequencies, build a Huffman tree, and
use it to determine a mapping between characters and their encoded
binary strings.

"""

import heapq


class Node:
    def __init__(self, key, val=None, left=None, right=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right

    def __eq__(self, other):
        return self.key == self.key

    def __lt__(self, other):
        return self.key < other.key


def huffmanTree(pairs):
    """Builds a minimal huffman tree. A pair is a tuple (frequency,
character) from which the huffman tree can be build."""
    heap = []
    # fill heap
    for p in pairs:
        freq, char = p
        heapq.heappush(heap, Node(freq, char))

    # build huffman tree
    while len(heap) > 1:
        first = heapq.heappop(heap)
        second = heapq.heappop(heap)
        freq = first.key + second.key
        node = Node(freq)
        node.left = first
        node.right = second
        heapq.heappush(heap, node)
    return heapq.heappop(heap)


def construct(root):
    d = {}

    def helper(node, path):
        # is leaf
        if not node.left and not node.right:
            d[node.val] = "".join(path)
            return

        if node.left:
            helper(node.left, path[:] + ["0"])

        if node.right:
            helper(node.right, path[:] + ["1"])

    helper(root, [])
    return d


def encode(word, d):
    return "".join([d[c] for c in word])


def test():
    pairs = [(5, "f"), (9, "e"), (12, "c"),
             (13, "b"), (16, "d"), (45, "a"),
    ]
    root = huffmanTree(pairs)
    d = construct(root)
    word = "cafe"
    actual = encode(word, d)
    expected = "100011001101"

    assert actual == expected
