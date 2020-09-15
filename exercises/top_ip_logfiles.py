"""Given an access logfile from a web server which contains all
requests with corresponding IP addresses per line.

Find the K-most occuring IP addresses.

"""

from collections import Counter
from heapq import heappush, heappop

LOGFILE = """192.168.33.1 - - [15/Oct/2019:19:41:46 +0000] "GET / HTTP/1.1" 200 396 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"
192.168.33.2 - - [15/Oct/2019:19:41:46 +0000] "GET / HTTP/1.1" 200 396 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"
192.168.33.3 - - [15/Oct/2019:19:41:46 +0000] "GET / HTTP/1.1" 200 396 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"
192.168.33.4 - - [15/Oct/2019:19:41:46 +0000] "GET / HTTP/1.1" 200 396 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"
192.168.33.1 - - [15/Oct/2019:19:41:46 +0000] "GET / HTTP/1.1" 200 396 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"
192.168.33.1 - - [15/Oct/2019:19:41:46 +0000] "GET / HTTP/1.1" 200 396 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"
192.168.33.1 - - [15/Oct/2019:19:41:46 +0000] "GET / HTTP/1.1" 200 396 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"
192.168.33.2 - - [15/Oct/2019:19:41:46 +0000] "GET / HTTP/1.1" 200 396 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"
192.168.33.2 - - [15/Oct/2019:19:41:46 +0000] "GET / HTTP/1.1" 200 396 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"
192.168.33.3 - - [15/Oct/2019:19:41:46 +0000] "GET / HTTP/1.1" 200 396 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"
"""


def getIPs(logfile):
    ips = []
    lines = logfile.splitlines()
    for line in lines:
        parts = line.split()
        ips.append(parts[0])
    return ips


def topK(logfile, K=3):
    # parse logfile, get only ip addresses
    ips = getIPs(logfile)

    # count number of ip-addresses
    ipCounts = Counter(ips)

    # put all ip-address with count (count, ip-address) in MAX-heap
    heap = []
    for ip, count in ipCounts.items():
        # we want to simulate a MAX-heap in order to pop the highest counts first
        heappush(heap, (-count, ip))

    # pop K ip address from heap
    result = []
    for i in range(K):
        count, ip = heappop(heap)
        result.append(ip)

    return result


def testGetIPs():
    lines = """192.168.33.4 - - [15/Oct/2019:19:41:46 +0000] "GET / HTTP/1.1" 200 396 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"
192.168.33.2 - - [15/Oct/2019:19:41:46 +0000] "GET / HTTP/1.1" 200 396 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"
"""
    actual = getIPs(lines)
    expected = ["192.168.33.4", "192.168.33.2"]
    assert actual == expected


def testTopK():
    actual = topK(LOGFILE, 3)
    expected = ["192.168.33.1", "192.168.33.2", "192.168.33.3"]
    assert actual == expected
