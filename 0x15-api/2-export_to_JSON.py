#!/usr/bin/python3
"""
script to query an api and store returned information
in a json file
"""
import json
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
    task_list = []
    for tasks in taskQuery:
        task_dict = {}
        task_dict['task'] = tasks.get('title')
        task_dict['completed'] = tasks.get('completed')
        task_dict['username'] = user_name
        task_list.append(task_dict)
        jsonObj = {}
        jsonObj[user_id] = task_list
        with open("{}.json".format(user_id), 'w') as fd:
            json.dump(jsonObj, fd)
