#!/usr/bin/python3
"""
Python script that takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter, and displays
the body of the response (decoded in utf-8)
"""
import urllib.request
import sys
import urllib.parse


if __name__ == "__main__":
    url, email = sys.argv[1], sys.argv[2]
    values = {'email': email}
    data = urllib.parse.urlencode(values).encode('ascii')
    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(url, data) as response:
        body = response.read()
        print(body.decode('utf-8'))
