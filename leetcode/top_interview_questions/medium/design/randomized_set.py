"""Design a data structure that supports all following operations in
average O(1) time.

insert(val): Inserts an item val to the set if not already present.

remove(val): Removes an item val from the set if present.

getRandom: Returns a random element from current set of elements. Each
element must have the same probability of being returned.

Example:

// Init an empty set.
RandomizedSet randomSet = new RandomizedSet();

// Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomSet.insert(1);

// Returns false as 2 does not exist in the set.
randomSet.remove(2);

// Inserts 2 to the set, returns true. Set now contains [1,2].
randomSet.insert(2);

// getRandom should return either 1 or 2 randomly.
randomSet.getRandom();

// Removes 1 from the set, returns true. Set now contains [2].
randomSet.remove(1);

// 2 was already in the set, so return false.
randomSet.insert(2);

// Since 2 is the only number in the set, getRandom always return 2.
randomSet.getRandom();

"""

from random import randint
from collections import defaultdict
import pprint


class RandomizedSet:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = {}
        self.lst = []

    def insert(self, val: int) -> bool:
        """Inserts a value to the set. Returns true if the set did not
        already contain the specified element.
        """
        if val in self.data:
            return False
        self.data[val] = len(self.lst)
        self.lst.append(val)
        return True

    def remove(self, val: int) -> bool:
        """Removes a value from the set. Returns true if the set contained
        the specified element.

        """
        if val not in self.data:
            return False
        index = self.data[val]
        del self.data[val]

        # update lst
        size = len(self.lst)
        last = self.lst[size - 1]
        self.lst[index], self.lst[size - 1] = (
            self.lst[size - 1],
            self.lst[index],
        )
        del self.lst[-1]
        if index != size - 1:
            self.data[last] = index
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        if not self.lst:
            raise RuntimeError("No elements in set.")
        i = randint(0, len(self.lst) - 1)
        return self.lst[i]


def test1():
    obj = RandomizedSet()
    actual = obj.insert(1)
    assert actual
    actual = obj.remove(2)
    assert not actual
    actual = obj.getRandom()
    assert actual == 1


def test2():
    obj = RandomizedSet()
    for i in range(20):
        obj.insert(i)

    stats = defaultdict(int)
    for i in range(100000):
        val = obj.getRandom()
        stats[val] += 1

    pp = pprint.PrettyPrinter()
    pp.pprint(stats)


def test3():
    obj = RandomizedSet()
    actual = [
        obj.insert(0),
        obj.insert(1),
        obj.remove(0),
        obj.insert(2),
        obj.remove(1),
        obj.getRandom(),
    ]
    assert actual == [True, True, True, True, True, 2]


def test4():
    obj = RandomizedSet()
    actual = [
        obj.remove(0),
        obj.remove(0),
        obj.insert(0),
        obj.getRandom(),
        obj.remove(0),
        obj.insert(0),
    ]
    assert actual == [False, False, True, 0, True, True]


def test5():
    obj = RandomizedSet()
    # inserts
    lst = list(range(3))
    for i in lst:
        obj.insert(i)

    assert obj.data == {0: 0, 1: 1, 2: 2}
    assert obj.lst == [0, 1, 2]
    # removes

    obj.remove(0)
    assert obj.data == {1: 1, 2: 0}
    assert obj.lst == [2, 1]
    obj.remove(1)
    assert obj.data == {2: 0}
    assert obj.lst == [2]
    obj.remove(2)
    assert obj.data == {}
    assert obj.lst == []
