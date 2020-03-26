"""Given an array where elements are sorted in ascending order,
convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary
tree in which the depth of the two subtrees of every node never differ
by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the
following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5

"""

from typing import List


class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

    def __str__(self):
        return "({} ({} {}))".format(self.val, self.left, self.right)


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def helper(min_index, max_index):
            if min_index > max_index:
                return None
            mid = (max_index + min_index) // 2
            node = TreeNode(nums[mid])
            node.left = helper(min_index, mid-1)
            node.right = helper(mid+1, max_index)
            return node
        return helper(0, len(nums)-1)


def inorder(node):
    result = []

    def helper(node):
        if not node:
            return None
        helper(node.left)
        result.append(node.val)
        helper(node.right)
    helper(node)
    return result


def test():
    input1 = [-10, -3, 0, 5, 9]
    sol = Solution()
    result = sol.sortedArrayToBST(input1)
    assert inorder(result) == input1
