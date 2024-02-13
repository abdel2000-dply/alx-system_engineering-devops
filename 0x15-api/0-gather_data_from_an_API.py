#!/usr/bin/python3
""" Gather data from an API """
import requests
from sys import argv


def todo_progress(user_id):
    info_url = f'https://jsonplaceholder.typicode.com/users/{user_id}'
    todos_url = f'https://jsonplaceholder.typicode.com/users/{user_id}/todos'
    todos_response = requests.get(todos_url)
    info_response = requests.get(info_url)

    todos = todos_response.json()
    info = info_response.json()

    total_tasks = len(todos)
    completed_tasks = sum(todo['completed'] for todo in todos)

    print("Employee {} is done with tasks({}/{}):".format(
        info['name'], completed_tasks, total_tasks
    ))

    for todo in todos:
        if todo['completed']:
            print(f"\t {todo['title']}")


if __name__ == "__main__":
    user_id = int(argv[1])
    todo_progress(user_id)
