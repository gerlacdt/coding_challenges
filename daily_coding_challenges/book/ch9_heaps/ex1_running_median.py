"""Compute the running median of a sequence of numbers. That is, given
a stream of numbers, print ut the median of the list so far after each
new element.

Recall that the median of an even-numbered list is the average of the
two middle numbers.

For example, given the sequence [2,1,5,7,2,0,5], your algorithm should print out:

2
1.5
2
3.5
2
2
2

"""


import heapq


class MinHeap:
    def __init__(self):
        self.arr = []

    def push(self, value):
        heapq.heappush(self.arr, value)

    def pop(self):
        return heapq.heappop(self.arr)

    def peek(self):
        return self.arr[0]

    def len(self):
        return len(self.arr)


class MaxHeap:
    def __init__(self):
        self.arr = []

    def push(self, value):
        heapq.heappush(self.arr, -value)

    def pop(self):
        return -heapq.heappop(self.arr)

    def peek(self):
        return -self.arr[0]

    def len(self):
        return len(self.arr)


class RunningMedian:
    def __init__(self):
        self.maxheap = MaxHeap()
        self.minheap = MinHeap()

    def add(self, value):
        if self.minheap.len() > self.maxheap.len():
            if value > self.minheap.peek():
                self.minheap.push(value)
                # balance
                self.maxheap.push(self.minheap.pop())
            else:
                self.maxheap.push(value)
        elif self.minheap.len() < self.maxheap.len():
            if value > self.minheap.peek():
                self.minheap.push(value)
            else:
                self.maxheap.push(value)
                self.minheap.push(self.maxheap.pop())
        else:
            # case: both heaps are empty
            if self.minheap.len() == 0:
                self.minheap.push(value)
                return
            if value > self.minheap.peek():
                self.minheap.push(value)
            else:
                self.maxheap.push(value)

    def median(self):
        if self.maxheap.len() > self.minheap.len():
            return self.maxheap.peek()
        elif self.maxheap.len() < self.minheap.len():
            return self.minheap.peek()
        else:
            return (self.maxheap.peek() + self.minheap.peek()) / 2


def testMinHeap():
    heap = MinHeap()
    sequence = [2, 1, 5, 7, 2, 0, 5]
    expected = [2, 1, 1, 1, 1, 0, 0]
    for i, num in enumerate(sequence):
        heap.push(num)
        actual = heap.peek()
        assert actual == expected[i]


def testMaxHeap():
    heap = MaxHeap()
    sequence = [2, 1, 5, 7, 2, 0, 5]
    expected = [2, 2, 5, 7, 7, 7, 7]
    for i, num in enumerate(sequence):
        heap.push(num)
        actual = heap.peek()
        assert actual == expected[i]


def testRunningMedian():
    runningMedian = RunningMedian()
    sequence = [2, 1, 5, 7, 2, 0, 5]
    expected = [2, 1.5, 2, 3.5, 2, 2, 2]
    for i, num in enumerate(sequence):
        runningMedian.add(num)
        actual = runningMedian.median()
        print("median: {}".format(actual))
        assert actual == expected[i]
