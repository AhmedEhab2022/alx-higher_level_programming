#!/usr/bin/python3

"""Define a function is_same_class"""


def is_same_class(obj, a_class):
    """Checking if he object is exactly an instance of the specified class

    Args:
        obj: the object
        a_class: the specified class

    Return:
        True if the object is exactly an instance of the specified class;
        otherwise False

    """
    if (a_class != object):
        return isinstance(obj, a_class)
    else:
        return False
