#!/usr/bin/python3
"""
Script that uses REST API to fetch TODO list progress for a given employee ID
and exports the data to a CSV file.
"""
import csv
import requests
import sys

def fetch_data(url):
    """Fetch data from the given URL and return the JSON response."""
    response = requests.get(url)
    return response.json()

def main(employee_id):
    # API URLs
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    # Fetch data from APIs
    user = fetch_data(user_url)
    todos = fetch_data(todos_url)

    # Extract username
    username = user['username']

    # CSV file name
    csv_filename = f"{employee_id}.csv"

    # Write to CSV file
    with open(csv_filename, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

        for todo in todos:
            writer.writerow([todo['userId'], username, todo['completed'], todo['title']])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./1-export_to_CSV.py <employee_id>")
        sys.exit(1)
    employee_id = sys.argv[1]
    main(employee_id)

