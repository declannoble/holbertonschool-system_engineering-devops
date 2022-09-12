#!/usr/bin/python3
"""
script to query dummy api and export info to CSV
"""
import csv
import requests
from sys import argv

if __name__ == "__main__":

    user_id = argv[1]

    userQuery = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                             .format(user_id)).json()
    taskQuery = requests.get(
                'https://jsonplaceholder.typicode.com/todos/?userId={}'
                .format(user_id)).json()
    user_name = userQuery.get('username')

    with open('{}.csv'.format(user_id), 'w', newline='') as fd:
        fileWriter = csv.writer(fd, quoting=csv.QUOTE_ALL)
        for tasks in taskQuery:
            fileWriter.writerow([int(user_id), user_name,
                                 tasks.get('completed'),
                                 tasks.get('title')])
