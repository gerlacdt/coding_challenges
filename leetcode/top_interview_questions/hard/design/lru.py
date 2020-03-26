"""Design and implement a data structure for Least Recently Used
(LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the
key exists in the cache, otherwise return -1.

put(key, value) - Set or insert the value if the key is not already
present. When the cache reached its capacity, it should invalidate the
least recently used item before inserting a new item.

The cache is initialized with a positive capacity.

Follow up:
Could you do both operations in O(1) time complexity?

Example:
LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4

"""


import os


def debug(s):
    isDebug = os.environ.get('DEBUG')
    if isDebug == "true":
        print(s)


class Node:
    def __init__(self, key, value, prev, nxt):
        self.key = key
        self.value = value
        self.prev = prev
        self.nxt = nxt

    def __str__(self):
        return "({}->{} {})".format(self.key, self.value, self.nxt)

    def __repr__(self):
        return self.__str__()


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def prepend(self, key, value):
        if not self.head:
            node = Node(key, value, None, None)
            self.head = node
            self.tail = node
            return node
        node = Node(key, value, None, self.head)
        self.head.prev = node
        self.head = node
        return self.head

    def delete(self, node: Node):
        # handle list with single node
        if not node.prev and not node.nxt:
            self.head = None
            self.tail = None
            return
        if node == self.head:
            # delete head
            node.nxt.prev = None
            self.head = node.nxt
            return
        if node == self.tail:
            # delete tail
            node.prev.nxt = None
            self.tail = node.prev
            return
        # delete normal case
        node.prev.nxt = node.nxt
        node.nxt.prev = node.prev

    def toList(self):
        arr = []
        node = self.head
        while node:
            arr.append(node.value)
            node = node.nxt
        return arr

    def toReverseList(self):
        arr = []
        node = self.tail
        while node:
            arr.append(node.value)
            node = node.prev
        return arr

    def __str__(self):
        head = self.head if self.head else None
        tail = self.tail if self.tail else None
        return "DOUBLE_LINKED_LIST Head: {}, Tail: {}".format(head, tail)


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.lst = DoubleLinkedList()

    def get(self, key: int) -> int:
        debug("GET({}) before lst: {}, cache: {}".format(key, self.lst, self.cache))
        if key in self.cache:
            node = self.cache[key]
            self.lst.delete(node)
            new_node = self.lst.prepend(node.key, node.value)
            self.cache[key] = new_node
            debug("GET({}) after found lst: {}, cache: {}".format(key, self.lst, self.cache))
            return node.value
        debug("GET({}) after not found lst: {}, cache: {}".format(key, self.lst, self.cache))
        return -1

    def put(self, key: int, value: int) -> None:
        debug("PUT({}, {}) before lst: {}".format(key, value, self.lst))
        if key in self.cache:
            old_node = self.cache[key]
            self.lst.delete(old_node)
            new_node = self.lst.prepend(key, value)
            self.cache[key] = new_node
            debug("PUT({}, {}) after lst: {}".format(key, value, self.lst))
            return None
        node = self.lst.prepend(key, value)
        self.cache[key] = node
        if self.capacity < len(self.cache):
            del self.cache[self.lst.tail.key]
            self.lst.delete(self.lst.tail)
        debug("PUT({}, {}) after lst: {}".format(key, value, self.lst))
        return None

    def __str__(self):
        return "(cache: {}, lst: {})".format(self.cache, self.lst)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


def test():
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1       # returns 1

    cache.put(3, 3)    # evicts key 2

    assert cache.get(2) == -1       # returns -1 (not found)
    cache.put(4, 4)    # evicts key 1
    assert cache.get(1) == -1       # returns -1 (not found)
    assert cache.get(3) == 3       # returns 3
    assert cache.get(4) == 4       # returns 4


def test2():
    c = LRUCache(2)
    c.put(2, 1)
    c.put(1, 1)
    c.put(2, 3)
    c.put(4, 1)
    assert c.get(1) == -1
    assert c.get(2) == 3
    for i in range(4):
        debug("i: {}, cache: {}".format(i, c))
        c.put(i, i)
        debug("i: {}, cache: {}".format(i, c))
        debug("get: {}, c: {}".format(c.get(1), c))


def test_double_linked_list():
    lst = DoubleLinkedList()
    lst.prepend(1, 1)
    lst.prepend(2, 2)
    lst.prepend(3, 3)

    # remove middle element
    lst.delete(lst.head.nxt)
    expected = [3, 1]
    assert lst.toList() == expected
    assert list(reversed(lst.toReverseList())) == expected

    # remove head
    lst.delete(lst.head)
    expected = [1]
    assert lst.toList() == expected
    assert list(reversed(lst.toReverseList())) == expected

    # remove head and tail
    lst.delete(lst.head)
    expected = []
    assert lst.toList() == expected
    assert list(reversed(lst.toReverseList())) == expected

    # remove tail
    lst = DoubleLinkedList()
    lst.prepend(1, 1)
    lst.prepend(2, 2)
    lst.prepend(3, 3)
    lst.delete(lst.tail)
    debug("list: {}".format(lst))

    expected = [3, 2]
    assert lst.toList() == expected
    assert list(reversed(lst.toReverseList())) == expected

    # remove head
    lst2 = DoubleLinkedList()
    n1 = lst2.prepend(1, 1)
    debug("n1: {}".format(n1))
    n2 = lst2.prepend(2, 2)
    debug("n2: {}".format(n2))
    n3 = lst2.prepend(3, 3)
    debug("n3: {}".format(n3))
    lst2.delete(n3)
    debug("list: {}".format(lst2))

    expected = [2, 1]
    assert lst2.toList() == expected
    assert list(reversed(lst2.toReverseList())) == expected


def testleet():
    commands = ["put","put","put","put","put","get","put","get","get","put","get","put","put","put","get","put","get","get","get","get","put","put","get","get","get","put","put","get","put","get","put","get","get","get","put","put","put","get","put","get","get","put","put","get","put","put","put","put","get","put","put","get","put","put","get","put","put","put","put","put","get","put","put","get","put","get","get","get","put","get","get","put","put","put","put","get","put","put","put","put","get","get","get","put","put","put","get","put","put","put","get","put","put","put","get","get","get","put","put","put","put","get","put","put","put","put","put","put","put"]

    values = [[10,13],[3,17],[6,11],[10,5],[9,10],[13],[2,19],[2],[3],[5,25],[8],[9,22],[5,5],[1,30],[11],[9,12],[7],[5],[8],[9],[4,30],[9,3],[9],[10],[10],[6,14],[3,1],[3],[10,11],[8],[2,14],[1],[5],[4],[11,4],[12,24],[5,18],[13],[7,23],[8],[12],[3,27],[2,12],[5],[2,9],[13,4],[8,18],[1,7],[6],[9,29],[8,21],[5],[6,30],[1,12],[10],[4,15],[7,22],[11,26],[8,17],[9,29],[5],[3,4],[11,30],[12],[4,29],[3],[9],[6],[3,4],[1],[10],[3,29],[10,28],[1,20],[11,13],[3],[3,12],[3,8],[10,9],[3,26],[8],[7],[5],[13,17],[2,27],[11,15],[12],[9,19],[2,15],[3,16],[1],[12,17],[9,1],[6,19],[4],[5],[5],[8,1],[11,7],[5,2],[9,28],[1],[2,2],[7,4],[4,22],[7,24],[9,26],[13,28],[11,26]]

    lru = LRUCache(10)
    for i in range(len(commands)):
        if commands[i] == "put":
            key , value = values[i]
            lru.put(key, value)
        elif commands[i] == "get":
            [key] = values[i]
            lru.get(key)
        else:
            RuntimeError("Wrong command: {}".format(commands[i]))
