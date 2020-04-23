# coding: utf-8

"""Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common
ancestor is defined between two nodes p and q as the lowest node in T
that has both p and q as descendants (where we allow a node to be a
descendant of itself).”

Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.


Example 2:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5

Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a
descendant of itself according to the LCA definition.


Note:

All of the nodes' values will be unique.
p and q are different and both values will exist in the binary tree.

"""


class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

    def __repr__(self):
        return "{}".format(self.val)


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":

        # find path to p
        pNode, pPath = self._dfs(root, p.val, [])
        # print("p: {}, pPath: {}".format(pNode, pPath))

        # find path to q
        qNode, qPath = self._dfs(root, q.val, [])
        # print("q: {}, qPath: {}".format(qNode, qPath))

        # find last common node in both paths
        i = 0
        current = None
        while i < len(pPath) and i < len(qPath) and pPath[i].val == qPath[i].val:
            current = pPath[i]
            i += 1
        return current

    def _dfs(self, node, goal, path):
        if not node:
            return None, path
        if node.val == goal:
            return node, path + [node]
        for succ in [node.left, node.right]:
            result, newPath = self._dfs(succ, goal, path + [node])
            if result:
                return result, newPath
        return None, path

    def lowestCommonAncestor2(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":

        result = None

        def helper(node):
            nonlocal result
            if not node:
                return False
            left = helper(node.left)
            right = helper(node.right)
            mid = node.val == p.val or node.val == q.val
            if (mid and left) or (mid and right) or (left and right):
                result = node
            return mid or left or right

        helper(root)
        return result


def test():
    sol = Solution()
    root = TreeNode(
        3,
        TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))),
        TreeNode(1, TreeNode(0), TreeNode(8)),
    )
    p = root.left
    q = root.right
    actual = sol.lowestCommonAncestor(root, p, q)
    actual2 = sol.lowestCommonAncestor2(root, p, q)
    expected = 3
    assert actual.val == expected
    assert actual2.val == expected

    p = root.left.left
    q = root.left.right
    actual = sol.lowestCommonAncestor(root, p, q)
    actual2 = sol.lowestCommonAncestor2(root, p, q)
    expected = 5
    assert actual.val == expected
    assert actual2.val == expected

    p = root.left
    q = root.left.right.right
    actual = sol.lowestCommonAncestor(root, p, q)
    actual2 = sol.lowestCommonAncestor2(root, p, q)
    expected = 5
    assert actual.val == expected
    assert actual2.val == expected
