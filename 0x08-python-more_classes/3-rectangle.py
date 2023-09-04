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
        if type(width) not in [float, int]:
            raise TypeError('width must be an integer')

        if width < 0:
            raise ValueError('width must be >= 0')

        if type(height) not in [float, int]:
            raise TypeError('height must be an integer')

        if height < 0:
            raise ValueError('height must be >= 0')

        self.__width = width
        self.__height = height

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

    def area(self):
        """Calculate the area of the rectangle"""

        return self.__width * self.__height

    def perimeter(self):
        """Calculate the perimeter of the rectangle"""

        if self.__width == 0 or self.__height == 0:
            return 0

        return (self.__width + self.__height) * 2

    def __str__(self):
        """print a rectangle with character #"""

        output = ''
        if self.__width == 0 or self.__height == 0:
            return output

        for i in range(self.__height):
            for j in range(self.__width):
                output += '#'
            if i < self.__height - 1:
                output += '\n'

        return output
