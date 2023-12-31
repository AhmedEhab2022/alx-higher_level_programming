#!/usr/bin/python3

"""Define a class Square"""


class Square:
    """
    Represents a square

    Attributes:
        __size: Private instance size
        __position: Private instance position

    Args:
        __size: the size of the square
        __position: a tuple that has a position to fill lines by spaces

    """
    def __init__(self, size=0, position=(0, 0)):
        if type(size) != int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        if type(position) != tuple:
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(position) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if type(position[0]) != int or type(position[1]) != int:
            raise TypeError('position must be a tuple of 2 positive integers')
        if position[0] < 0 or position[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """gets the size of the square"""

        return self.__size

    @size.setter
    def size(self, value):
        """sets the size of the square"""

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
        """prints in stdout the square with the character #"""

        if self.__size == 0:
            print()
            return
        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            for k in range(self.__position[0]):
                print(' ', end='')
            for j in range(self.__size):
                print("#", end='')
            print()

    @property
    def position(self):
        """gets the position"""

        return self.__position

    @position.setter
    def position(self, value):
        """sets the position"""

        if type(value) != tuple:
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if type(value[0]) != int or type(value[1]) != int:
            raise TypeError('position must be a tuple of 2 positive integers')
        if value[0] < 0 or value[1] < 0 or len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def __str__(self):
        """makes Printing a Square instance
        have the same behavior as my_print()"""

        str_to_print = ""
        if self.__size == 0:
            return str_to_print

        for i in range(self.__position[1]):
            str_to_print += "\n"
        for i in range(self.__size):
            for k in range(self.__position[0]):
                str_to_print += " "
            for j in range(self.__size):
                str_to_print += "#"
            if i + 1 < self.__size:
                str_to_print += "\n"

        return str_to_print
