#!/usr/bin/python3
""" Dictionary of list of dictionaries """
import json
import requests


if __name__ == "__main__":
    users_url = "https://jsonplaceholder.typicode.com/users"
    users_response = requests.get(users_url)
    users_data = users_response.json()

    tasks_url = "https://jsonplaceholder.typicode.com/todos"
    tasks_response = requests.get(tasks_url)
    tasks_data = tasks_response.json()

    user_tasks = {}

    for task in tasks_data:
        user_id = task['userId']
        username = next(
            user['username'] for user in users_data if user['id'] == user_id)
        """
        instead of generator expression:

        username = None
        for user in users_data:
            if user['id'] == user_id:
                username = user['username']
                break
        """

        if user_id not in user_tasks:
            user_tasks[user_id] = []

        task_info = {
            "username": username,
            "task": task["title"],
            "completed": task["completed"]
        }

        user_tasks[user_id].append(task_info)

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(user_tasks, json_file)
