#!/usr/bin/python3

def print_square(size):
    """prints a square with the character #.

    Args:
        size: the size length of the square

    Return:
        nothing
    """

    if type(size) != int:
        raise TypeError('size must be an integer')

    if size < 0:
        raise ValueError('size must be >= 0')

    for i in range(size):
        for j in range(size):
            print('#', end='')
        print("")
