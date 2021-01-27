"""Given the root of a binary tree, flatten the tree into a "linked
list":

The "linked list" should use the same TreeNode class where the right
child pointer points to the next node in the list and the left child
pointer is always null.

The "linked list" should be in the same order as a pre-order traversal
of the binary tree.


Example 1:


Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]

Example 2:

Input: root = []
Output: []

Example 3:

Input: root = [0]
Output: [0]

https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

"""

from collections import namedtuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"{self.val} ({self.left} {self.right})"


def toList(root):
    result = []

    def helper(node):
        if not node:
            return None
        result.append(node.val)
        helper(node.left)
        helper(node.right)

    helper(root)
    return result


class Solution:
    def flatten(self, root: TreeNode) -> TreeNode:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None

        current = TreeNode(root.val)
        newRoot = current

        def helper(node):
            nonlocal current
            if not node:
                return None
            current.right = TreeNode(node.val)
            current = current.right

            helper(node.left)
            helper(node.right)

        helper(root)
        return newRoot.right


Case = namedtuple("Case", ["root", "expected"])


def test():
    sol = Solution()
    cases = [
        Case(
            TreeNode(
                1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(5, None, TreeNode(6))
            ),
            [1, 2, 3, 4, 5, 6],
        )
    ]
    for c in cases:
        actual = sol.flatten(c.root)
        print(actual)
        assert toList(actual) == c.expected
