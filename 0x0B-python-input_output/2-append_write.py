#!/usr/bin/python3

"""Deine a function append_write"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file (UTF8) and
    returns the number of characters added"""

    if type(filename) is not str:
        raise TypeError('filename must be string')

    if type(text) is not str:
        raise TypeError('text must be string')

    with open(filename, "a", encoding='utf-8') as f:
        return f.write(text)
