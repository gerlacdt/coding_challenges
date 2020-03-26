"""Find inorder successor of given node. Nodes have a link to its
parent.

"""


class Node:
    def __init__(self, val, parent=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

    def __str__(self):
        return "{} ({} {})".format(self.val, self.left, self.right)


def treeMin(root):
    if not root:
        return None
    if not root.left:
        return root
    else:
        return treeMin(root.left)


def successor(node):
    # case 1
    if node.right:
        return treeMin(node.right)

    # case 2
    current = node
    p = current.parent
    while p:
        if current != p.right:
            break
        current = p
        p = current.parent
    return p


def insert(node, n):
    if not node:
        return Node(n)
    if node.val >= n:
        temp = insert(node.left, n)
        node.left = temp
        temp.parent = node
    else:
        temp = insert(node.right, n)
        node.right = temp
        temp.parent = node
    return node


def inorder(root):
    nodes = []

    def helper(node):
        if not node:
            return None
        helper(node.left)
        nodes.append(node)
        helper(node.right)
    helper(root)
    return nodes


def test():
    root = None
    root = insert(root, 20)
    root = insert(root, 8)
    root = insert(root, 22)
    root = insert(root, 4)
    root = insert(root, 12)
    root = insert(root, 10)
    root = insert(root, 14)

    nodes = inorder(root)
    for i, n in enumerate(nodes):
        succ = successor(n)
        if i < (len(nodes) - 1):
            expected = nodes[i+1]
            print("current: {}, succ: {}, expected: {}".format(n.val, succ.val, expected.val))
            assert succ.val == expected.val
        else:
            print("current: {}, succ: {}, expected: {}".format(n.val, succ, None))
            assert not succ
