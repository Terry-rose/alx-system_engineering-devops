#!/usr/bin/python3
"""
Script that uses REST API to fetch TODO list progress for a given employee ID
and exports the data to a JSON file.
"""

import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    base_url = "https://jsonplaceholder.typicode.com"

    user_url = "{}/users/{}".format(base_url, employee_id)
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print("Error: User not found.")
        sys.exit(1)

    user_data = user_response.json()
    employee_username = user_data.get("username")

    todos_url = "{}/todos?userId={}".format(base_url, employee_id)
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    tasks = []
    for task in todos_data:
        task_dict = {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": employee_username
        }
        tasks.append(task_dict)

    json_data = {str(employee_id): tasks}

    json_filename = "{}.json".format(employee_id)
    with open(json_filename, 'w') as json_file:
        json.dump(json_data, json_file)

