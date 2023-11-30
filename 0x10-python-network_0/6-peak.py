#!/usr/bin/python3
""" Module contain find_peak function """


def find_peak(list_of_integers):
    """Finds a Peak in a list of integers"""

    if list_of_integers:
        size = len(list_of_integers)
        listInt = list_of_integers.copy()
        return sorted(listInt)[size - 1]
