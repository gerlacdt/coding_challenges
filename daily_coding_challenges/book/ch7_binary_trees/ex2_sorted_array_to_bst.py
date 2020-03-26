"""Given a sorted array, convert it into a height-balanced binary
tree.

"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return "{} ({} {})".format(self.val, self.left, self.right)


def inorder(root):
    result = []

    def helper(node):
        if not node:
            return None
        helper(node.left)
        result.append(node.val)
        helper(node.right)

    helper(root)
    return result


def toBst(arr):

    def helper(low, high):
        print("low: {} high: {}".format(low, high))
        if low > high:
            return None
        mid = (low + high) // 2
        node = Node(arr[mid])
        node.left = helper(low, mid-1)
        node.right = helper(mid+1, high)
        return node

    return helper(0, len(arr) - 1)


def test():
    arr = [i for i in range(10)]
    actual = toBst(arr)
    print("bst: {}".format(actual))
    assert inorder(actual) == arr
