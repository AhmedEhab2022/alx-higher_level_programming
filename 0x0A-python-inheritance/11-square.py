#!/usr/bin/python3

"""Define a class Square"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square that inherits from Rectangle (9-rectangle.py)

    Attributes:
        __size: Private instance size

    Args:
        size: the size of the square

    """

    def __init__(self, size):
        """constractor of the square"""

        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Calculate the area of square"""

        return self.__size ** 2

    def __str__(self):
        """string representaion when use print function"""

        return f"[Square] {self.__size:d}/{self.__size:d}"
