#!/usr/bin/python3
"""
script to query an api and store returned information
in a json file
"""
import json
import requests

if __name__ == "__main__":
    userQuery = requests.get("https://jsonplaceholder.typicode.com/users"
                             ).json()
    userDict = {}
    userNameDict = {}
    for user in userQuery:
        userId = user.get("id")
        userDict[userID] = []
        userNameDict[userId] = user.get("username")
    taskQuery = requests.get("https://jsonplaceholder.typicode.com/todos")
    .json()
    for task in taskQuery:
        taskDict = {}
        userId = task.get("userId")
        taskDict["task"] = task.get('title')
        taskDict["completed"] = task.get('completed')
        taskDict["username"] = userNameDict.get(userId)
        userDict.get(userId).append(taskDict)
    with open("todo_all_employees.json", 'w') as fd:
        json.dump(userDict, fd)
