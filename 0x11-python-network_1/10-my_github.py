#!/usr/bin/python3
"""
Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""
import sys
import requests


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    url = 'https://@' + password + 'api.github.com/users/' + username
    response = requests.get(url)
    if response:
        data = response.json()
        print(data.get('id'))
    else:
        print(None)
