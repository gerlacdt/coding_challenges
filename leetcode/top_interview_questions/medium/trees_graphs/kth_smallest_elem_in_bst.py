"""https://leetcode.com/explore/interview/card/top-interview-questions-medium/108/trees-and-graphs/790/

Given a binary search tree, write a function kthSmallest to find the
kth smallest element in it.

Note:
You may assume k is always valid, 1 <= k <= BST's total elements.

Example 1:

Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1

Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3

Follow up:

What if the BST is modified (insert/delete operations) often and you
need to find the kth smallest frequently? How would you optimize the
kthSmallest routine?

"""


class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

    def __str__(self):
        return "{} ({} {})".format(self.val, self.left, self.right)


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        lst = self.inorder(root, k)
        return lst[-1]

    def inorder(self, root: TreeNode, k):
        results = []

        def helper(node):
            # return as fast as possible, we found k elements
            if not node or len(results) > k:
                return
            helper(node.left)
            if len(results) < k:
                # the k smallest elements are found, save memory and
                # don't add additional elems to the result list
                results.append(node.val)
            helper(node.right)

        helper(root)
        return results


def test():
    root = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
    k = 1
    sol = Solution()
    actual = sol.kthSmallest(root, k)
    expected = 1
    assert actual == expected


def test2():
    root = TreeNode(5, TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)), TreeNode(6))
    k = 3
    sol = Solution()
    actual = sol.kthSmallest(root, k)
    expected = 3
    assert actual == expected
