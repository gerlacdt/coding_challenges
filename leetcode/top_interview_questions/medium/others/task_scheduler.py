"""Given a char array representing tasks CPU need to do. It contains
capital letters A to Z where different letters represent different
tasks. Tasks could be done without original order. Each task could be
done in one interval. For each interval, CPU could finish one task or
just be idle.

However, there is a non-negative cooling interval n that means between
two same tasks, there must be at least n intervals that CPU are doing
different tasks or just be idle.

You need to return the least number of intervals the CPU will take to
finish all the given tasks.



Example:

Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.


Constraints:

The number of tasks is in the range [1, 10000].
The integer n is in the range [0, 100].

"""

from typing import List, Tuple
from heapq import heappush, heappop
from collections import Counter


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        sortedCounts = sorted(counts.items(), key=lambda x: x[1])
        queue: List = []
        for c in sortedCounts:
            task, count = c
            heappush(queue, (-1 * count, task))
        result: List[str] = []
        while queue:
            restTasks: List[Tuple] = []
            i = 0
            while i <= n:
                if queue:
                    count, task = heappop(queue)
                    count *= -1
                    # print("({} {}), queue: {}".format(count, task, queue))
                    # placing task is possible
                    result.append(task)
                    if count > 1:
                        restTasks.append((-1 * (count - 1), task))
                elif restTasks:
                    # only add IDLE if sth. still needs to be
                    # scheduled. If this is not checked we would add
                    # useless IDLEs at the end of the result list
                    result.append("IDLE")
                i += 1
            for t in restTasks:
                heappush(queue, t)

        # print("result: {}".format(result))
        return len(result)


def test1():
    sol = Solution()
    tasks = ["A", "A", "A", "B", "B", "B", "C", "C", "D"]
    n = 2
    actual = sol.leastInterval(tasks, n)
    expected = 9
    assert actual == expected

    tasks = ["A", "A", "A", "B", "B", "B"]
    n = 2
    actual = sol.leastInterval(tasks, n)
    expected = 8
    assert actual == expected

    tasks = ["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"]
    n = 2
    actual = sol.leastInterval(tasks, n)
    expected = 16
    assert actual == expected

    tasks = ["A", "A", "A", "B", "B", "B"]
    n = 4
    actual = sol.leastInterval(tasks, n)
    expected = 12
    assert actual == expected
