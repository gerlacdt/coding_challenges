"""Given two words (beginWord and endWord), and a dictionary's word list,
find the length of shortest transformation sequence from beginWord to
endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.


Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.

"""

from collections import defaultdict, deque
from typing import List, Set
import os


DEBUG = os.environ.get("DEBUG")


def debug(s):
    if DEBUG:
        print(s)
    return


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0

        # build graph

        # naivly building graph is time complexity O(n**2) which is
        # too slow for leetcode

        L = len(beginWord)

        def buildGraph():
            graph = defaultdict(set)
            if beginWord not in wordList:
                wordList.append(beginWord)
            for w in wordList:
                for i in range(L):
                    graph[w[:i] + "*" + w[i + 1 :]].add(w)
            debug("graph: {}".format(graph))
            return graph

        # bfs over graph
        def bfs(graph, start, goal):
            visited: Set = set()
            frontier = deque([(start, 1)])
            while frontier:
                current, level = frontier.popleft()
                visited.add(current)
                if current == goal:
                    return level
                for succ in successors(graph, current):
                    if succ not in visited:
                        frontier.append((succ, level + 1))
            return 0

        def successors(graph, current):
            succs = []
            for i in range(L):
                star_word = current[:i] + "*" + current[i + 1 :]
                for w in graph[star_word]:
                    succs.append(w)
            return succs

        return bfs(buildGraph(), beginWord, endWord)


def test1():
    sol = Solution()
    beginWord = "hit"
    endWord = "cog"
    words = ["hot", "dot", "dog", "lot", "log", "cog"]
    actual = sol.ladderLength(beginWord, endWord, words)
    expected = 5
    assert actual == expected

    beginWord = "hit"
    endWord = "cog"
    words = ["hot", "dot", "dog", "lot", "log"]
    actual = sol.ladderLength(beginWord, endWord, words)
    expected = 0
    assert actual == expected

    beginWord = "a"
    endWord = "c"
    words = ["a", "b", "c"]
    actual = sol.ladderLength(beginWord, endWord, words)
    expected = 2
    assert actual == expected

    beginWord = "leet"
    endWord = "code"
    words = ["lest", "leet", "lose", "code", "lode", "robe", "lost"]
    actual = sol.ladderLength(beginWord, endWord, words)
    expected = 6
    assert actual == expected
