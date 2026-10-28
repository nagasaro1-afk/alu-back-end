#!/usr/bin/python3
"""Export an employee's TODO list to a CSV file."""
import csv
import requests
import sys

if __name__ == "__main__":
    base = "https://jsonplaceholder.typicode.com"
    user_id = sys.argv[1]
    user = requests.get("{}/users/{}".format(base, user_id)).json()
    todos = requests.get(
        "{}/todos".format(base), params={"userId": user_id}
    ).json()
    username = user.get("username")
    with open("{}.csv".format(user_id), "w", newline="") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL, lineterminator="\n")
        for t in todos:
            writer.writerow(
                [user_id, username, t.get("completed"), t.get("title")])
