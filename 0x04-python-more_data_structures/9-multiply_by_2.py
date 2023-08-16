#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    cp_dict = a_dictionary.copy()
    for key in cp_dict.keys():
        cp_dict[key] *= 2
    return cp_dict
