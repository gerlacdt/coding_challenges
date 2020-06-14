"""Given the root node of a binary search tree (BST) and a value. You
need to find the node in the BST that the node's value equals the
given value. Return the subtree rooted with that node. If such node
doesn't exist, you should return NULL.

For example,

Given the tree:
        4
       / \
      2   7
     / \
    1   3

And the value to search: 2
You should return this subtree:

      2
     / \
    1   3
In the example above, if we want to search the value 5, since there is no node with value 5, we should return NULL.

Note that an empty tree is represented by NULL, therefore you would
see the expected output (serialized tree format) as [], not null.

"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return "{} ({} {})".format(self.val, self.left, self.right)


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        def helper(node):
            if not node:
                return None
            if node.val == val:
                return node
            lresult = helper(node.left)
            if lresult:
                return lresult
            rresult = helper(node.right)
            if rresult:
                return rresult
            return None

        return helper(root)


def test1():
    root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7))
    sol = Solution()
    actual = sol.searchBST(root, 2)
    expected = 2
    assert actual.val == expected
