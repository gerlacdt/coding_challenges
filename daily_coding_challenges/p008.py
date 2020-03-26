"""Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

A unival tree (which stands for "universal value") is a tree where all
nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1

"""


class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return "Node ({} ({} {}))".format(self.data, self.left, self.right)


def count_unival(root):
    counter = 0

    def helper(root):
        nonlocal counter
        if root is None:
            return True
        # postorder - traversal
        is_left_unival = helper(root.left)
        is_right_unival = helper(root.right)

        if (is_left_unival and is_right_unival):
            if (root.left and root.right):
                if (root.left.data == root.right.data
                    and root.data == root.right.data):
                    counter += 1
                    return True
                else:
                    return False
            if root.left and root.left.data == root.data:
                counter += 1
                return True
            if root.right and root.right.data == root.data:
                counter += 1
                return True
            if not root.left and not root.right:
                counter += 1
                return True

            # shorter verion from dailing coding problem blog
            # if root.left is not None and root.data != root.left.data:
            #     return False
            # if root.right is not None and root.data != root.right.data:
            #     return False
            else:
                # counter += 1
                return False
        return False

    helper(root)
    return counter


def test():
    # tree
    #   0
    #  / \
    # 1   0
    #    / \
    #   1   0
    #  / \
    # 1   1
    tree = Node(0, Node(1, None, None),
                Node(0, Node(1, Node(1, None, None),
                             Node(1, None, None)),
                     Node(0, None, None)))

    # print(tree)
    assert count_unival(tree) == 5

    # tree2
    #     5
    #    / \
    #   1   5
    #  / \   \
    # 5   5   5

    tree2 = Node(5, Node(1, Node(5, None, None), Node(5, None, None)),
                 Node(5, None, Node(5, None, None)))

    assert count_unival(tree2) == 4

    # tree3
    #     5
    #    / \
    #   4   5
    #  / \   \
    # 4   4   5

    tree3 = Node(5, Node(4, Node(4, None, None), Node(4, None, None)),
                 Node(5, None, Node(5, None, None)))

    assert count_unival(tree3) == 5
