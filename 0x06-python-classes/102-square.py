#!/usr/bin/python3

"""Define a class Square"""


class Square:
    """
    Represents a square

    Attributes:
        __size: Private instance size

    Args:
        __size: the size of the square

    """
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """
        gets the size of the square

        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        sets the size of the square

        """
        if type(value) != int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """
        calculate the area of square

        Returns:
            int: area. the area of the square

        """
        return self.__size ** 2

    def __le__(self, other):
        """Represent the <= comparison operator for two squares"""

        return self.area() <= other.area()

    def __ge__(self, other):
        """Represent the >= comparison operator for two squares"""

        return self.area() >= other.area()

    def __eq__(self, other):
        """Represent the == comparison operator for two squares"""

        return self.area() == other.area()

    def __gt__(self, other):
        """Represent the > comparison operator for two squares"""

        return self.area() > other.area()

    def __lt__(self, other):
        """Represent the < comparison operator for two squares"""

        return self.area() < other.area()

    def __ne__(self, other):
        """Represent the != comparison operator for two squares"""

        return self.area() != other.area()
