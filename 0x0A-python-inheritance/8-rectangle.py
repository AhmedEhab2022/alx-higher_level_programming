#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""Define a class Rectangle"""


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

        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
