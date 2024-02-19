#!/usr/bin/python3
"""Export user's tasks data to JSON"""

import json
import requests
from sys import argv


def export_user_tasks(user_id):
    """Export user's tasks data to JSON"""

    # Define the base URL for the API
    base_url = 'https://jsonplaceholder.typicode.com'

    # Get user data
    user_response = requests.get(f'{base_url}/users/{user_id}')
    user_data = user_response.json()

    # Get user's tasks data
    tasks_response = requests.get(f'{base_url}/todos?userId={user_id}')
    tasks_data = tasks_response.json()

    # Prepare data for export
    user_tasks = {user_id: []}
    for task in tasks_data:
        task_info = {
            'task': task['title'],
            'completed': task['completed'],
            'username': user_data.get("name")
        }
        user_tasks[user_id].append(task_info)

    # Export to JSON
    with open(f'{user_id}.json', 'w') as json_file:
        json.dump(user_tasks, json_file, indent=4)


if __name__ == '__main__':
    if len(argv) != 2:
        print("Usage: python3 export_to_json.py <user_id>")
    else:
        export_user_tasks(argv[1])
