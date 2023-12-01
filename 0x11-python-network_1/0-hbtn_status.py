#!/usr/bin/python3
""" Python script that fetches https://alx-intranet.hbtn.io/status """
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as res:
        data = res.read()
        print("Body response:")
        print('    - type: {}'.format(type(data)))
        print('    - content: {}'.format(data))
        print('    - utf8 content: {}'.format(data.decode('utf-8')))
