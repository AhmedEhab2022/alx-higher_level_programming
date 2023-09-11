#!/usr/bin/python3

"""Define a class MyList"""


class MyList(list):
    """Represents a MyList that inherits from list

    Attributes:
        Nothing

     Args:
        Nothing
    """

    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""

        print(sorted(self))
