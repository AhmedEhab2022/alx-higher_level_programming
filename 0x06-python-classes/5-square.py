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
        if type(size) != int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
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

    def my_print(self):
        """
        prints in stdout the square with the character #

        """
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end='')
            print()
        if self.__size == 0:
            print()
