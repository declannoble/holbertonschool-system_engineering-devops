#!/usr/bin/python3

from email import header
import requests


def top_ten(subreddit):
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent': 'HolbertonSchoolApiRequests (by /u/declannoble)'}
    req = requests.get(url, headers=headers)
    if req.status_code == 404:
        return None
    data = req.json().get('data')
    children = data.get('children')

    for posts in children:
        postDict = posts.get('data')
        print(postDict.get('title'))
