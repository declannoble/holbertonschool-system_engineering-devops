#!/usr/bin/python3
"""
script to query reddit api and return list of hot posts
of given subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    headers = {'User-Agent': 'HolbertonSchoolApiRequests (by /u/declannoble)'}
    url = 'https://www.reddit.com/r/{:}/hot.json?after={:}'.format(
        subreddit, after)
    req = requests.get(url, headers=headers, allow_redirects=False)
    if req.status_code == 200:
        data_dict = req.json().get('data')
        children = data_dict.get('children')
        for post in children:
            post_data_dict = post.get('data')
            hot_list.append(post_data_dict.get('title'))
        after = data_dict.get('after')
        if data_dict.get('after') is None:
            return hot_list
        return recurse(subreddit, hot_list, after)
    else:
        return None
