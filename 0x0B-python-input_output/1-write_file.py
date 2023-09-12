#!/usr/bin/python3

"""Deine a function write_file"""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8) and
    returns the number of characters written"""

    if type(filename) is not str:
        raise TypeError('filename must be string')

    if type(text) is not str:
        raise TypeError('text must be string')

    with open(filename, "w", encoding='utf-8') as f:
        no_chars = f.write(text)
        return no_chars
