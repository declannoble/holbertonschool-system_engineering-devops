#!/usr/bin/python3
"""
script to query reddit api and return number of subscribers to given subreddit
"""

import requests


def number_of_subscribers(subreddit):

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'HolbertonSchoolApiRequests (by /u/declannoble)'}
    req = requests.get(url, headers=headers)

    if req.status_code == 404:
        return 0

    data = req.json().get("data")
    subs = data.get('subscribers')

    return (subs)
