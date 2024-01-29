#!/usr/bin/python3
""" Gather data from an API, and export to CSV format"""
import requests
from sys import argv
import csv


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

    csv_file = f'{user_id}.csv'
    with open(csv_file, mode='w') as file:
        writer = csv.writer(file)
        writer.writerow(
            ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        for todo in todos:
            writer.writerow(
                    [user_id, info['username'],
                    str(todo['completed']), todo['title']]
            )
            if todo['completed']:
                print(f"\t {todo['title']}")


if __name__ == "__main__":
    user_id = int(argv[1])
    todo_progress(user_id)
