#!/usr/bin/python3

"""Define a function is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """Checking if the object is an instance of, or if the object is an
    instance of a class that inherited from, the specified class

    Args:
        obj: the object
        a_class: the specified class

    Return:
        True if the object is an instance of, or if the object is
        an instance of a class that inherited from, the specified class ;
        otherwise False.
    """

    return isinstance(obj, a_class)
