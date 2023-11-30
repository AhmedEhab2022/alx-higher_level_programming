#!/usr/bin/python3
""" Module contain find_peak function """


def find_peak(list_of_integers):
    """Finds a Peak in a list of integers"""

    if list_of_integers:
        size = len(list_of_integers)
        listInt = list_of_integers
        for i in range(size):
            if i == 0 and listInt[i] >= listInt[i + 1]:
                return listInt[i]
            elif i == size - 1 and listInt[i] > listInt[i - 1]:
                return listInt[i]
            elif listInt[i] >= listInt[i - 1] and listInt[i] >= listInt[i + 1]:
                return listInt[i]
