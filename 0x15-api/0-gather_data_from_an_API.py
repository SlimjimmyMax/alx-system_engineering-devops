#!/usr/bin/python3
"""
Script to retrieve information  from API
"""

import requests
from sys import argv


def fetch_todo_list(employee_id):
    """
    Fetches the TODO list for a given employee ID from the JSONPlaceholder API.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        dict: Dictionary containing the employee's TODO list.
    """
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    response = requests.get(url)
    return response.json()


def main():
    """
    Main function to process command-line input and fetch employee TODO list.
    """
    if len(argv) != 2:
        print("Usage: ./gather_data_from_an_API.py <employee_id>")
        return

    employee_id = int(argv[1])
    todo_list = fetch_todo_list(employee_id)

    done_tasks = [task for task in todo_list if task.get('completed')]
    total_tasks = len(todo_list)
    done_count = len(done_tasks)
    employee_name = todo_list[0]['username']

    print(
        f"Employee {employee_name} is done ({done_count}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t{task['title']}")


if __name__ == "__main__":
    main()
