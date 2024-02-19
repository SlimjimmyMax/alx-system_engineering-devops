#!/usr/bin/python3
"""
Retrieve TODO list progress from a REST API and export it to CSV.
"""
import json
import requests
import sys

def export_to_csv(user_id):
    url = 'https://jsonplaceholder.typicode.com/todos'
    response = requests.get(url, params={'userId': user_id})
    todos = response.json()

    filename = f"{user_id}.csv"
    with open(filename, 'w') as f:
        f.write('"USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"\n')
        for todo in todos:
            user_id = todo['userId']
            username = todo['title']
            completed = todo['completed']
            task_title = todo['title'].replace('"', '""')  # Handling double quotes in task title
            f.write(f'"{user_id}","{username}","{completed}","{task_title}"\n')

def export_to_json():
    url = 'https://jsonplaceholder.typicode.com/todos'
    response = requests.get(url)
    todos = response.json()

    user_tasks = {}
    for todo in todos:
        user_id = str(todo['userId'])
        username = todo['username']
        task_title = todo['title']
        completed = todo['completed']
        
        task_info = {"username": username, "task": task_title, "completed": completed}
        
        if user_id in user_tasks:
            user_tasks[user_id].append(task_info)
        else:
            user_tasks[user_id] = [task_info]

    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(user_tasks, json_file, indent=4)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        user_id = int(sys.argv[1])
        export_to_csv(user_id)
    else:
        export_to_json()
