"""You are given a list of (website, user) paris that represent users
visiting websites. Come up with a program that identifies the top k
pairs of websites with the greatest similarity.

For example, suppose k=1, and the list of tuples is:

pairs = [('google.com', 1), ('google.com', 3), ('google.com', 5),
         ('pets.com', 1), ('pets.com', 2),
         ('yahoo.com', 6), ('yahoo.com', 2), ('yahoo.com', 3) ('yahoo.com', 5), ('yahoo.com', 5),
         ('wikipedia.org', 4), ('wikipedia.org', 5), ('wikipedia.org', 6), ('wikipedia.org', 7),
         ('bing.com', 1), ('bing.com', 3), ('bing.com', 5), ('bing.com', 6),
]

To compute the similarity between two websites you should compute the
number of users they have in common divided by the number of users who
have visited either site in total. (This is known as the Jacard index).

For example, in this case, we would conclude that google.com and
bing.com are the most similar, with a score of 3/4 or 0.75.

"""

from collections import defaultdict
import heapq

pairs = [
    ("google.com", 1),
    ("google.com", 3),
    ("google.com", 5),
    ("pets.com", 1),
    ("pets.com", 2),
    ("yahoo.com", 6),
    ("yahoo.com", 2),
    ("yahoo.com", 3),
    ("yahoo.com", 5),
    ("yahoo.com", 5),
    ("wikipedia.org", 4),
    ("wikipedia.org", 5),
    ("wikipedia.org", 6),
    ("wikipedia.org", 7),
    ("bing.com", 1),
    ("bing.com", 3),
    ("bing.com", 5),
    ("bing.com", 6),
]


class MaxHeap:
    def __init__(self):
        self.heap = []

    def push(self, item):
        index, user = item
        heapq.heappush(self.heap, (-index, user))

    def pop(self):
        index, user = heapq.heappop(self.heap)
        return (-index, user)


def jacardIndex(pages, p1, p2):
    return len(pages[p1] & pages[p2]) / len(pages[p1] | pages[p2])


def kSimilarWebsites(pairs, k=1):
    # build map with key: website and value: set of users
    pages = defaultdict(set)
    heap = MaxHeap()
    for p in pairs:
        webpage, user = p
        pages[webpage].add(user)

    sites = list(pages.keys())
    for i in range(len(sites) - 1):
        for j in range(i + 1, len(sites)):
            score = jacardIndex(pages, sites[i], sites[j])
            heap.push((score, frozenset([sites[i], sites[j]])))
    return [heap.pop() for i in range(k)]


def testK1():
    actual = kSimilarWebsites(pairs, 1)
    expected = [(0.75, frozenset(["bing.com", "google.com"]))]
    assert actual == expected


def testK3():
    actual = kSimilarWebsites(pairs, 3)
    expected = [
        (0.75, frozenset(["bing.com", "google.com"])),
        (0.6, frozenset(["yahoo.com", "bing.com"])),
        (0.4, frozenset(["google.com", "yahoo.com"])),
    ]
    assert actual == expected
