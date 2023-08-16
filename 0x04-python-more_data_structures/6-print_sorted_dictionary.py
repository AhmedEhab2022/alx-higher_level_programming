#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for key in sorted(a_dictionary):
        if type(a_dictionary[key]) == int:
            print("{} : {:d}".format(key, a_dictionary[key]))
        else:
            print("{} : {}".format(key, a_dictionary[key]))
