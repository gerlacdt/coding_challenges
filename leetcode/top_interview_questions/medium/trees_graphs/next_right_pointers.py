"""You are given a perfect binary tree where all leaves are on the
same level, and every parent has two children. The binary tree has the
following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}

Populate each next pointer to point to its next right node. If there
is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.



Follow up:

You may only use constant extra space.  Recursive approach is fine,
you may assume implicit stack space does not count as extra space for
this problem.


Example 1:



Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]

Explanation: Given the above perfect binary tree (Figure A), your
function should populate each next pointer to point to its next right
node, just like in Figure B. The serialized output is in level order
as connected by the next pointers, with '#' signifying the end of each
level.


Constraints:

The number of nodes in the given tree is less than 4096.
-1000 <= node.val <= 1000

"""

from collections import deque


class Node:
    def __init__(
        self,
        val: int = 0,
        left: "Node" = None,
        right: "Node" = None,
        next: "Node" = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: "Node") -> "Node":
        if not root:
            return None
        frontier = deque([(root, 0)])  # tuple (node, level)
        nodes = []
        prev, prevLevel = (None, -1)
        # BFS traversal
        while frontier:
            node, level = frontier.popleft()
            if prevLevel == level:
                prev.next = node
            prev, prevLevel = node, level
            nodes.append((node, level))
            if node.left:
                frontier.append((node.left, level + 1))
            if node.right:
                frontier.append((node.right, level + 1))
        return root


def inorder(root):
    result = []

    def helper(node):
        if not node:
            return None
        helper(node.left)
        if node.next:
            result.append(node.next.val)
        else:
            result.append(None)
        helper(node.right)

    helper(root)
    return result


def test():
    root = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))
    sol = Solution()

    actual = sol.connect(root)
    # inorder = [4, 2, 5, 1, 6, 3, 7]
    expected = [5, 3, 6, None, 7, None, None]
    assert inorder(actual) == expected
