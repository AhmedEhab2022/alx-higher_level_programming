#!/usr/bin/python3
""" Module contain find_peak function """


def find_peak(list_of_integers):
    """Finds a Peak in a list of integers"""

    if list_of_integers:
        size = len(list_of_integers)
        listInt = list_of_integers.copy()
        l, r = 0, size - 1
        while l < r:
            mid = (l + r) // 2
            if listInt[mid] >= listInt[mid + 1]:
                return listInt[mid]
            else:
                l = mid + 1
