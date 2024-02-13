#!/usr/bin/python3
"""  Recurse it! """
import requests


def recurse(subreddit, hot_list=[], after=None):
    """ Recurse it! """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "MyCustomUserAgent/1.0"}
    params = {"limit": 100, "after": after}
    response = requests.get(
        url, allow_redirects=False, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        children = data.get("data", {}).get("children", [])
        for child in children:
            title = child.get("data", {}).get("title")
            hot_list.append(title)

        after = data.get("data", {}).get("after")
        if after is not None:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list

    return None
