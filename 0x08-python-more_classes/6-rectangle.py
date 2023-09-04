#!/usr/bin/python3

"""Module class define a rectangle"""


class Rectangle:
    """Represents a rectangle

    Attributes:
        __width: Private instance width of the rectangle
        __height: Private instance height of the rectangle
        number_of_instances: Public class that calculate the number of instance

    Args:
        width: the width of the rectangle
        height: the height of thr rectangle
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def __repr__(self):
        """return a string representation of the rectangle
        to be able to recreate a new instance by using eval()
        """

        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Print the message Bye rectangle...(... being 3 dots not ellipsis)
        when an instance of Rectangle is deleted
        """

        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
