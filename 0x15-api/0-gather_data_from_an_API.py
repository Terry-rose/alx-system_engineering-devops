#!/usr/bin/python3
"""
Script that uses REST API to fetch TODO list progress for a given employee ID.
"""

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
    employee_name = user_data.get("name")

    todos_url = "{}/todos?userId={}".format(base_url, employee_id)
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    completed_tasks = [todo for todo in todos_data if todo.get("completed")]
    total_tasks = len(todos_data)
    done_tasks = len(completed_tasks)

    print("Employee {} is done with tasks({}/{}):".format(employee_name, done_tasks, total_tasks))
    for task in completed_tasks:
        print("\t {}".format(task.get("title")))

