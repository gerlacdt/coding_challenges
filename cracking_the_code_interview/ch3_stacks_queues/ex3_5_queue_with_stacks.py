"""
Implement a queue with 2 stacks.
"""


class MyQueue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def __str__(self):
        return "({} {})".format(self.s1, self.s2)

    def enqueue(self, val):
        print("enter enqueue(): {}".format(self))
        if not self.s2:
            self.s1.append(val)
            return None
        raise RuntimeError("Queue is in inconsistent state")

    def dequeue(self):
        print("enter dequeue(): {}".format(self))
        if not self.s1:
            raise RuntimeError("Queue is empty")
        for i in range(len(self.s1)):
            val = self.s1.pop()
            self.s2.append(val)
        result = self.s2.pop()  # last value is the value of interest
        for i in range(len(self.s2)):
            val = self.s2.pop()
            self.s1.append(val)
        assert not self.s2
        return result


def test():
    q = MyQueue()
    for i in range(8):

        q.enqueue(i)

    assert not q.s2
    assert q.s1 == [0,1,2,3,4,5,6,7]

    for i in range(8):
        val = q.dequeue()
        assert val == i
