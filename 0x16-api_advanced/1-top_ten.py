#!/usr/bin/python3
"""
This module contains a function that queries the Reddit API
"""
import requests

headers = {'User-Agent': 'Mozilla/5.0'}


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    response = requests.get(url, allow_redirects=False, headers=headers)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            title = post['data']['title']
            print(title)
    else:
        print(None)
