"""Given a non-negative integer numRows, generate the first numRows of
Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers
directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

"""

from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        "iterative version"
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        result = [[1], [1, 1]]
        counter = 2
        while (counter < numRows):
            last = result[-1]
            new = [1]
            for j in range(1, len(last)):
                new.append(last[j-1] + last[j])
            new.append(1)
            result.append(new)
            counter += 1
        return result

    def generate2(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]
        else:
            pyramid = self.generate(numRows-1)
            last = pyramid[-1]
            new = [1]
            for i in range(1, len(last)):
                new.append(last[i-1] + last[i])
            new.append(1)
            pyramid.append(new)
            return pyramid


def pascal(n):
    """Original pascal function, only returns last row, not the whole
triangle.

    """
    if n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    else:
        last = pascal(n-1)
        new = [1]
        for i in range(1, len(last)):
            new.append(last[i-1] + last[i])
        new.append(1)
        return new


def testPascal():
    result = pascal(5)
    expected = [1, 4, 6, 4, 1]
    assert result == expected


def testRecursive():
    s = Solution()
    result = s.generate(5)
    expected = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    assert result == expected


def testIterative():
    s = Solution()
    for n in range(7):
        result = s.generate(n)
        result2 = s.generate2(n)
        # print("n = {} result = {}".format(n, result))
        assert result == result2
