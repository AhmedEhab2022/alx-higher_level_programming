#!/usr/bin/python3

"""Define a class BaseGeometry"""


class BaseGeometry:
    """base class for Geometric shapes"""

    def area(self):
        """raises an Exception with the message area() is not implemented"""

        raise Exception('area() is not implemented')
