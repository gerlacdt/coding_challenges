"""Good morning! Here's your coding interview problem for today.

This problem was asked by Amazon.

A tree is symmetric if its data and shape remain unchanged when it is
reflected about the root node. The following tree is an example:

        4
      / | \
    3   5   3
  /           \
9              9
Given a k-ary tree, determine whether it is symmetric.

"""


class Node:
    def __init__(self, val):
        self.val = val
        self.successors = []

    def __repr__(self):
        return "{} {}".format(self.val, self.successors)


class Solution:
    def isSymmetric(self, root: Node) -> bool:
        def helper(tree1, tree2):
            # print("tree1: {} tree2: {}".format(tree1, tree2))
            if not tree1 and not tree2:
                return True
            result = []
            if tree1 and tree2 and tree1.val == tree2.val:
                i = 0
                if len(tree1.successors) != len(tree2.successors):
                    return False
                j = len(tree1.successors) - 1
                while i <= j:
                    result.append(
                        helper(tree1.successors[i], tree2.successors[j])
                        and helper(tree1.successors[j], tree2.successors[i])
                    )
                    i += 1
                    j -= 1
                return all(result)
            return False

        return helper(root, root)


def testIsSymmetricTrue():
    root = Node(4)
    node3 = Node(3)
    node5 = Node(5)
    node3_2 = Node(3)
    node9 = Node(9)
    node9_2 = Node(9)
    root.successors.append(node3)
    root.successors.append(node5)
    root.successors.append(node3_2)
    node3.successors.append(node9)
    node3_2.successors.append(node9_2)

    sol = Solution()
    actual = sol.isSymmetric(root)
    expected = True
    assert actual == expected


def testIsSymmetricFalse():
    root = Node(4)
    node3 = Node(3)
    node5 = Node(5)
    node3_2 = Node(3)
    node9_2 = Node(9)
    root.successors.append(node3)
    root.successors.append(node5)
    root.successors.append(node3_2)
    node3_2.successors.append(node9_2)

    sol = Solution()
    actual = sol.isSymmetric(root)
    expected = False
    assert actual == expected


def testBinarySymmetricTrue():
    root = Node(4)
    node2 = Node(2)
    node2_2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node3_2 = Node(3)
    node4_2 = Node(4)
    root.successors.append(node2)
    root.successors.append(node2_2)
    node2.successors.append(node3)
    node2.successors.append(node4)
    node2_2.successors.append(node4_2)
    node2_2.successors.append(node3_2)

    sol = Solution()
    actual = sol.isSymmetric(root)
    expected = True
    assert actual == expected


def testBinarySymmetricFalse():
    root = Node(4)
    node2 = Node(2)
    node2_2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node3_2 = Node(3)
    node5 = Node(5)
    root.successors.append(node2)
    root.successors.append(node2_2)
    node2.successors.append(node3)
    node2.successors.append(node4)
    node2_2.successors.append(node5)
    node2_2.successors.append(node3_2)

    sol = Solution()
    actual = sol.isSymmetric(root)
    expected = False
    assert actual == expected
