"""Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.

You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.

Example 1:

Input:
	Tree 1                     Tree 2
          1                         2
         / \                       / \
        3   2                     1   3
       /                           \   \
      5                             4   7
Output:
Merged tree:
	     3
	    / \
	   4   5
	  / \   \
	 5   4   7

Note: The merging process must start from the root nodes of both trees.

"""

from collections import namedtuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"{self.val} ({self.left} {self.right})"


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


class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1:
            return t2
        if not t2:
            return t1
        t1.val += t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)

        return t1

    def nonDestructive(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        def helper(node1, node2):
            if not node1 and not node2:
                return None
            elif not node1:
                p = TreeNode(node2.val)
                p.left = helper(None, node2.left)
                p.right = helper(None, node2.right)
                return p
            elif not node2:
                p = TreeNode(node1.val)
                p.left = helper(node1.left, None)
                p.right = helper(node1.right, None)
                return p
            else:
                p = TreeNode(node1.val + node2.val)
                p.left = helper(node1.left, node2.left)
                p.right = helper(node1.right, node2.right)
                return p

        return helper(t1, t2)


Case = namedtuple("Case", ["t1", "t2", "expectedInorder", "expectedPreorder"])


def test():
    sol = Solution()
    cases = [
        Case(
            TreeNode(1, TreeNode(3, TreeNode(5)), TreeNode(2)),
            TreeNode(2, TreeNode(1, None, TreeNode(4)), TreeNode(3, None, TreeNode(7))),
            [5, 4, 4, 3, 5, 7],
            [3, 4, 5, 4, 5, 7],
        ),
        Case(TreeNode(1), TreeNode(2), [3], [3]),
    ]
    for c in cases:
        actual = sol.nonDestructive(c.t1, c.t2)
        assert inorder(actual) == c.expectedInorder
        assert preorder(actual) == c.expectedPreorder

        # ATTENTION, must be last because it's destructive!!!
        actual = sol.mergeTrees(c.t1, c.t2)
        assert inorder(actual) == c.expectedInorder
        assert preorder(actual) == c.expectedPreorder
