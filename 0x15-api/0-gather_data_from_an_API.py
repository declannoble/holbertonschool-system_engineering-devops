#!/usr/bin/python3
"""script to query an api and return information"""


import requests
from sys import argv


if __name__ == "__main__":
    num_tasks = 0
    completed = 0
    completed_tasks = []
    uQuery = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                          .format(argv[1])).json()
    tQuery = requests.get(
                'https://jsonplaceholder.typicode.com/todos/?userId={}'
                .format(argv[1])).json()
    for tasks in tQuery:
        num_tasks += 1
        if tasks.get('completed') is True:
            completed += 1
            completed_tasks.append(tasks.get('title'))
        print("Employee {} is done with tasks({}/{}):".format(
                uQuery.get('name'), completed, num_tasks))
        for item in completed_tasks:
            print("\t {}".format(item))
