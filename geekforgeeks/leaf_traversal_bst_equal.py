"""
see:
https://www.geeksforgeeks.org/check-if-leaf-traversal-of-two-binary-trees-is-same

Given two binary tree.  Return True if the leaf traveral order is
equal for both trees.

Example 1 True, traversal order is 4,6,7

     1
    / \
   2   3
  /   / \
 4   6   7

     0
    /  \
   5    8
    \  / \
     4 6  7


Example 2 False, traversal order is 8,9,2 and 8,2,9

     0
    / \
   1   2
      / \
     8   9

     1
    / \
   4   3
    \ / \
     8 2  9


Example 3 True

          1
         / \
        2   5
       /
      3
     /
    4


      1
     / \
    2   3
   /     \
  4       5


Example 4 False

        1
       / \
      2   4
     /   / \
    3   5   6

     1
    / \
   3   5

"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isLeaf(node):
    return not node.left and not node.right


def isEqualLeafTraversal(root1, root2):
    stack1 = [root1]
    stack2 = [root2]
    while stack1 or stack2:
        if not stack1:
            return False
        if not stack2:
            return False
        node1 = stack1.pop()
        node2 = stack2.pop()

        # find leaf for first tree
        while not isLeaf(node1):
            if node1.left:
                stack1.append(node1.left)
            if node1.right:
                stack1.append(node1.right)
            node1 = stack1.pop()

        # find leaf for second tree
        while not isLeaf(node2):
            if node2.left:
                stack2.append(node2.left)
            if node2.right:
                stack2.append(node2.right)
            node2 = stack2.pop()

        if node1.val != node2.val:
            return False
    return True


def testSimple():
    root1 = Node(1)
    root2 = Node(0, None, Node(1))
    actual = isEqualLeafTraversal(root1, root2)
    expected = True
    assert actual == expected


def testExample1():
    root1 = Node(1, Node(2, Node(4)), Node(3, Node(6), Node(7)))
    root2 = Node(0, Node(5, None, Node(4)), Node(8, Node(6), Node(7)))
    actual = isEqualLeafTraversal(root1, root2)
    expected = True
    assert actual == expected


def testExample2():
    root1 = Node(0, Node(1), Node(2, Node(8), Node(9)))
    root2 = Node(1, Node(4, None, Node(8)), Node(3, Node(2), Node(9)))
    actual = isEqualLeafTraversal(root1, root2)
    expected = False
    assert actual == expected


def testExample3():
    root1 = Node(1, Node(2, Node(3, Node(4))), Node(5))
    root2 = Node(1, Node(2, Node(4)), Node(3, None, Node(5)))
    actual = isEqualLeafTraversal(root1, root2)
    expected = True
    assert actual == expected


def testExample4():
    root1 = Node(1, Node(2, Node(3)), Node(4, Node(5), Node(6)))
    root2 = Node(1, Node(3), Node(5))
    actual = isEqualLeafTraversal(root1, root2)
    expected = False
    assert actual == expected
