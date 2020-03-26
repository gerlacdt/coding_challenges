"""Find the common ancestor 2 given nodes p and q. The tree is not a
binary search tree.

Do not use a helper data structure to store tree-nodes.

"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return "{} ({} {})".format(self.val, self.left, self.right)


def covers(root, node):
    """Returns True if the given node is found under the given
root-tree. Otherwise returns False

    """
    if not root:
        return False
    if root == node:
        return True
    return covers(root.left, node) or covers(root.right, node)


def find(root, val):
    """Find a node with the given value Starts searching from the given
root. Notice: we do not use binary search here because the tree is not
a binary search tree.

    """
    if not root:
        return None
    if root.val == val:
        return root
    left = find(root.left, val)
    right = find(root.right, val)
    return left or right


def ancestor(root, p, q):
    if not root:
        return None
    if root == p or root == q:
        return root
    p_on_left = covers(root.left, p)
    q_on_left = covers(root.left, q)
    if (p_on_left != q_on_left):
        return root
    if p_on_left:
        return ancestor(root.left, p, q)
    else:
        return ancestor(root.right, p, q)


def ancestor2(root, p, q):
    """Optimized version. Can fail if p or q is not in tree. Possible
remedy: check if p and q exist in tree."""
    if not root:
        return None
    if root == p or root == q:
        return root
    left = ancestor2(root.left, p, q)
    right = ancestor2(root.right, p, q)
    if left and right:
        return root
    return left if left else right


def test():
    node2 = Node(2, Node(4), Node(5))
    node3 = Node(3, Node(6), Node(7))
    root = Node(1, node2, node3)

    print(root)
    assert covers(root, node2)
    assert not covers(node2, node3)

    assert find(root, 7).val == 7
    assert find(root, 2).val == 2
    assert find(root, 3).val == 3
    assert not find(root, 0)

    result = ancestor(root, find(root, 3), find(root, 2))
    result1 = ancestor2(root, find(root, 3), find(root, 2))
    assert result.val == 1
    assert result == result1

    result = ancestor(root, find(root, 7), find(root, 2))
    result1 = ancestor2(root, find(root, 7), find(root, 2))
    assert result.val == 1
    assert result == result1

    result = ancestor(root, find(root, 5), find(root, 4))
    result1 = ancestor2(root, find(root, 5), find(root, 4))
    assert result.val == 2
    assert result == result1

    result = ancestor(root, find(root, 1), find(root, 7))
    result1 = ancestor2(root, find(root, 1), find(root, 7))
    assert result.val == 1
    assert result == result1
