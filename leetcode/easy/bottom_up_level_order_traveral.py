"""Given a binary tree, return the bottom-up level order traversal of its
nodes' values. (ie, from left to right, level by level from leaf to
root).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

return its bottom-up level order traversal as:

[
  [15,7],
  [9,20],
  [3]
]

"""

from collections import deque, defaultdict
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        result = defaultdict(list)
        frontier = deque([(0, root)])
        while frontier:
            level, node = frontier.popleft()
            result[level].append(node.val)
            if node.left:
                frontier.append((level + 1, node.left))
            if node.right:
                frontier.append((level + 1, node.right))
        return [result[key] for key in sorted(result, reverse=True)]


def test():
    sol = Solution()
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))

    actual = sol.levelOrderBottom(root)
    expected = [[15, 7], [9, 20], [3]]

    assert actual == expected


def testNoneRoot():
    sol = Solution()
    root = None

    actual = sol.levelOrderBottom(root)
    expected = []

    assert actual == expected
