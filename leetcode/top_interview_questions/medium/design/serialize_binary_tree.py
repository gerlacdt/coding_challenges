"""Serialization is the process of converting a data structure or
object into a sequence of bits so that it can be stored in a file or
memory buffer, or transmitted across a network connection link to be
reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There
is no restriction on how your serialization/deserialization algorithm
should work. You just need to ensure that a binary tree can be
serialized to a string and this string can be deserialized to the
original tree structure.

Example:

You may serialize the following tree:

    1
   / \
  2   3
     / \
    4   5

as "[1,2,3,null,null,4,5]"


Clarification: The above format is the same as how LeetCode serializes
a binary tree. You do not necessarily need to follow this format, so
please be creative and come up with different approaches yourself.

Note: Do not use class member/global/static variables to store
states. Your serialize and deserialize algorithms should be stateless.

"""


class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

    def __str__(self):
        return "{} ({} {})".format(self.val, self.left, self.right)


def inorder(root):
    result = []

    def helper(node):
        if not node:
            return
        helper(node.left)
        result.append(node.val)
        helper(node.right)

    helper(root)
    return result


def preorder(root):
    result = []

    def helper(node):
        if not node:
            return
        result.append(node.val)
        helper(node.left)
        helper(node.right)

    helper(root)
    return result


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        result = []

        def helper(node):
            if not node:
                result.append(None)
                return
            result.append(node.val)
            helper(node.left)
            helper(node.right)

        helper(root)
        return str(result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        nums = eval(data)

        def helper(nums):
            if not nums:
                raise RuntimeError("Illegal data: {}".format(data))
            num = nums[0]
            if num == None:
                return None, nums[1:]
            node = TreeNode(num)
            node.left, lrest = helper(nums[1:])
            node.right, rrest = helper(lrest)
            return node, rrest

        result, _ = helper(nums)
        return result


def testSerialize():
    root = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
    codec = Codec()
    actual = codec.serialize(root)
    expected = "[1, 2, None, None, 3, 4, None, None, 5, None, None]"
    assert actual == expected


def testDeserialize():
    string = "[1, 2, None, None, 3, 4, None, None, 5, None, None]"
    codec = Codec()
    actual = codec.deserialize(string)
    expected = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
    assert inorder(actual) == inorder(expected)
    assert preorder(actual) == preorder(expected)


def testRoundtrip():
    root = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
    codec = Codec()
    actual = codec.deserialize(codec.serialize(root))
    expected = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
    assert inorder(actual) == inorder(expected)
    assert preorder(actual) == preorder(expected)


def testRoundtripEmptyTree():
    root = None
    codec = Codec()
    actual = codec.deserialize(codec.serialize(root))
    expected = None
    assert actual == expected


def testInorder():
    root = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
    actual = inorder(root)
    expected = [2, 1, 4, 3, 5]
    assert actual == expected


def testPreorder():
    root = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
    actual = preorder(root)
    expected = [1, 2, 3, 4, 5]
    assert actual == expected
