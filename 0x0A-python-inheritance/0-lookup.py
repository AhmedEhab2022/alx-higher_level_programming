#!/usr/bin/python3

"""Define a lookup function"""


def lookup(obj):
    """returns the list of available attributes and methods of an object

    Args:
        obj: the object

    Return:
        returns the list of available attributes and methods

    """

    return dir(obj)
