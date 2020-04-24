"""Given a binary tree and a sum, determine if the tree has a
root-to-leaf path such that adding up all the values along the path
equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1

return true, as there exist a root-to-leaf path 5->4->11->2 which sum
is 22.

"""


class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

    def __repr__(self):
        return "{}".format(self.val)


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False

        def helper(node, goal, state):
            # print("node: {}, goal: {}, state: {}".format(node, goal, state))
            if not node:
                return False
            if state == goal and not node.left and not node.right:
                return True
            for succ in [node.left, node.right]:
                if succ:
                    tmp = helper(succ, goal, state + succ.val)
                    if tmp:
                        return True
            return False

        return helper(root, sum, root.val)


def test():
    root = TreeNode(
        5,
        TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2)), None),
        TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1))),
    )

    sol = Solution()
    actual = sol.hasPathSum(root, 22)
    expected = True
    assert actual == expected

    actual = sol.hasPathSum(root, 26)
    expected = True
    assert actual == expected

    actual = sol.hasPathSum(root, 9)
    expected = False
    assert actual == expected

    root = TreeNode(1)
    actual = sol.hasPathSum(root, 0)
    expected = False
    assert actual == expected

    root = None
    actual = sol.hasPathSum(root, 1)
    expected = False
    assert actual == expected
