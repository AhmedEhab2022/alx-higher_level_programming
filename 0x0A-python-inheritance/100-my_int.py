#!/usr/bin/python3

"""Define a class MyInt"""


class MyInt(int):
    """A class that inherted from int"""

    def __eq__(self, other):
        """Inverts the == operator"""

        return not int(self) == other

    def __ne__(self, other):
        """Inverts the != operator"""

        return not int(self) != other
