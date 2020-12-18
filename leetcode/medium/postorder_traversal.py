"""Given the root of a binary tree, return the postorder traversal of
its nodes' values.

Example 1:

Input: root = [1,null,2,3]
Output: [3,2,1]

Example 2:

Input: root = []
Output: []

Example 3:

Input: root = [1]
Output: [1]

Example 4:

Input: root = [1,2]
Output: [2,1]

Example 5:

Input: root = [1,null,2]
Output: [2,1]


https://leetcode.com/problems/binary-tree-postorder-traversal/

"""

from collections import namedtuple, defaultdict
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"{self.val} ({self.left} {self.right})"


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        result = []

        def helper(node):
            if not node:
                return
            helper(node.left)
            helper(node.right)
            result.append(node.val)

        helper(root)
        return result

    def iterative(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack1 = [root]
        stack2 = []

        while stack1:
            node = stack1.pop()
            stack2.append(node.val)
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)

        return list(reversed(stack2))

    def dfs(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        discoveryTimes = defaultdict(int)
        finishingTimes = defaultdict(int)
        time = 0

        def helper(node):
            nonlocal time
            time += 1
            discoveryTimes[node.val] = time
            if node.left:
                helper(node.left)
            if node.right:
                helper(node.right)

            time += 1
            finishingTimes[node.val] = time

        helper(root)

        return [k for k, _ in sorted(finishingTimes.items(), key=lambda item: item[1])]


Case = namedtuple("Case", ["root", "expected"])


def test():
    sol = Solution()
    cases = [
        Case(TreeNode(1, None, TreeNode(2, TreeNode(3))), [3, 2, 1]),
        Case(TreeNode(1, TreeNode(2)), [2, 1]),
        Case(TreeNode(1, None, TreeNode(2)), [2, 1]),
        Case(None, []),
        Case(TreeNode(1), [1]),
        Case(
            TreeNode(
                1,
                TreeNode(2, TreeNode(4), TreeNode(5)),
                TreeNode(3, TreeNode(6), TreeNode(7)),
            ),
            [4, 5, 2, 6, 7, 3, 1],
        ),
    ]
    for c in cases:
        actual = sol.postorderTraversal(c.root)
        assert actual == c.expected, f"root: {c.root}"

        actual2 = sol.iterative(c.root)
        assert actual2 == c.expected, f"root: {c.root}"

        actual3 = sol.dfs(c.root)
        assert actual3 == c.expected, f"root: {c.root}"
