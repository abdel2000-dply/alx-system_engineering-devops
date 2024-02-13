#!/usr/bin/python3
"""
This module contains a function that queries the Reddit API
and returns the number of subscribers for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """ Returns the number of subscribers for a given subreddit. """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'MyCustomUserAgent/1.0'}
    response = requests.get(url, allow_redirects=False, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0
