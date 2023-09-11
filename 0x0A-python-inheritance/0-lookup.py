#!/usr/bin/python3

def lookup(obj):
    """returns the list of available attributes and methods of an object

    Args:
        obj: the object

    Return:
        returns the list of available attributes and methods

    """

    return obj.__dict__
