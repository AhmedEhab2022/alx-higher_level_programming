#!/usr/bin/python3
""" Module contain find_peak function """


def find_peak(list_of_integers):
    """Finds a Peak in a list of integers"""

    if list_of_integers:
        size = len(list_of_integers)
        listInt = list_of_integers.copy()
        if listInt[0] >= listInt[1]:
            return listInt[0]
        if listInt[size - 1] >= listInt[size - 2]:
            return listInt[size - 1]

        for i in range(1, size - 1, 1):
            if listInt[i] >= listInt[i + 1]:
                return listInt[i]
