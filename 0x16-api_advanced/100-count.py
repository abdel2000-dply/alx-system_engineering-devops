#!/usr/bin/python3
""" count it! """
import requests


def count_words(subreddit, word_list, after=None, count_dict={}):
    """ count it! """
    if after is None:
        url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    else:
        url = f'https://www.reddit.com/r/{subreddit}/hot.json?after={after}'

    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return

    data = response.json().get('data')
    children = data.get('children')

    for child in children:
        title = child.get('data').get('title').lower()
        for word in word_list:
            count = title.count(word.lower())
            if count > 0:
                if word in count_dict:
                    count_dict[word] += count
                else:
                    count_dict[word] = count

    after = data.get('after')
    if after is None:
        sorted_counts = sorted(count_dict.items(), key=lambda x: (-x[1], x[0]))
        # The lambda function is used as the key parameter in the sorted()
        for word, count in sorted_counts:
            print('{}: {}'.format(word, count))
    else:
        count_words(subreddit, word_list, after, count_dict)
