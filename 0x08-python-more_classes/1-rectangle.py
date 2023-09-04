#!/usr/bin/python3

"""Module class define a rectangle"""


class Rectangle:
    """Represents a rectangle

    Attributes:
        __width: Private instance width of the rectangle
        __height: Private instance height of the rectangle

    Args:
        width: the width of the rectangle
        height: the height of thr rectangle
    """

    def __init__(self, width=0, height=0):
        self.__width = __width
        self.__height = __height

    @property
    def width(self):
        """gets the width"""

        return self.__width

    @width.setter
    def width(self, value):
        """sets the width"""

        if type(value) not in [float, int]:
            raise TypeError('width must be an integer')

        if value < 0:
            raise ValueError('width must be >= 0')

        self.__width = value

    @property
    def height(self):
        """gets the height"""

        return self.__height

    @height.setter
    def height(self, value):
        """sets the height"""

        if type(value) not in [float, int]:
            raise TypeError('height must be an integer')

        if value < 0:
            raise ValueError('height must be >= 0')

        self.__height = value
