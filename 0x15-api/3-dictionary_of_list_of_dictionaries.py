#!/usr/bin/python3
"""
Fetches information about all employees and exports their TODO list progress
in a JSON format.

The JSON file will have a dictionary with the user ID as the key, and a list of
dictionaries for each TODO task as the value. Each task dictionary will contain
`task`, `completed`, and `username` fields.
"""

import json
import requests

def fetch_data(url):
    """Fetch data from the given URL and return the JSON response."""
    response = requests.get(url)
    return response.json()

def main():
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    users = fetch_data(users_url)
    todos = fetch_data(todos_url)

    data = {}

    for user in users:
        user_id = user['id']
        username = user['username']
        user_todos = [
            {"task": todo['title'], "completed": todo['completed'], "username": username}
            for todo in todos if todo['userId'] == user_id
        ]
        data[user_id] = user_todos

    json_filename = "todo_all_employees.json"

    with open(json_filename, mode='w') as json_file:
        json.dump(data, json_file)

if __name__ == "__main__":
    main()

