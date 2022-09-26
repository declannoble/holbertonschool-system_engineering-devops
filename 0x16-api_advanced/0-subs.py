#!/usr/bin/python3
"""
script to query reddit api and return number of subscribers to given subreddit
"""

import requests


def number_of_subscribers(subreddit):

    if subreddit is None or type(subreddit) is not str:
        return 0

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'HolbertonSchoolApiRequests (by /u/declannoble)'}
    req = requests.get(url, headers=headers).json()
    data = req.get("data")
    subs = data.get('subscribers')

    return (subs)
