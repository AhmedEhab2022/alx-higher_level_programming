#!/usr/bin/python3
"""
Python script that  takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter
"""
import sys
import requests


if __name__ == "__main__":
    letter = sys.argv[1]
    url = 'http://0.0.0.0:5000/search_user'
    if letter:
        value = {'q': letter}
        response = requests.post(url, data=value)
        if response.headers.get('Content-Type') != 'application/json':
            print('Not a valid JSON')
        elif response.text and len(response.text) == 0:
            print('No result')
        else:
            data_json = response.json()
            id = data_json.get('id')
            name = data_json.get('name')
            print(f'[{id}] {name}')
    else:
        print('No result')
