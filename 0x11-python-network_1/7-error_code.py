#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to
the URL and displays the body of the response (decoded in utf-8)
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        response = requests.get(url)
        print(response.text)
    except requests.exceptions.HTTPError as e:
        print(f'Error code: {e.response.status_code}')
