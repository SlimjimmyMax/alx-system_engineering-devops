#!/usr/bin/python3
"""
Retrieve TODO list progress from a REST API and export it to CSV.
"""

import csv
import requests
import sys


def export_to_csv(employee_id):
    """
    Retrieve and export TODO list progress.
    """
    base_url = "https://jsonplaceholder.typicode.com/"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    try:
        # Fetch user information
        user_response = requests.get(user_url)
        user_data = user_response.json()
        user_id = user_data.get("id")
        employee_name = user_data.get("name")

        # Fetch TODO list information
        todos_response = requests.get(todos_url)
        todos_data = todos_response.json()

        # Write tasks to CSV file
        filename = f"{user_id}.csv"
        with open(filename, "w", newline="") as csvfile:
            fieldnames = [
                "USER_ID",
                "USERNAME",
                "TASK_COMPLETED_STATUS",
                "TASK_TITLE"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for task in todos_data:
                writer.writerow({
                    "USER_ID": user_id,
                    "USERNAME": name,
                    "TASK_COMPLETED_STATUS": str(task.get("completed")),
                    "TASK_TITLE": task.get("title")
                })

        print(f"TODO list progress exported to {filename}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    export_to_csv(employee_id)
