#!/usr/bin/python3

"""Deine a function save_to_json_file"""

import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation"""

    if type(filename) is not str:
        raise TypeError('filename must be string')

    json_repr = json.dumps(my_obj)
    with open(filename, "w") as f:
        f.write(json_repr)
