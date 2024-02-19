#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID, returns
information about his/her TODO list progress.
"""

import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: {} <employee_id>".format(argv[0]))
        exit(1)

    employee_id = argv[1]

    # Fetch user info
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(employee_id)
    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_name = user_data.get('name')

    # Fetch todo list
    todo_url = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(employee_id)
    todo_response = requests.get(todo_url)
    todo_data = todo_response.json()

    # Filter completed tasks
    completed_tasks = [task for task in todo_data if task.get('completed')]

    # Output employee todo list progress
    print("Employee {} is done with tasks({}/{}):".format(employee_name, len(completed_tasks), len(todo_data)))
    for task in completed_tasks:
        print("\t {}".format(task.get('title')))
