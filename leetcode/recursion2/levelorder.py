"""Given a binary tree, return the level order traversal of its
nodes' values. (ie, from left to right, level by level).

For example:

Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]

"""

from typing import List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return "{} ({} {})".format(self.val, self.left, self.right)


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        height = self._height(root)
        result: List[List[int]] = [[] for _ in range(height)]
        queue: deque = deque([])
        queue.append((root, 0))
        while queue:
            node, level = queue.popleft()
            result[level].append(node.val)
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
        return result

    def _height(self, node):
        if not node:
            return 0
        leftHeight = self._height(node.left)
        rightHeight = self._height(node.right)
        return max(leftHeight, rightHeight) + 1


def testLevelOrder():
    sol = Solution()
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    actual = sol.levelOrder(root)
    expected = [[3], [9, 20], [15, 7]]
    assert actual == expected


def testHeight():
    sol = Solution()
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    actual = sol._height(root)
    expected = 3
    assert actual == expected
