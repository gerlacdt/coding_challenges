"""Given a binary tree, check whether it is a mirror of itself (ie,
symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3

But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3

Bonus points if you could solve it both recursively and iteratively.
"""

from collections import deque


class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


def dfs_iter(root):
    frontier = deque([root])
    result = []
    while frontier:
        current = frontier.pop()
        result.append(current.val)
        for node in [current.left, current.right]:
            if not node:
                continue
            frontier.append(node)
    return result


def dfs(root):
    result = []

    def helper(node):
        if not node:
            result.append(None)
            return None
        result.append(node.val)
        helper(node.left)
        helper(node.right)
        return None
    helper(root)
    return result


def dfsright(root):
    result = []

    def helper(node):
        if not node:
            result.append(None)
            return None
        result.append(node.val)
        helper(node.right)
        helper(node.left)
        return None
    helper(root)
    return result


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return dfs(root.left) == dfsright(root.right)

    def isSymmetric2(self, root: TreeNode) -> bool:
        def isMirror(node1, node2):
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False
            if ((node1.val == node2.val) and
                isMirror(node1.right, node2.left) and
                isMirror(node1.left, node2.right)):
                return True
            else:
                return False
        return isMirror(root.left, root.right)

    def isSymmetric3(self, root: TreeNode) -> bool:
        q = deque([])
        q.append(root)
        q.append(root)
        while q:
            t1 = q.popleft()
            t2 = q.popleft()
            if not t1 and not t2:
                continue
            if not t1 or not t2:
                return False
            if t1.val != t2.val:
                return False
            q.append(t1.left)
            q.append(t2.right)
            q.append(t1.right)
            q.append(t2.left)
        return True


def test():
    root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)),
                    TreeNode(2, TreeNode(4), TreeNode(3)))
    result = dfs(root)
    expected = [1, 2, 3, None, None, 4, None, None, 2, 4,
                None,  None, 3, None, None]
    assert result == expected

    iter_result = dfs_iter(root)
    assert iter_result == [1, 2, 3, 4, 2, 4, 3]


    sol = Solution()
    result = sol.isSymmetric(root)
    result2 = sol.isSymmetric2(root)
    result3 = sol.isSymmetric3(root)
    assert result == result2
    assert result == result3

    root = TreeNode(1, TreeNode(2, None, TreeNode(3)),
                    TreeNode(2, None, TreeNode(3)))

    result = sol.isSymmetric(root)
    result2 = sol.isSymmetric2(root)
    result3 = sol.isSymmetric3(root)
    assert result == result2
    assert result == result3
