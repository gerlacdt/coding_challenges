"""Given a binary tree. Return all paths with sum up to a given
value. The path does not need to start or end at the root or a leaf.

"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return "{} ({} {})".format(self.val, self.left, self.right)


def findHeight(root):
    if not root:
        return 0
    return 1 + max(findHeight(root.left), findHeight(root.right))


def findKSum(root, k):
    result = []

    def helper(node, k, path):
        # no goal found and end here
        if not node:
            return None
        # extend possible solution
        path.append(node.val)
        # run reverse through path and check sum
        t = 0
        for i in range(len(path)-1, -1, -1):
            t += path[i]
            if t == k:
                # found solution
                result.append(path[i:])
        helper(node.left, k, path)
        helper(node.right, k, path)
        # backtrack
        path.pop()

    helper(root, k, [])
    return result


def test():
    root = Node(3, Node(1, Node(1), Node(1)),
                Node(2, Node(-2, Node(6, Node(-4))), Node(10)))

    height = findHeight(root)
    assert height == 5

    result = findKSum(root, 5)
    assert len(result) == 4
    assert result == [[3, 1, 1], [3, 1, 1], [3, 2], [3, 2, -2, 6, -4]]
    # print(result)
