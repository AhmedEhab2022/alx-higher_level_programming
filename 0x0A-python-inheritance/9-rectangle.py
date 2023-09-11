#!/usr/bin/python3
"""Define a class Rectangle"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle  inherits from BaseGeometry (7-base_geometry.py)

    Attributes:
        __width: Private instance width of the rectangle
        __height: Private instance height of the rectangle

    Args:
        width: the width of the rectangle
        height: the height of thr rectangle
    """

    def __init__(self, width, height):
        """constractor of the rectangle"""

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Calculate the area of the rectangle"""

        return (self.__width * self.__height)

    def __str__(self):
        """string representaton when use print function"""

        return f"[Rectangle] {self.__width:d}/{self.__height:d}"
