"""Given a binary tree, return the zigzag level order traversal of
its nodes' values. (ie, from left to right, then right to left for the
next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
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


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        def toList(d):
            lst = [[] for i in range(len(d))]
            for k, v in d.items():
                if k % 2 == 0:
                    lst[k] = v
                else:
                    lst[k] = list(reversed(v))
            return lst

        def bfs(node):
            if not node:
                return []
            level = 0
            queue = deque([(node, level)])
            results = defaultdict(list)
            while queue:
                node, level = queue.popleft()
                results[level].append(node.val)
                for child in [node.left, node.right]:
                    if child:
                        queue.append((child, level+1))
            return toList(results)
        return bfs(root)


def test():
    s = Solution()
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    actual = s.zigzagLevelOrder(root)
    expected = [
        [3],
        [20,9],
        [15,7],
    ]
    assert actual == expected

    root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5, None, TreeNode(8))),
                    TreeNode(3, TreeNode(6, TreeNode(9)), TreeNode(7)))
    actual = s.zigzagLevelOrder(root)
    expected = [
        [1],
        [3, 2],
        [4, 5, 6 ,7],
        [9, 8],
    ]
    assert actual == expected

    root = None
    actual = s.zigzagLevelOrder(root)
    expected = []
    assert actual == expected
