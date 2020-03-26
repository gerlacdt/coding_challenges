"""Given a sorted array with unique integers. Create a binary search
tree with minimal height.
"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return "{} ({} {})".format(self.val, self.left, self.right)


def createTree(arr):
    def helper(min_index, max_index):
        if min_index > max_index:
            return None
        mid = (max_index + min_index) // 2
        node = Node(arr[mid])
        node.left = helper(min_index, mid-1)
        node.right = helper(mid+1, max_index)
        return node
    return helper(0, len(arr)-1)


def test():
    # root = Node(1, Node(0), Node(2, None, Node(3)))
    arr = [1,2,3,4,5]
    root = createTree(arr)
    print(root)
