"""Given the root of a binary tree and an integer targetSum, return
all root-to-leaf paths where each path's sum equals targetSum.

A leaf is a node with no children.

Example 1:


Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]


Example 2:


Input: root = [1,2,3], targetSum = 5
Output: []


Example 3:

Input: root = [1,2], targetSum = 0
Output: []

"""

from collections import namedtuple
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        # naive solution
        def helper(node):
            if not node:
                return []
            l = helper(node.left)
            r = helper(node.right)

            result = []
            if not l and not r:
                result.append([node.val])
            if l:
                result.extend([[node.val] + path for path in l])
            if r:
                result.extend([[node.val] + path for path in r])

            return result

        return [item for item in helper(root) if sum(item) == targetSum]

    def dfs(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        if not root:
            return []
        result = []
        frontier = [(root, [root.val])]
        while frontier:
            node, path = frontier.pop()
            if sum(path) == targetSum and not node.left and not node.right:
                result.append(path)

            for child in [node.right, node.left]:
                if child:
                    frontier.append((child, path + [child.val]))

        return result


Case = namedtuple("Case", ["root", "targetSum", "expected"])


def test():

    sol = Solution()
    cases = [
        Case(
            TreeNode(
                5,
                TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))),
                TreeNode(8, TreeNode(13), TreeNode(4, TreeNode(5), TreeNode(1))),
            ),
            22,
            [[5, 4, 11, 2], [5, 8, 4, 5]],
        ),
        Case(TreeNode(1, TreeNode(2, TreeNode(3))), 5, []),
        Case(TreeNode(1, TreeNode(2)), 1, []),
    ]

    for c in cases:
        actual = sol.pathSum(c.root, c.targetSum)
        assert actual == c.expected

        actual = sol.dfs(c.root, c.targetSum)
        assert actual == c.expected
