#!/usr/bin/python3
"""Define a function inherits_from"""


def inherits_from(obj, a_class):
    """Checking if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class"""

    return issubclass(type(obj), a_class) and type(obj) != a_class
