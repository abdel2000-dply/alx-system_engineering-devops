#!/usr/bin/python3
""" Dictionary of list of dictionaries """
import json
import requests


def fetch_todo_data():
    """ Fetches todo data """
    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url)
    return response.json()


def organize_data(todo_data):
    """Organizes todo data based on user IDs."""
    organized_data = {}
    for task in todo_data:
        user_id = task['userId']
        if user_id not in organized_data:
            organized_data[user_id] = []
        organized_data[user_id].append({
            "username": task['title'],
            "task": task['title'],
            "completed": task['completed']
        })
    return organized_data


def export_to_json(organized_data):
    """Exports organized data to a JSON file."""
    filename = "todo_all_employees.json"
    with open(filename, 'w') as json_file:
        json.dump(organized_data, json_file)


def main():
    """Main function to fetch, organize, and export data."""
    todo_data = fetch_todo_data()
    organized_data = organize_data(todo_data)
    export_to_json(organized_data)


if __name__ == "__main__":
    main()
