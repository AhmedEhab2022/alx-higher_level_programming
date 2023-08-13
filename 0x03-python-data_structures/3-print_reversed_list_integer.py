#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if len(my_list) > 0:
        rev_list = my_list.copy()
        rev_list.reverse()
        for ele in rev_list:
            print("{:d}".format(ele))
