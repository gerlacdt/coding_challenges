"""Implement an LRU (Least Recent Used) cache. The cache should be
able to be initialized with cache size n, and provide the following
methods:

set(key, value) set key to value. If there are already n items in the
cache and we are adding a new item, also remove the least recenty used
item.

get(key) get the value of the key. If no such key exists, return null

"""


class Node:
    def __init__(self, key, val, prev=None, nxt=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.nxt = nxt

    def __str__(self):
        return "({}, {}) -> {}".format(self.key, self.val, self.nxt)


class LinkedList:
    def __init__(self):
        self.head = None
        self.end = None

    def prepend(self, node):
        if not self.head:
            self.head = node
            self.end = node
        else:
            node.nxt = self.head
            self.head.prev = node
            self.head = node

    def append(self, node):
        if not self.head:
            self.head = node
            self.end = node
        else:
            self.end.nxt = node
            node.prev = self.end
            self.end = node

    def remove(self, node):
        prev = node.prev
        nxt = node.nxt
        if not prev and not nxt:
            self.head = None
            self.end = None
        if not prev:
            self.head = node.nxt
            self.head.prev = None
        elif not nxt:
            self.end = node.prev
            self.end.nxt = None
        else:
            prev.nxt = nxt
            nxt.prev = prev

    def toList(self):
        arr = []
        node = self.head
        while node:
            arr.append(node.val)
            node = node.nxt
        return arr

    def toReverseList(self):
        arr = []
        node = self.end
        while node:
            arr.append(node.val)
            node = node.prev
        return arr


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.linkedList = LinkedList()

    def get(self, key):
        if key not in self.cache:
            return None
        node = self.cache[key]
        self.linkedList.remove(node)
        self.linkedList.prepend(Node(key, node.val))
        self.cache[key] = self.linkedList.head
        return node.val

    def set(self, key, value):
        if key in self.cache:
            node = self.cache.key
            del self.cache[key]
            self.linkedList.remove(node)
        if len(self.cache) < self.capacity:
            self.linkedList.prepend(Node(key, value))
            self.cache[key] = self.linkedList.head
        else:
            del self.cache[self.linkedList.end.key]
            self.linkedList.remove(self.linkedList.end)
            self.linkedList.prepend(Node(key, value))
            self.cache[key] = self.linkedList.head


def testList():
    lst = LinkedList()
    lst.prepend(Node("key", 1))
    lst.prepend(Node("key", 2))
    lst.prepend(Node("key", 3))
    expected = [3,2,1]
    assert lst.toList() == expected
    assert lst.toReverseList() == list(reversed(expected))

    lst = LinkedList()
    lst.append(Node("key", 1))
    lst.append(Node("key", 2))
    lst.append(Node("key", 3))
    expected = [1,2,3]
    assert lst.toList() == expected
    assert lst.toReverseList() == list(reversed(expected))

    lst = LinkedList()
    lst.append(Node("key", 1))
    lst.append(Node("key", 2))
    lst.append(Node("key", 3))
    expected = [2,3]
    lst.remove(lst.head)
    assert lst.toList() == expected
    assert lst.toReverseList() == list(reversed(expected))

    lst = LinkedList()
    lst.append(Node("key", 1))
    lst.append(Node("key", 2))
    lst.append(Node("key", 3))
    expected = [1,2]
    lst.remove(lst.head.nxt.nxt)
    assert lst.toList() == expected
    assert lst.toReverseList() == list(reversed(expected))

    lst = LinkedList()
    lst.append(Node("key", 1))
    lst.append(Node("key", 2))
    lst.append(Node("key", 3))
    expected = [1,3]
    lst.remove(lst.head.nxt)
    assert lst.toList() == expected
    assert lst.toReverseList() == list(reversed(expected))


def test():
    cache = LRUCache(2)
    cache.set(1, 1)
    cache.set(2, 2)
    assert cache.get(1) == 1
    cache.set(3, 3)    # evicts key 2
    assert not cache.get(2)
    cache.set(4, 4)    # evicts key 1
    assert not cache.get(1)
    assert cache.get(3) == 3
    assert cache.get(4) == 4
