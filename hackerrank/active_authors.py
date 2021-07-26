import urllib.request
from collections import defaultdict
import json


def getUsernames(threshold):
    url = "https://jsonmock.hackerrank.com/api/article_users?page={}"
    total_pages = 0
    total_submissions = defaultdict(int)
    with urllib.request.urlopen(url.format(1)) as response:
        body = json.loads(response.read())
        total_pages = body["total_pages"]

    for i in range(1, total_pages + 1):
        with urllib.request.urlopen(url.format(i)) as response:
            body = json.loads(response.read())
            data = body["data"]
            for author in data:
                total_submissions[author["username"]] += int(author["submission_count"])

    return [
        username for username, count in total_submissions.items() if count > threshold
    ]


def test():
    actual = getUsernames(10)
    expected = [
        "epaga",
        "panny",
        "olalonde",
        "WisNorCan",
        "dmmalam",
        "replicatorblog",
        "vladikoff",
        "mpweiher",
        "coloneltcb",
        "guelo",
    ]
    assert expected == actual
