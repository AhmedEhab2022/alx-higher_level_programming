#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for key, val in sorted(a_dictionary.items()):
        if type(val) == int:
            print("{} : {:d}".format(key, val))
        else:
            print("{} : {}".format(key, val))
