"""You have a large array, most of whose elements are zero.

Create a space-efficient data structure, SparseArray, that implements
the following interface:

init(arr, size) initialize with the original large array and size

set(i, val) update index at i to val

get(i) get the value at index i

"""

from collections import defaultdict
import pytest


class SparseArray:
    def __init__(self, arr):
        self.size = len(arr)
        self.sparseMap = defaultdict(int)
        for i, v in enumerate(arr):
            if v != 0:
                self.sparseMap[i] = v

    def set(self, i, val):
        if i < 0 or i >= self.size:
            raise RuntimeError("Index i: {} out of bounds".format(i))
        else:
            if val == 0:
                del self.sparseMap[i]
            else:
                self.sparseMap[i] = val

    def get(self, i):
        if i < 0 or i >= self.size:
            raise RuntimeError("Index i: {} out of bounds".format(i))
        else:
            return self.sparseMap[i]


def test():
    arr = [0,0,0,0,0,0,1,0,0,0,2]
    sparseArray = SparseArray(arr)
    sparseArray.set(0, 3)
    actual = sparseArray.get(0)
    expected = 3
    assert actual == expected

    with pytest.raises(RuntimeError) as excinfo:
        sparseArray.set(12, 42)
    assert str(excinfo.value) == "Index i: 12 out of bounds"

    with pytest.raises(RuntimeError) as excinfo:
        sparseArray.get(-1)
    assert str(excinfo.value) == "Index i: -1 out of bounds"

    sparseArray.set(0, 0)
    expected = {6: 1, 10: 2}
    assert sparseArray.sparseMap == expected
