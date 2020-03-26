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
from collections import deque, defaultdict


class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


def toList(d):
    result = [[] for i in range(len(d))]
    for i, v in d.items():
        result[i] = v
    return result


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        "Iterative solution."
        if not root:
            return []
        stack = deque([root])
        result = []
        while stack:
            size = len(stack)
            levelList = []
            for i in range(size):
                node = stack.popleft()
                levelList.append(node.val)
                for n in [node.left, node.right]:
                    if not n:
                        continue
                    stack.append(n)
            result.append(levelList)
        return result

    def levelOrder2(self, root: TreeNode) -> List[List[int]]:
        "Recursive solution."
        if not root:
            return []
        result = defaultdict(list)  # list of lists

        def helper(node, level):
            if not node:
                return None
            helper(node.left, level+1)
            result[level].append(node.val)
            helper(node.right, level+1)
            return None
        helper(root, 0)
        return toList(result)


def test():
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    expected = [
        [3],
        [9, 20],
        [15, 7]
    ]
    sol = Solution()
    result = sol.levelOrder2(root)
    assert result == expected

    result2 = sol.levelOrder(root)
    assert result == result2
