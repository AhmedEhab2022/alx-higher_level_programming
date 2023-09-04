#!/usr/bin/python3
"""Module to define a rectangle"""


class Rectangle:
    """Defines a rectangle"""
    def __init__(self, width=0, height=0):
        """Constructor of rectangle class"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter of width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Getter of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter of height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """Return the area of rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """Return the perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0

        return (self.__width * 2) + (self.__height * 2)

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